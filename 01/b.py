with open("input") as f:
    reports = f.readlines()

def toint(x):
	try:
		return int(x)
	except:
		pass
reports = [toint(r.strip()) for r in reports]
reports = [r for r in reports if r]

r = reports

print(len(
    [
    v for v
    in range(len(reports)-3)
    if 
       sum(reports[v:v+3])
       <
       sum(reports[v+1:v+4])
    ]
    ))
