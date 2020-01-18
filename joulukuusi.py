def joulukuusi(n):
    x=' '
    r='*'
    for i in range (1, n+1):
        p = n - i
        if i>1:
            i = i*2
        print(x*p, r*i)









joulukuusi(10)