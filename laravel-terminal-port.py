# pip install psutil rich

import psutil
import time
from rich.console import Console
from rich.table import Table


console = Console()
laravel_servers = {} 

def get_laravel_servers(): 
    global laravel_servers
    current_servers = {}

    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            pid = conn.pid
            port = conn.laddr.port
            ip = conn.laddr.ip

            try:
                process = psutil.Process(pid)
                process_name = process.name().lower()

                if 'php' in process_name and 'cgi' not in process_name:
                    current_servers[pid] = {
                        'pid': pid,
                        'ip': ip,
                        'port': port,
                        'process': process_name
                    }

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    for pid, server in current_servers.items():
        if pid not in laravel_servers:
            laravel_servers[pid] = server
            console.print(f"[green]Server Laravel baru terdeteksi:[/green] PID: {server['pid']}, IP: {server['ip']}, Port: {server['port']}")

    for pid in list(laravel_servers.keys()):
        if pid not in current_servers:
            console.print(f"[red]Server Laravel berhenti:[/red] PID: {laravel_servers[pid]['pid']}, Port: {laravel_servers[pid]['port']}")
            del laravel_servers[pid]

def display_table():
    table = Table(title="Server Laravel yang Berjalan")

    table.add_column("PID", justify="right", style="cyan")
    table.add_column("IP Address", style="magenta")
    table.add_column("Port", justify="right", style="yellow")
    table.add_column("Process", style="green")

    for server in laravel_servers.values():
        table.add_row(str(server['pid']), server['ip'], str(server['port']), server['process'])

    console.clear()
    console.print(table)

if __name__ == "__main__":
    console.print("[bold yellow]Mendeteksi server Laravel yang berjalan... (Tekan Ctrl+C untuk keluar)[/bold yellow]\n")

    while True:
        get_laravel_servers()
        display_table()
        time.sleep(60)