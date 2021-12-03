with open("input") as f:
    reports = f.readlines()

def toint(x):
	try:
		return int(x)
	except:
		pass
reports = [toint(r.strip()) for r in reports]
reports = [r for r in reports if r]

print(len(
    [
    v for v in range(len(reports)-1)
    if reports[0+v] < reports[1+v]
    ]
    ))
