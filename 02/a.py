with open("input") as f:
    commands = f.readlines()

dirs = {
"forward": (lambda h, d, v: (h+v, d  )),
"down":    (lambda h, d, v: (h,   d+v)),
"up":      (lambda h, d, v: (h,   d-v)),
}

commands = [r.strip() for r in commands]
h, d = 0, 0
for cmd in commands:
    if not cmd:
      continue
    cmd, v = cmd.split()
    v = int(v)
    h, d = dirs[cmd](h, d, v)
distance = h * d

print(distance)
