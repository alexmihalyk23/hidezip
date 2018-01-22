#coding: utf-8
try:
	namefile= input("Файл-Оболочка: ")
	with open(namefile, 'rb') as file1:
		read1=file1.read()
except FileNotFoundError:
	print("[x] Файл: '"+str(namefile)+ "'Не найден!")
	raise SystemExit
try:
	zipfile=input("Zip-Файл: ")
	with open(zipfile, 'rb') as file2:
		read2=file2.read()
except FileNotFoundError:
	print("[x] Zip-Файл: '"+str(namefile)+ "'Не найден!")
	raise SystemExit
with open(namefile, 'wb') as file3:
	file3.write(read1)
	file3.write(read2)
	print("[+] Файл: '"+str(namefile)+ "'успешно перезаписан!")
input()