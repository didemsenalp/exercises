i = 0
str = "pynative"
list_of_even_index_character = []
list_of_odd_index_character = []
for character in str:
    i +=1
    if ( i % 2 == 0):
        list_of_even_index_character.append(character)
    else:
        list_of_odd_index_character.append(character)
    
    print("İndeksi çift olan harfler: ", list_of_even_index_character)
    print("İndeksi tek olan harfler: ", list_of_odd_index_character)
    
