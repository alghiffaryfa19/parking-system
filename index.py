import random #menggunakan library pengacak
import sqlite3 #menggunakan library sqlite

conn = sqlite3.connect('data.db') #koneksi database
c = conn.cursor()
kapasitas_motor = c.execute('SELECT kapasitas_motor FROM setting WHERE id = 1').fetchall() #mengambil value kapasitas motor dari database table setting
kapasitas_mobil = c.execute('SELECT kapasitas_mobil FROM setting WHERE id = 1').fetchall() #mengambil value kapasitas mobil dari database table setting
tarif_motor_per_jam = c.execute('SELECT tarif_motor FROM setting WHERE id = 1').fetchall() #mengambil value tarif motor dari database table setting
tarif_mobil_per_jam = c.execute('SELECT tarif_mobil FROM setting WHERE id = 1').fetchall() #mengambil value kapasitas mobil dari database table setting
c.close()
conn.close() #menutup koneksi database
movie_list = ['Selamat Datang Di Parkir Modern', 'Keamanan kendaraan anda, prioritas kami'] #array string welcome


moview_item = random.choice(movie_list) #mengacak string dari variable movie_list
print (moview_item) #menampilkan ucapan selamat datang

class Kendaraan: #class Kendaraan
    def __init__(self, plat): #konstruktor
        self.plat = plat
        
    def tambah(self): #abstrak method
        pass

    def update(self): #abstrak method
        pass

    def hapus(self): #abstrak method
        pass

    def atur(self): #abstrak method
        pass

class Motor(Kendaraan): #class motor subclass kendaraan
    def __init__(self, plat='', durasi=0, platlama = ''): #konstruktor
        self.plat = plat
        self.durasi = durasi
        self.platlama = platlama

    def tambah(self): #method tambah
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        jenis = 1 #jenis 1 untuk motor
        tarif = str(tarif_motor_per_jam).strip("[(,)]") #mengambil value tarif motor per jam
        bayar = self.durasi*int(tarif) #kalkulasi bayar
        c.execute("INSERT INTO data VALUES(?,?,?,?)", (self.plat, jenis, self.durasi, bayar)) #insert ke database
        c.execute("UPDATE setting SET kapasitas_motor = kapasitas_motor - 1 WHERE id = 1;") #mengurangi kapasitas parkir motor
        conn.commit()
        c.close()
        conn.close()

    def update(self): #method update    
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        tarif = str(tarif_motor_per_jam).strip("[(,)]") #mengambil value tarif motor per jam
        bayar = self.durasi*int(tarif) #kalkulasi bayar
        c.execute("UPDATE data SET plat = ?, durasi = ?, bayar = ? WHERE plat = ?;", (self.plat, self.durasi, bayar, self.platlama)) #memperbarui data
        conn.commit()
        c.close()
        conn.close()

    def hapus(self): #method hapus
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("DELETE FROM data WHERE plat = ?;", (self.plat,)) #menghapus data dari database
        c.execute("UPDATE setting SET kapasitas_motor = kapasitas_motor + 1 WHERE id = 1;") #menambah kapasitas parkir motor
        conn.commit()
        c.close()
        conn.close()

    def atur(self): #method atur
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        kapasitas_motor = int(input("Masukkan Kapasitas Parkir Motor: ")) #inputan konfigurasi kapasitas motor
        tarif_motor = int(input("Masukkan Tarif Parkir Motor Per Jam: ")) #inputan konfigurasi tarif motor perjam
        c.execute("UPDATE setting SET kapasitas_motor = ?, tarif_motor = ? WHERE id = 1;", (kapasitas_motor, tarif_motor)) #memperbarui data konfigurasi parkir motor
        conn.commit()
        c.close()
        conn.close()

class Mobil(Kendaraan): #class mobil subclass kendaraan
    def __init__(self, plat='', durasi=0, platlama = ''): #konstruktor
        self.plat = plat
        self.durasi = durasi
        self.platlama = platlama

    def tambah(self): #method tambah
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        jenis = 2
        tarif = str(tarif_mobil_per_jam).strip("[(,)]")
        bayar = self.durasi*int(tarif)
        c.execute("INSERT INTO data VALUES(?,?,?,?)", (self.plat, jenis, self.durasi, bayar))
        c.execute("UPDATE setting SET kapasitas_mobil = kapasitas_mobil - 1 WHERE id = 1;")
        conn.commit()
        c.close()
        conn.close()

    def update(self): #method update
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        tarif = str(tarif_mobil_per_jam).strip("[(,)]")
        bayar = self.durasi*int(tarif)
        c.execute("UPDATE data SET plat = ?, durasi = ?, bayar = ? WHERE plat = ?;", (self.plat, self.durasi, bayar, self.platlama))
        conn.commit()
        c.close()
        conn.close()

    def hapus(self): #method hapus
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("DELETE FROM data WHERE plat = ?;", (self.plat,))
        c.execute("UPDATE setting SET kapasitas_mobil = kapasitas_mobil + 1 WHERE id = 1;")
        conn.commit()
        c.close()
        conn.close()

    def atur(self): #method atur
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        kapasitas_mobil = int(input("Masukkan Kapasitas Parkir Mobil: "))
        tarif_mobil = int(input("Masukkan Tarif Parkir Mobil Per Jam: "))
        c.execute("UPDATE setting SET kapasitas_mobil = ?, tarif_mobil = ? WHERE id = 1;", (kapasitas_mobil, tarif_mobil))
        conn.commit()
        c.close()
        conn.close()

def show_menu(): #function menu utama
    print(" ")
    print('Kapasitas Motor : '+str(kapasitas_motor).strip("[(,)]")) #menampilkan kapasitas motor
    print('Kapasitas Mobil : '+str(kapasitas_mobil).strip("[(,)]")) #menampilkan kapasitas mobil
    print('Tarif Motor Per Jam : '+str(tarif_motor_per_jam).strip("[(,)]")) #menampilkan tarif motor per jam
    print('Tarif Mobil Per Jam : '+str(tarif_mobil_per_jam).strip("[(,)]")) #menampilkan tarif mobil per jam
    print(" ")
    print("Pilih Jenis Kendaraan")
    print("[1] Roda Dua")
    print("[2] Roda Empat")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        motor() #jika pilih 1 maka pilih motor
    elif(selected_menu == "2"):
        mobil() #jika pilih 2 maka pilih mobil
    else: #jika selain 1 dan 2 maka kembali ke menu utama
        print("Menu tidak ada")
        back_to_menu()

def back_to_menu(): #function kembali ke menu utama
    show_menu() #memanggil function menu utama

def motor(): #menu motor
    print(" ")
    print("Menu Kendaraan Roda Dua")
    print("[1] Tambah Data Kendaraan Roda Dua")
    print("[2] Perbarui Data Kendaraan Roda Dua")
    print("[3] Hapus Data Kendaraan Roda Dua")
    print("[4] Menu Utama")
    print("[5] Pengaturan")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"): #pilihan menu tambah data motor
        plat = input("Masukkan Nomor Polisi: ") #inputan plat nomor
        durasi = int(input("Masukkan Durasi: ")) #inputan durasi
        motor = Motor(plat,durasi) #inisialisasi class motor dengan argumen dari 2 variable sebelumnya
        motor.tambah() #memanggil method tambah dari class motor
    elif(selected_menu == "2"): #pilihan menu update data motor
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE jenis = 1') #menampilkan semua data motor
        for row in c.fetchall():
            print(row)
        c.close()
        conn.close()
        platlama = input("Masukkan Nomor Polisi Yang Ingin Diperbarui: ") #inputan plat nomor motor yang akan diperbarui datanya
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE plat = ?', (platlama,)) #mengecek apakah data ada sesuai inputan platnomor
        if res.fetchone() is None:
            print('Data Tidak Ada')
        else:
            plat_baru = input("Masukkan Nomor Polisi: ") #inputan plat baru
            durasi = int(input("Masukkan Durasi: ")) #inputan durasi
            motor = Motor(plat_baru,durasi,platlama) #inisialisasi class motor dengan argumen dari 3 variable sebelumnya
            motor.update() #memanggil method update dari class motor
        
        c.close()
        conn.close()

    elif(selected_menu == "3"):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE jenis = 1') #menampilkan semua data motor
        for row in c.fetchall():
            print(row)
        c.close()
        conn.close()

        plat = input("Masukkan Nomor Polisi Yang Ingin Dihapus: ") #inputan plat nomor motor yang akan dihapus datanya
        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        res = c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE plat = ?', (plat,)) #mengecek apakah data ada sesuai inputan platnomor
        if res.fetchone() is None:
            print('Data Tidak Ada')
        else:
            beli = Motor(plat) #inisialisasi class motor dengan argumen dari 1 variable sebelumnya
            beli.hapus() #memanggil method hapus dari class motor

        c.close()
        conn.close()
    elif(selected_menu == "4"):
        back_to_menu() #kembali ke menu utama
    elif(selected_menu == "5"):
        beli = Motor() #inisialisasi class motor
        beli.atur() #memanggil method atur dari class motor
    else:
        print("Menu tidak ada")
        back_to_menu()

def mobil():
    print(" ")
    print("Menu Kendaraan Roda Empat")
    print("[1] Tambah Data Kendaraan Roda Empat")
    print("[2] Perbarui Data Kendaraan Roda Empat")
    print("[3] Hapus Data Kendaraan Roda Empat")
    print("[4] Menu Utama")
    print("[5] Pengaturan")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        plat = input("Masukkan Nomor Polisi: ")
        durasi = int(input("Masukkan Durasi: "))
        beli = Mobil(plat,durasi)
        beli.tambah()
    elif(selected_menu == "2"):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE jenis = 2')
        for row in c.fetchall():
            print(row)
        c.close()
        conn.close()
        platlama = input("Masukkan Nomor Polisi Yang Ingin Diperbarui: ")
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE plat = ?', (platlama,))
        if res.fetchone() is None:
            print('Data Tidak Ada')
        else:
            plat_baru = input("Masukkan Nomor Polisi: ")
            durasi = int(input("Masukkan Durasi: "))
            beli = Mobil(plat_baru,durasi,platlama)
            beli.update()
        
        c.close()
        conn.close()

    elif(selected_menu == "3"):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE jenis = 2')
        for row in c.fetchall():
            print(row)
        c.close()
        conn.close()

        plat = input("Masukkan Nomor Polisi Yang Ingin Dihapus: ")
        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        res = c.execute('SELECT plat, CASE WHEN jenis = 1 THEN "Motor" WHEN jenis = 2 THEN "Mobil" ELSE "No" END, durasi ' ' || " Jam", bayar FROM data WHERE plat = ?', (plat,))
        if res.fetchone() is None:
            print('Data Tidak Ada')
        else:
            beli = Mobil(plat)
            beli.hapus()

        c.close()
        conn.close()
    elif(selected_menu == "4"):
        back_to_menu()
    elif(selected_menu == "5"):
        beli = Mobil()
        beli.atur()
    else:
        print("Menu tidak ada")
        back_to_menu()

if __name__ == "__main__": #ditampilkan paling awal ketika program dijalankan
    while True:
        show_menu() 


#materi yang diterapkan pada program ini adalah class, abstrac class, polymorphism overriding, function, database