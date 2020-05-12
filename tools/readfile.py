

a = []

with open("../zufangspider/poisecond.txt","r",encoding="utf-8") as f:
    a = f.readlines()
    # print(a)

b = []
for i in a:
    j = i.split("、")
    for n in j:
        b.append(n)
    # print(i)
print(b)
c = []
for i in b:
    if "\n" in i:
        v =i.replace("\n","")
        c.append(v)
    else:
        c.append(i)

print(c)
