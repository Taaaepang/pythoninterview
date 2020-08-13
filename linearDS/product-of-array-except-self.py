num = [1, 2, 3, 4]
p = 1
out = []

for i in range(len(num)):
    out.append(p)
    p *= num[i]

p = 1
for i in range(len(num)-1, -1, -1 ):
    out[i] = p * out[i]
    p *= num[i]

print(out)

