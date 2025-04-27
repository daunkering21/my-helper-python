# pip install psutil rich

import psutil
import time
import os
from rich.console import Console
from rich.table import Table

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_laravel_servers():
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

    return current_servers

def display_table(laravel_servers):
    clear_screen()

    table = Table(title="List Running Laravel Servers")

    table.add_column("PID", justify="right", style="cyan")
    table.add_column("IP Address", style="magenta")
    table.add_column("Port", justify="right", style="yellow")
    table.add_column("Process", style="green")

    if laravel_servers:
        for server in laravel_servers.values():
            table.add_row(str(server['pid']), server['ip'], str(server['port']), server['process'])
    else:
        table.add_row("[dim]No Laravel Server detected[/dim]", "", "", "")

    console.print(table)

if __name__ == "__main__":
    console.print("[bold yellow]Detecting runing Laravel servers... (Press Ctrl+C to quit)[/bold yellow]\n")

    while True:
        laravel_servers = get_laravel_servers()
        display_table(laravel_servers) 
        time.sleep(5) 
