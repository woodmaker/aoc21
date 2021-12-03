with open("input") as f:
    report = f.readlines()

report = [[int(x)
		for x
   		in
		r.strip()
	]
	for r 
	in report 
	if r
]
print(report)
g = [0]*12
e = [0]*12
for r in report:
    for i in range(len(r)):
        g[i] = g[i]+1 if r[i] else g[i]-1
        e[i] = e[i]+1 if r[i] else e[i]-1
g = [1 if x>0 else 0 for x in g]
g.reverse()
g = [(g[i]*(2**i)) for i in range(len(g))]
g = sum(g)
print(g)

e = [1 if x<0 else 0 for x in e]
e.reverse()
e = [(e[i]*(2**i)) for i in range(len(e))]
e = sum(e)
print(e)

print(g*e)

