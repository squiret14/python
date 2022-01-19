def  Cubed(n):
    total=n * n * n
    return total

def CubedPlusSquared(n):
    total=n * n + Cubed(n)
    return total

#main program
answer=CubedPlusSquared(3)
print(answer)

