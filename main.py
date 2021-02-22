def doubleLast(x):
   
    x.append(x[len(x)-1])
    return x


print(doubleLast(["cat", "dog", "pig", "bear", "bear"]))    