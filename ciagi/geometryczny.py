def geo_ogolny(a1,q,n):
    an=a1*q**n-1
    return an

def geo_suma(a1,q,n):
    sn=a1*((1-q**n)/(1-q))
    return sn
