# import requests
# from concurrent.futures import ThreadPoolExecutor

# # Fungsi untuk mengirim permintaan HTTP dan mencetak status code
# def send_request(url):
#     try:
#         response = requests.get(url)
#         print(response.status_code)
#     except requests.exceptions.RequestException:
#         print("Error")

# # Fungsi untuk mengatur uji beban
# def load_test(url, num_requests):
#     with ThreadPoolExecutor(max_workers=100000) as executor:
#         for _ in range(num_requests):
#             executor.submit(send_request, url)

# if __name__ == "__main__":
#     target_url = "https://dewajitugrup.com/"  # Ganti dengan URL server Anda
#     num_requests = 1000000  # Jumlah permintaan yang akan dikirim

#     load_test(target_url, num_requests)



# Script Ke-2
import requests
from concurrent.futures import ThreadPoolExecutor

# Fungsi untuk mengirim permintaan HTTP dan mencetak status code
def send_request(url):
    try:
        with requests.get(url) as response:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("500")

# Fungsi untuk mengatur uji beban
def load_test(url, num_requests):
    with ThreadPoolExecutor(max_workers=100000) as executor:
        executor.map(send_request, [url] * num_requests)

if __name__ == "__main__":
    target_url = "http://127.0.0.1:3306/"  # Ganti dengan URL server Anda
    num_requests = 1000000  # Jumlah permintaan yang akan dikirim

    load_test(target_url, num_requests)