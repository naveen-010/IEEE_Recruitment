words = list((input("Enter Paragraph: ")).split())

def is_pallin(word):

    word = word.lower()
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)] :
            return 0
    return 1

for word in words:
    print(word, end = " ") if is_pallin(word) else None
