#AIzaSyBbT2r7aeoJ85nvBDq6PGYclrcYj8sod50    api key
import requests
import csv
import pandas as pd

API_KEY = ''
def get_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def save_to_csv(books, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Authors', 'Publisher', 'Published Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books['items']:
            volume_info = book.get('volumeInfo')
            title = volume_info.get('title', 'N/A')
            authors = ', '.join(volume_info.get('authors', ['N/A']))
            publisher = volume_info.get('publisher', 'N/A')
            published_date = volume_info.get('publishedDate', 'N/A')
            writer.writerow({'Title': title, 'Authors': authors, 'Publisher': publisher, 'Published Date': published_date})

query = input("Kitap araması yapın: ")
books_data = get_books(query)

if 'items' in books_data:
    save_to_csv(books_data, 'kitaplar.csv')
    print("Kitaplar başarıyla kaydedildi.")
else:
    print("Herhangi bir kitap bulunamadı.")


df = pd.read_csv('kitaplar.csv')
print(df.head())
