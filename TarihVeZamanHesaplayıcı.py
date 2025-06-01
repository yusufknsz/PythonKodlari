import time
import sys
from fractions import Fraction
from datetime import datetime, timedelta
import calendar



def zaman_goster():
    try:
        oran_str = input("Kendi evreninde 1 saniye, dünya zamanında kaç saniyeye eşit? (örn: 2, 0.5 ya da 1/2): ")
        oran = float(Fraction(oran_str))

        if oran == 0:
            raise ValueError("Oran sıfır olamaz!")  # 0'a bölünme hatasını engellemek için

    except Exception as e: #Hataları yakalamak ve belirtmek için
        print(f"Hata: {e}")
        sys.exit()

    start_world = time.time()  

    while True:
        world_seconds = int(time.time() - start_world) 

        # Dünya saati
        w_s = world_seconds % 60
        w_m = (world_seconds // 60)
        w_h = (world_seconds // 3600)

        # Evren saati
        universe_seconds = int(world_seconds / oran) #Evren saatindeki 1 saniyeyi belirliyoruz
        u_s = universe_seconds % 60         #mod alma işlemleriyle sınırlar içinde hesaplamalar yapabiliyoruz.
        u_m = (universe_seconds // 60) % 60
        u_h = (universe_seconds // 3600) % 24

        print(f"\r[Dünya] {w_h:02}:{w_m:02}:{w_s:02} | [Evren] {u_h:02}:{u_m:02}:{u_s:02}", end="") #02 ile 2 li yazım formatını kullanıyoruz
        time.sleep(1)




def tarih_giris(mesaj):
    while True:
        tarih_str = input(mesaj + " (GG.AA.YYYY): ")
        try:
            tarih = datetime.strptime(tarih_str, "%d.%m.%Y")
            return tarih
        except ValueError:
            print("Geçersiz tarih formatı veya tarih değeri! Lütfen geçerli bir tarih giriniz (örneğin: 28.02.2024).")




def zaman_giris():
    while True:
        try:
            yil = int(input("Yıl: "))
            if yil < 0:
                print("Yıl negatif olamaz!")
                continue

            ay = int(input("Ay (1-12): "))
            if ay < 1 or ay > 12:
                print("Ay 1 ile 12 arasında olmalı!")
                continue

            max_gun = calendar.monthrange(yil, ay)[1]
            gun = int(input(f"Gün (1-{max_gun}): "))
            if gun < 1 or gun > max_gun:
                print(f"{calendar.month_name[ay]} ayında en fazla {max_gun} gün olabilir.")
                continue

            return yil, ay, gun

        except ValueError:
            print("Lütfen sadece tam sayı giriniz!")


def hesap_makinesi():
    print("İşlem türünü seçin: (1) Toplama, (2) Çıkarma, (3) Çarpma, (4) Bölme")
    secim = input("Seçiminiz: ")

    if secim in ["1", "2"]:
        tarih = tarih_giris("Tarihi giriniz")
        print("Eklenecek/Çıkarılacak zamanı giriniz:")
        yil, ay, gun = zaman_giris()
        # Ayları ve yılları gün cinsinden çevirmek (yaklaşık):
        toplam_gun = gun + ay * 30 + yil * 365
        fark = timedelta(days=toplam_gun)
 
        if secim == "1":
            sonuc = tarih + fark
        if secim =="2":
            sonuc = tarih - fark

        print("Sonuç:", sonuc.strftime("%d.%m.%Y"))

    elif secim in ["3", "4"]:
        print("Zamanı giriniz:")
        yil, ay, gun = zaman_giris()
        sayi = int(input("Sayı: "))

        if secim == "3":
            yil *= sayi
            ay *= sayi
            gun *= sayi
        else:
            if sayi == 0:
                print("Sıfıra bölünemez!")
                return
            yil //= sayi
            ay //= sayi
            gun //= sayi

        print(f"Sonuç: {yil} yıl, {ay} ay, {gun} gün")

    else:
        print("Geçersiz seçim!")

# Program başlangıcı
while True:
    print("\n--- Zaman İşlemleri Programı ---")
    print("1 - Zaman Gösterimi")
    print("2 - Hesap Makinesi")
    print("0 - Çıkış")
    secim = input("Seçiminizi girin: ")

    if secim == "1":
        zaman_goster()
        secim = input("Çıkış için 0: ")
        

    elif secim == "2":
        hesap_makinesi()
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
