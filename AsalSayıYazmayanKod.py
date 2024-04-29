n = int(input("Bir sayı giriniz"))
sayı = 2
while sayı <= n:
    sayaç = 0
    bolen = 1
    while bolen <= sayı:
        if sayı % bolen == 0:
            bolen = bolen + 1
            sayaç = sayaç + 1
        else:
            bolen = bolen + 1
    if sayaç == 2:
        pass
    else:
        print(sayı)
    sayı = sayı + 1
