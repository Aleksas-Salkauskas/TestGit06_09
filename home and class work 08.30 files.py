# -------------------------------------------files----------------------------------------------------------------
# absoliutus kelias iki failo
# darasyti \ kur reikia kad python neskaitytu kaip komanda
# file=open("C:\\Users\Aleks\OneDrive\Desktop\\Namu darbai\Python namu darbai\home and class work 08.30 files.py")
# file=open("txt,txt", "r")
# -------------------------------------------------------------------------------------------------------------------
# fileHandler=open("C:/Users/Aleks/OneDrive/Desktop/Namu darbai/Python namu darbai/data//test.txt")
# try:
#     fileHandler=open("C:/Users/Aleks/OneDrive/Desktop//Namu darbai/Python namu darbai/data/test.txt")
#     if fileHandler:
#       print("file is open")
#     print(fileHandler.read(6))
#     print("-"*20)
#     print(fileHandler.read())
# except:
#     print("no file in directory")
# --------------------------------------------------------------------------------------------------------------------
# try:
#     fileHandler=open("C:/Users/Aleks/OneDrive/Desktop//Namu darbai/Python namu darbai/data/test.txt")
#
#     str1=fileHandler.readlines()
#     print(str1)
# except FileNotFoundError:
#     print("no file in directory")
# ---------------------------------------------------------------------------------------------------------------------
# try:
#     fileHandler=open("C:/Users/Aleks/OneDrive/Desktop//Namu darbai/Python namu darbai/data/test.txt", "r")
#     for line in fileHandler:
#        print(line)
# except FileNotFoundError:
#     print("no file in directory")
# ----------------------------------------------------------------------------------------------------------------------
# try:
#     fileHandler=open("test.text1","w+")
#     n=fileHandler.write("how to create text file via pyton")
#     print(f"we wrote {n} symbols")
# except FileNotFoundError:
#     print("no file in directory")
# ----------------------------------------------------------------------------------------------------------------------
# try:
#     fileHandler=open("test.text1","w")
#     for i in range(5):
#         fileHandler.write(f"this is line{i+1}\n")
#
#     fileHandler.close()
#     fileHandler=open("test.txt1","a")
#     myStr=["appended line\n", "appended line2\n"]
#     fileHandler.writelines(myStr)
#
# except FileNotFoundError:
#     print("no file in directory")
# ----------------------------------------homework task 1---------------------------------------------------------------

line1 = input("put in first line: ")
line2 = input("put in second line: ")
line3 = input("put in third line: ")

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")
print("lines writen in file data.txt")
#--------------------------------Homework task 2-----------------------------------------------------------------------
import os
filename="data.txt"

if os.path.exists(filename):
    print(f"file {filename} existing. printing ewery second line\n")
    with open(filename, "r", encoding="utf-8") as file:
        lines=file.readlines()
        for i in range (1, len(lines), 2):
            print(lines[i].strip())
else:
    print(f"file{filename} not found")











# 📄 Таблиця режимів відкриття файлів (текстові та двійкові)
# Режим	Опис	Обробка даних починається з…
#
# r	Відкриття текстового файлу лише для читання. Якщо такого файлу не існує, буде згенеровано виняток.	Початку файлу
#
# w	Відкриття текстового файлу лише для запису. Якщо такий файл не існує,
# він буде створений. Інакше його вміст буде видалено і файл буде перезаписано.	Початку файлу
#
# a	Відкриття текстового файлу для додавання. Якщо такий файл не існує, він буде створений.	Кінця файлу
#
# r+	Відкриття текстового файлу для читання та запису. Якщо такого файлу не існує, буде виведена помилка.	Початку файлу
#
# w+	Відкриття текстового файлу для читання та запису. Якщо такий файл не існує,
# він буде створений. Інакше його буде видалено і файл буде перезаписано.	Початку файлу
#
# a+	Відкриття текстового файлу для читання та додавання. Якщо такий файл не існує, він буде створений.	Кінця файлу
#
# rb	Відкриття двійкового файлу для читання. Якщо такого файлу не існує, буде виведена помилка.	Початку файлу
#
# wb	Відкриття двійкового файлу для запису. Якщо такий файл не існує, він буде створений.
# Інакше його буде видалено і файл буде перезаписано.	Початку файлу
#
# ab	Відкриття двійкового файлу для додавання. Якщо такий файл не існує, він буде створений.
# Інакше дані з нього будуть видалені.	Кінця файлу
#
# wb+	Відкриття двійкового файлу для читання та запису. Якщо такий файл не існує,
# він буде створений. Інакше його буде видалено і файл буде перезаписано.	Початку файлу
#
# ab+	Відкриття двійкового файлу для читання та додавання. Якщо такий файл не існує, він буде створений.
# Інакше його вміст буде видалено.	Кінця файлу