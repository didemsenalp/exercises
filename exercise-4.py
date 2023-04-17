str = "pynative"
n= int(input("Değer:"))
characters_to_be_remove = []

if(len(str) >= n ):
    for index in range(n):
        new = str[index]
        characters_to_be_remove.append(new)
        print(characters_to_be_remove)
    for char in characters_to_be_remove:
        print(char)
        str = str.replace(char,"")
        print("Yeni str:" + str)
    
else:
    print("Lütfen silmek istediğiniz karakter sayısını doğru giriniz...")