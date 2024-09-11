meme_dict = { 
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("anlamını bilmediğiniz kelimeyi yazın : ") 

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(word, "kelimesinin anlamı : ",meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("yazdığınız kelime sözlükte yok")
