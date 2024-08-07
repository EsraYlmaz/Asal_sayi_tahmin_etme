def asal_sayi_mi(sayi):              #Asal sayıyı kontrol ettirme

    if sayi <= 1:                    #Sayı bir veya birden küçük ise asal değildir
         return False
    for i in range(2,sayi):          #2'den sayıya kadar olan aralığı kontrol etmesi
       
            if (sayi % i) == 0:      #Sayı i'ye tam bölünüyorsa asal değil
                return False
    return True 
def asalsayi():
    while True:
        try:
            sayi= int(input("bir sayı giriniz"))
            if asal_sayi_mi(sayi): 
                 print(f'{sayi} asal sayıdır')
            else: 
                 print(f'{sayi} asal sayı değildir')
        except ValueError: 
             print("geçerli değil")
        devam=input("Başka bir sayı denemek ister misiniz? (evet/hayır):")
        if devam.lower() != 'evet':
             print("çıkış")
             break
asalsayi() 
