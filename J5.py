speed = 0
qType = int(input())
n = int(input())
d = list(input().replace(" ", ""))
p = list(input().replace(" ", ""))
d = [int(di) for di in d]
p = [int(pi) for pi in p]

if qType == 1:
    for k in range(n):
        speed += max(max(p),max(d))
        p.remove(max(p))
        d.remove(max(d))
    print(speed)

elif qType == 2:
    for k in range(n):
        speed += max(max(p),min(d))
        p.remove(max(p))
        d.remove(min(d))
    print(speed)