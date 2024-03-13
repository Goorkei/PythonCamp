# 1 - Kulanicidan alinan sayinin tekmi ciftmi oldugunu bildiren kodu yaziniz.

def isSingle(sayi):
    if sayi%2==0:
        return False
    else:
        return True
    
# 2- Kullanicadan alinan sayinin tersini alan kodu yaziniz. Ornek: Girdi : -1 Cikti : 1 Girdi : 1 Cikti : -1
    
def Inverse(sayi):
    return sayi*-1



# 3 - Kullanicidan bir vize ve bir final notu isteyiniz.Eger vize ve final notu 0 ile 100 arasinda degilse ekrana hata mesaji veriniz.
# Eger 0 ile 100 arasinda ise not ortalamasinin %40 ni ile final notunun %60 nin toplami olarak hesaplayip ekranda yazdiriniz. 
# Ardindan not ortalamasini asagidaki kurala gore hesaplayip ekrana yazdiriniz.

def NotHesapla(vize,final):
    if (vize>0 and vize<=100) and (final>=0 and final<=100 ):
        result = vize*40+final*60
        return result/100
    return "Hatalı rakam girdiniz"


# 4 - Kullanicidan ucgen dikdortgen kare secmesini isteyiniz. Ardindan secim yanlissa hata mesaji veriniz. 
# Uygun sekilde secim yapilmissa secilen sekle gore kenar uzunluklarini isteyiniz ardindan alan ve cevre degerlerini hesaplayiniz.

def Sekil(sekil, kenar,yukseklik=1):
    if sekil=="üçgen":
        return kenar*yukseklik/2
    elif sekil=="kare":
        return kenar**2
    elif sekil=="dikdörtgen":
        return kenar*yukseklik
    return "Hatalı şekil girdiniz."
    
# 5- Kullanicidan iki sayi isteyiniz sonrasinda yapilmak istenilen islemi isteyiniz (carpma,bolme,toplama, cikarma). 
# Sonrasinda islemi yapip sonucu ekrana yazdiriniz.
def Islem(islem,sayi1,sayi2):
    if   islem=="toplama":
        return sayi1+sayi2
    elif islem == "çarpma":
        return sayi1*sayi2
    elif islem == "bölme":
        return sayi1/sayi2
    elif islem == "çıkarma":
        return sayi1-sayi2
    else:
        return "Hatalı işlem girdiniz."

 
# 6- Bir 4 haneli pin kodu belirleyiniz. Bu pin kodunu uygulamaniza kisiyi dogrulamakta kullanmak icin kullancaksiniz.
# Kullanici 3 kez yanlis pin girdiginde uyari mesaji vererek uygulamayi sonlandirir. Basarili giriste ise "Giris dogrulandi" seklinde ekrana bildirim versin.

def Giris(pin):
    sayac=0
    while(sayac<3):
        x = input("Pini girimiz:")
        if pin == x:
            return True
        sayac+=1
    return False
        
# 7- Kullanicidan bir sayi girilmesi istinilsin ekran girilen sayiya kadar olan sayilar yazdirilsin.

def SayiYazdir(sayi):
    for i in range(0,sayi):
        print(i) 

 
# 8 - Kullanicidan alt limit ust limit ve artis miktari istenilsin.
# Ekran alt limitten baslayarak artis miktari kadar artirarak ust limite kadar sayilar ekrana yazdirilsin.

def LimitliYazdir(altLimit, ustLimit, artisMiktari):
    for i in range(altLimit,ustLimit,artisMiktari):
        print(i)

# 9 - Kullanicidan alt limit ve ust limit alinsin ve aradaki sayilarin toplami hesaplansin.

def LimitliTopla(altLimit, ustLimit):
    sonuc=0
    for i in range(altLimit,ustLimit+1):
        sonuc+=i
    return sonuc
        


 
# 10 - Girilen sayinin faktoriyelini hesaplayan kodu yaziniz eger deger sifirdan kucukse hata mesaji verin 

def Faktoriyel(sayi):
    sonuc=1
    for i in range(2,sayi+1):
        sonuc*=i
    return sonuc

    
    