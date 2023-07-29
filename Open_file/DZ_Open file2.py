from operator import itemgetter

a = ['1.txt', '2.txt', '3.txt']
c = []
for j in a:
    with open(j, encoding='utf-8') as f:
        lines = f.readlines()
        c.append([j, len(lines), lines])
res = sorted(c, key=itemgetter(1))
with open('output.txt', 'w', encoding='utf-8') as z:
    for j in res:
        z.write(f'{j[0]}\n{j[1]}\n{"".join(j[2])}')
