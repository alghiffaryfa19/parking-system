###MEDIUM####
import random
movie_list = ['Selamat dan Semangat Chinta', 'Semangat Belajar Chinta', 'Semoga mendapat hasil yang baik Chinta', 'Usahamu tidak akan sia-sia Chinta']

moview_item = random.choice(movie_list)
print (moview_item)

def show_menu():
    print(" ")
    print("Menu Utama")
    print("[1] Hitung Luas Segitiga")
    print("[2] Hitung Luas Persegi")
    print("[3] Hitung Luas Lingkaran")
    print("[4] Hitung Daya Listrik")
    print("[5] Hitung Hambatan Listrik")
    print("[6] Hitung Gaya Gerak Listrik")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    if(selected_menu == "1"):
        segitiga()
    elif(selected_menu == "2"):
        persegi()
    elif(selected_menu == "3"):
        lingkaran()
    elif(selected_menu == "4"):
        daya()
    elif(selected_menu == "5"):
        hambatan()
    elif(selected_menu == "6"):
        gaya()
    else:
        print("Menu tidak ada")
        back_to_menu()

def back_to_menu():
    show_menu()

def segitiga():
  class Triangle():
    def __init__(self, alas, tinggi, half = 0.5):
      self.alas = alas
      self.tinggi = tinggi
      self.half = half

    def hitung(self):
        print("Luas Segitiga:",self.alas*self.tinggi*self.half, "cm2")
  
  a = int(input("Masukkan Alas (cm): "))
  t = int(input("Masukkan Tinggi (cm): "))

  Luas = Triangle(a,t)
  Luas.hitung()

def persegi():
  class Square():
    def __init__(self, sisi):
      self.sisi = sisi

    def hitung(self):
        print("Luas Persegi:",self.sisi*self.sisi, "cm2")
  
  s = int(input("Masukkan Sisi (cm): "))

  Luas = Square(s)
  Luas.hitung()

def lingkaran():
  class Circle():
    def __init__(self, jarijari, phi = 22/7):
      self.jarijari = jarijari
      self.phi = phi

    def hitung(self):
        print("Luas Lingkaran:",self.phi*self.jarijari*self.jarijari, "cm2")
  
  r = int(input("Masukkan Jari-Jari (cm2) :"))

  Luas = Circle(r)
  Luas.hitung()

def daya():
  class Daya():
    def __init__(self, w, t):
      self.w = w
      self.t = t

    def hitung(self):
        print("Daya Listrik:",self.w/self.t, "Joule")
  
  w = int(input("Masukkan W: "))
  t = int(input("Masukkan T: "))

  Luas = Daya(w, t)
  Luas.hitung()

def hambatan():
  class Hambatan():
    def __init__(self, v, i):
      self.v = v
      self.i = i

    def hitung(self):
        print("Hambatan Listrik:",self.v/self.i, "ohm")
  
  v = int(input("Masukkan v: "))
  i = int(input("Masukkan i: "))

  Hitung = Hambatan(v, i)
  Hitung.hitung()

def gaya():
  class Gaya():
    def __init__(self, w, q):
      self.w = w
      self.q = q

    def hitung(self):
        print("Gaya Gerak Listrik:",self.w/self.q, "V")
  
  w = int(input("Masukkan w: "))
  q = int(input("Masukkan q: "))

  Hitung = Gaya(w, q)
  Hitung.hitung()

if __name__ == "__main__":
    while True:
        show_menu()