uns = 2149583361

def toBin(n):
    b = ""
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

def unsToIp(un):
    un = int(toBin(un))
    ip = []
    while un > 0:
        ip.append(int(str(un % 10**8), base = 2))
        un //= 10**8
    return ".".join(str(x) for x in reversed(ip))

print(unsToIp(uns))