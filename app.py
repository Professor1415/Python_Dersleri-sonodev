import db as m1
import methods as m2

urunler = m1.urunler
urunEkle = m2.urunEkle
urunGuncelle = m2.urunGuncelle
urunleriGetir = m2.urunleriGetir
urunEkle("iphone15", 60000)
urunGuncelle(1,"iphone 15 pro", 80000)
urunleriGetir()
