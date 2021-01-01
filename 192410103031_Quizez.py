###EZ###
import csv
import os
import operator


def show_menu():
    print(" ")
    print("Menu Utama")
    print("[1] Lihat Data")
    print("[2] Cari Data")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        show_data()
    elif(selected_menu == "2"):
        search_data(input("Isi nama atau nim yang akan dicari: "))
    else:
        print("Menu tidak ada")
        back_to_menu()

def back_to_menu():
    show_menu()

def show_data():
    with open('/Users/fauzanamiralghiffary/Desktop/Python/DaftarNama.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_data(namaataunim):
    with open('/Users/fauzanamiralghiffary/Desktop/Python/DaftarNama.csv', 'r+') as f:
        reader = csv.reader(f)
        for row in reader:
            for data in row:
                if namaataunim in data:
                    if row[2] < 3:
                        print('maaf kamu tidak memenuhi kualifikasi')
                    elif row[2] < 3.5 and row[3] > 4:
                        print('maaf kamu tidak memenuhi kualifikasi')
                    else:
                        print(row)   

if __name__ == "__main__":
    while True:
        show_menu()