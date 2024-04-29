sayı = int(input("Bir sayı giriniz"))
sayaç = 0
bolen = 1
while bolen <= sayı:
    if sayı % bolen == 0:
        bolen = bolen + 1
        sayaç = sayaç + 1
    else:
        bolen = bolen + 1
if sayı % sayaç == 0:
    print("tau sayısıdır")
else:
    print("tau sayısı değildir")
