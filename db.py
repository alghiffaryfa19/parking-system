import sqlite3

class Prodi:
    def __init__(self, id_prodi):
        self.prodi_id = id_prodi
        
    def prodi(self):
      return self.prodi_id

def show_menu():
    print(" ")
    print("Pilih Jenis Kendaraan")
    print("[1] Program Studi")
    print("[2] Mahasiswa")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        prodi()
    elif(selected_menu == "2"):
        mahasiswa()
    else:
        print("Menu tidak ada")
        back_to_menu()

def prodi():
    print(" ")
    print("Menu Program Stdui")
    print("[1] Tambah Program Studi")
    print("[2] Lihat Program Studi")
    print("[3] Lihat Program Studi by ID")
    print("[4] Perbarui Program Studi")
    print("[5] Hapus Program Studi")
    print("[6] Menu Utama")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        tambah_prodi()
    elif(selected_menu == "2"):
        lihat_prodi()
    elif(selected_menu == "3"):
        lihat_prodi_id()
    elif(selected_menu == "4"):
        update_prodi()
    elif(selected_menu == "5"):
        hapus_prodi()
    elif(selected_menu == "6"):
        back_to_menu()
    else:
        print("Menu tidak ada")
        back_to_menu()

def mahasiswa():
    print(" ")
    print("Menu Mahasiswa")
    print("[1] Tambah Mahasiswa")
    print("[2] Lihat Mahasiswa")
    print("[3] Lihat Mahasiswa by NIM")
    print("[4] Perbarui Mahasiswa")
    print("[5] Hapus Mahasiswa")
    print("[6] Menu Utama")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        tambah_mahasiswa()
    elif(selected_menu == "2"):
        lihat_mahasiswa()
    elif(selected_menu == "3"):
        lihat_mahasiswa_by_nim()
    elif(selected_menu == "4"):
        perbarui_mahasiswa()
    elif(selected_menu == "5"):
        hapus_mahasiswa()
    elif(selected_menu == "6"):
        back_to_menu()
    else:
        print("Menu tidak ada")
        back_to_menu()

def back_to_menu():
  show_menu()

def tambah_prodi():
    kode_prodi = int(input("Kode Prodi: "))
    prodi = input("Masukkan Nama Prodi: ")
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM prodi WHERE id = ?', (kode_prodi,))
    if res.fetchone() is None:
        c.execute("INSERT INTO prodi VALUES(?,?)", (kode_prodi, prodi))
        conn.commit()
    else:
        print('Data Sudah Ada')
    c.close()
    conn.close()

def lihat_prodi():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prodi')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()

def lihat_prodi_id():
    id_prodi = int(input("Masukkan Kode Prodi: "))
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    res = c.execute('SELECT * FROM prodi WHERE id = ?', (id_prodi,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        c.execute('SELECT * FROM prodi WHERE id = ?', (id_prodi,))
        for row in c.fetchall():
            print(row)
    
    
    c.close()
    conn.close()

def update_prodi():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prodi')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()
    

    id_prodi = int(input("Masukkan Kode Prodi Yang Ingin Diperbarui: "))

    
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM prodi WHERE id = ?', (id_prodi,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        kode_prodi = int(input("Kode Prodi Baru: "))
        nama_prodi = input("Nama Prodi Baru: ")
        c.execute("UPDATE prodi SET id = ?, nama = ? WHERE id = ?;", (kode_prodi, nama_prodi, id_prodi))
        conn.commit()
    
    c.close()
    conn.close()

def hapus_prodi():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prodi')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()

    id_prodi = int(input("Masukkan Kode Prodi Yang Ingin Dihapus: "))
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    res = c.execute('SELECT * FROM prodi WHERE id = ?', (id_prodi,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        c.execute("DELETE FROM prodi WHERE id = ?;", (id_prodi,))
        conn.commit()

    c.close()
    conn.close()

def tambah_mahasiswa():
    class Mahasiswa(Prodi):
        def __init__(self, prodi_id, nim, nama):
            super().__init__(prodi_id)
            self.nim = nim
            self.nama = nama
            self.prodi_id = prodi_id
            
        def print_mahasiswa(self):
            print(super().prodi(),self.nim, self.nama)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prodi')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()

    nim = int(input("NIM: "))
    nama = input("Nama: ")
    prodi_id = int(input("ID Prodi: "))

    m1 = Mahasiswa(prodi_id, nim, nama)
    m1.print_mahasiswa()

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM mahasiswa WHERE nim = ?', (nim,))
    if res.fetchone() is None:
        c.execute("INSERT INTO mahasiswa VALUES(?,?,?)", (nim, nama, prodi_id))
        conn.commit()
    else:
        print('Data Sudah Ada')
    c.close()
    conn.close()

def lihat_mahasiswa():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT m.nim, m.nama, p.nama FROM mahasiswa m JOIN prodi p ON m.prodi_id = p.id')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()

def lihat_mahasiswa_by_nim():
    nim = int(input("Masukkan NIM: "))
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    res = c.execute('SELECT * FROM mahasiswa WHERE nim = ?', (nim,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        c.execute('SELECT m.nim, m.nama, p.nama FROM mahasiswa m JOIN prodi p ON m.prodi_id = p.id WHERE nim = ?', (nim,))
        for row in c.fetchall():
            print(row)
    c.close()
    conn.close()

def perbarui_mahasiswa():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT m.nim, m.nama, p.nama FROM mahasiswa m JOIN prodi p ON m.prodi_id = p.id')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()
    

    nim = int(input("Masukkan NIM Yang Ingin Diperbarui: "))

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prodi')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM mahasiswa WHERE nim = ?', (nim,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        nim_baru = int(input("NIM Baru: "))
        nama_baru = input("Nama Baru: ")
        prodi_baru = int(input("ID Prodi Baru: "))
        c.execute("UPDATE mahasiswa SET nim = ?, nama = ? WHERE prodi_id = ?;", (nim_baru, nama_baru, prodi_baru))
        conn.commit()
    
    c.close()
    conn.close()

def hapus_mahasiswa():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT m.nim, m.nama, p.nama FROM mahasiswa m JOIN prodi p ON m.prodi_id = p.id')
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()

    nim_mahasiswa = int(input("Masukkan NIM Ingin Dihapus: "))
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    res = c.execute('SELECT * FROM mahasiswa WHERE nim = ?', (nim_mahasiswa,))
    if res.fetchone() is None:
        print('Data Tidak Ada')
    else:
        c.execute("DELETE FROM mahasiswa WHERE nim = ?;", (nim_mahasiswa,))
        conn.commit()

    c.close()
    conn.close()


if __name__ == "__main__":
  while True:
    show_menu()

