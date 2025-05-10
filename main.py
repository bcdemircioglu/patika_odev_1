#Girilen Sayinin Pozitif, Negatif veya 0 oldugunu yazan metot
def find_number_status(sayi) :
    if sayi > 0:
        print('Girdiginiz sayi pozitiftir')
    elif sayi < 0:
        print('Girdiginiz sayi negatiftir')
    else:
        print('Girdiniz sayi 0')

#Girilen Sayinin tek mi cift mi oldugunu yazan metot
def find_odd_or_even(sayi):
    if sayi < 0:
        print('Lutfen pozitif bir tam sayi giriniz')
    elif sayi % 2 == 0:
        print('Girdiginiz sayi cifttir')
    else:
        print('Girdiginiz sayi tektir')

# Girilen nota gore harf notunu belirleyen metot
def find_grade(grade) :
    if 80 <= grade <= 100:
        print('Notunuz A')
    elif 60<=grade<80:
        print('Notunuz B')
    elif 50<=grade<60:
        print('Notunuz C')
    else:
        print('Notunuz D')

# Girilen ismin uzunluguna gore durumu yazdiran metot
def find_name_status(name) :
    if len(name.strip()) > 5 :
        print('Uzun bir isminiz var')
    else:
        print(name)

# Girilen sayinin asal olup olmadigini bulan metot
def find_is_prime(sayi) :
    if sayi == 0 :
        print('Lutfen 2 den buyuk bir sayi giriniz. En kucuk asal sayi 2dir')
    if sayi % 2 == 0  and sayi % sayi == 0 :
        print('Sayiniz asaldir')
    else:
        print('Sayiniz asaldir degil')

