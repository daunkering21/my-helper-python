import http.client
import time
import threading
from urllib.parse import urlparse

def send_request(url, fake_ip):
    parsed_url = urlparse(url)

    if not parsed_url.scheme:
        print(f"URL tidak valid: {url}")
        return

    conn = http.client.HTTPConnection(parsed_url.netloc, timeout=10) 
    
    headers = {
        'X-Forwarded-For': fake_ip, 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        conn.request("GET", parsed_url.path or "/", headers=headers)
    except Exception as e:
        print(f"Error saat mengirim request ke {url} dengan IP {fake_ip}: {e}")
    finally:
        conn.close()

def main(url, num_requests):
    fake_ips = [
        "192.168.1.101", 
        "192.168.1.102", 
        "192.168.1.103",
        "192.168.1.104", 
        "192.168.1.105", 
        "192.168.1.106",
        "192.168.1.107", 
        "192.168.1.108", 
        "192.168.1.109",
        "192.168.1.110",
    ] 
    
    threads = []
    
    for i in range(num_requests):
        fake_ip = fake_ips[i % len(fake_ips)]
        thread = threading.Thread(target=send_request, args=(url, fake_ip))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = input("Masukkan URL yang akan diakses (dengan http/https): ")
    
    try:
        num_requests = int(input("Masukkan jumlah request yang ingin dikirim: "))
    except ValueError:
        print("Input jumlah request harus berupa angka.")
        exit(1)

    start_time = time.time()
    
    main(url, num_requests)
    
    print(f"Took {time.time() - start_time:.2f} seconds")
