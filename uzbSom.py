#%% Prosta Project
print("""---Valyuta Ayirboshlash
      1. Rubl -> So'm
      2. So'm -> Rubl
      3. So'm -> Dollar
      4. Dollar -> So'm
      -1. Chiqish uchun""")
soqqa = 0
while True:
        amal = int(input("Amalni tanlang: ")
        if(amal == -1):
            print("Yana kutamiz!")
            break
        if(amal == 1):        
            rublSom = float(input("Necha rublni so'm qilmoqchisiz: "))
            jamiRubl = 145.26 * rublSom
            print(jamiRubl,"so'm")
        elif(amal == 2):
            somRubl = float(input("Necha so'mni rubl qilmoqchisiz: "))
            jamiSom = 145.26 * somRubl
            print(jamiSom,"rubl")
        elif(amal == 3):
            somDollar = float(input("Necha so'mni dollar qilmoqchisiz: "))
            jamiDollarS = 0.000094  * somDollar
            print(jamiDollarS,"dollar")
        elif(amal == 4):
            dollarSom = float(input("Necha dollarni so'm qilmoqchisiz: "))
            jamiDollar = 10640.06 * dollarSom
            print(jamiDollar,"so'm")