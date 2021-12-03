with open("input") as f:
    commands = f.readlines()

dirs = {
"forward": (lambda h, d, a, v: (h+v, d+a*v  , a   )),
"down":    (lambda h, d, a, v: (h  , d      , a+v )),
"up":      (lambda h, d, a, v: (h  , d      , a-v )),
}

commands = [r.strip() for r in commands]
h, d, a = 0, 0, 0
for cmd in commands:
    if not cmd:
      continue
    cmd, v = cmd.split()
    v = int(v)
    h, d, a = dirs[cmd](h, d, a, v)
distance = h * d

print(distance)
