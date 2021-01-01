import random
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


kapasitas_motor = c.execute('SELECT kapasitas_motor FROM setting WHERE id = 1').fetchall()
kapasitas_mobil = c.execute('SELECT kapasitas_mobil FROM setting WHERE id = 1').fetchall()
tarif_motor_per_jam = c.execute('SELECT tarif_motor FROM setting WHERE id = 1').fetchall()
tarif_mobil_per_jam = c.execute('SELECT tarif_mobil FROM setting WHERE id = 1').fetchall()
movie_list = ['Selamat Datang Di Parkir Modern', 'Keamanan kendaraan anda, prioritas kami']

moview_item = random.choice(movie_list)
print (moview_item)

class Kendaraan:
  def __init__(self, nopol):
    self.platnomor = nopol
  
  def plat_kendaraan(self):
    return self.platnomor

def show_menu():
    print(" ")
    print('Kapasitas Motor : '+str(kapasitas_motor).strip("[(,)]"))
    print('Kapasitas Mobil : '+str(kapasitas_mobil).strip("[(,)]"))
    print('Tarif Motor Per Jam : '+str(tarif_motor_per_jam).strip("[(,)]"))
    print('Tarif Mobil Per Jam : '+str(tarif_mobil_per_jam).strip("[(,)]"))
    print(" ")
    print("Pilih Jenis Kendaraan")
    print("[1] Roda Dua")
    print("[2] Roda Empat")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        motor()
    elif(selected_menu == "2"):
        mobil()
    else:
        print("Menu tidak ada")
        back_to_menu()

def motor():
    print(" ")
    print("Menu Kendaraan Roda Dua")
    print("[1] Tambah Data Kendaraan Roda Dua")
    print("[2] Perbarui Data Kendaraan Roda Dua")
    print("[3] Hapus Data Kendaraan Roda Dua")
    print("[4] Menu Utama")
    print("[5] Pengaturan")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        tambah_motor()
    elif(selected_menu == "2"):
        update_motor()
    elif(selected_menu == "3"):
        hapus_motor()
    elif(selected_menu == "4"):
        back_to_menu()
    elif(selected_menu == "5"):
        atur_motor()
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
        motor()
    elif(selected_menu == "2"):
        mobil()
    elif(selected_menu == "3"):
        mobil()
    elif(selected_menu == "4"):
        back_to_menu()
    elif(selected_menu == "5"):
        atur_mobil()
    else:
        print("Menu tidak ada")
        back_to_menu()

def atur_motor():
    kapasitas_motor = int(input("Masukkan Kapasitas Parkir Motor: "))
    tarif_motor = int(input("Masukkan Tarif Parkir Motor Per Jam: "))
    c.execute("UPDATE setting SET kapasitas_motor = ?, tarif_motor = ? WHERE id = 1;", (kapasitas_motor, tarif_motor))
    conn.commit()
    c.close()
    conn.close()

def atur_mobil():
    kapasitas_mobil = int(input("Masukkan Kapasitas Parkir Mobil: "))
    tarif_mobil = int(input("Masukkan Tarif Parkir Mobil Per Jam: "))
    c.execute("UPDATE setting SET kapasitas_mobil = ?, tarif_mobil = ? WHERE id = 1;", (kapasitas_mobil, tarif_mobil))
    conn.commit()
    c.close()
    conn.close()

def back_to_menu():
  show_menu()

def tambah_motor():
  class Motor(Kendaraan):
    def __init__(self, plat, durasi):
      super().__init__(plat)
      self.durasi = durasi

    def print_motor(self):
      print(super().plat_kendaraan(),self.durasi*tarif_motor_per_jam, self.durasi)

  nopol = input("Masukkan Nomor Polisi: ")
  durasi = int(input("Masukkan Durasi: "))
  bayar = durasi*tarif_motor_per_jam
  c.execute("INSERT INTO data VALUES(3,?,'Motor',?,?)", (nopol, durasi, bayar))
  conn.commit()
  c.close()
  conn.close()

  c.execute("UPDATE setting SET kapasitas_motor = kapasitas_motor - 1 WHERE id = 1;")
  conn.commit()
  c.close()
  conn.close()

def tambah_mobil():
  global kapasitas_mobil
  class Mobil(Kendaraan):
    def __init__(self, plat, durasi):
      super().__init__(plat)
      self.durasi = durasi

    def print_mobil(self):
      print(super().plat_kendaraan(),self.durasi*tarif_mobil_per_jam, self.durasi)

  nopol = input("Masukkan Nomor Polisi: ")
  durasi = int(input("Masukkan Durasi: "))
  x = Mobil(nopol, durasi)
  kapasitas_mobil -= 1
  x.print()

if __name__ == "__main__":
  while True:
    show_menu()

