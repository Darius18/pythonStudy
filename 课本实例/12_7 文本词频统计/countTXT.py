words = "im so tired running as fast as i can."
def getText():
    txt = open("gaga.txt","r").read()
    txt = txt.lower()
    for ch in '!"!@#$%^&*()':
        txt = txt.replace(ch, " ")
    return txt

gagaText = getText()
words = gagaText.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key =lambda x:x[1], reverse = True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
