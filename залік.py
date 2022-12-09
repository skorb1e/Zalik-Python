def readline():
    with open ("text.txt", "r") as f:
        a=f.readlines()
    return a
text=readline()

for i in text:
    print(i)    
wordfromuser=input("Яке слово ви хочете знайти в тексті - ")
l=0
for i in text:
    f=i.split(' ')
    for j in range(len(f)):
        k=j+1
        if f[j]==str(wordfromuser):
                print("Cлово знайдено в тексті в рядку\n", i, "\nце слово під номером - ", k)
                l=12
if l==0:
    print("Такого слова немає в тексті")
