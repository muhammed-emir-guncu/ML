"""lsls"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
veri_x=[i for i in range(1,200)]
veri_y=[i*2+5+np.random.normal(0,50) for i in veri_x]


def kayip_fonk(m,b,p_x:list,p_y:list):
    """kayıp"""
    toplam_hata=0
    assert len(p_x)==len(p_y)
    n=len(p_x)
    for i in range(n):
        x=p_x[i]
        y=p_y[i]
        toplam_hata += (y - (m * x + b))**2
    return toplam_hata/float(n)

def gradyan(m,b,p_x,p_y,l):
    """grafyan"""
    assert len(p_x)==len(p_y)
    m_g=0
    b_g=0
    n=len(p_x)
    for i in range(n):
        x=p_x[i]
        y=p_y[i]
        m_g += -(2/n) * x *(y-(m * x + b))
        b_g += -(2/n) * (y-(m * x + b))
    m = m - m_g * l
    b = b - b_g * l
    return m, b
M=0
B=0
L=0.001
EPOCH=100
for i in range(EPOCH):
    print(i)
    M, B=gradyan(M,B,veri_x,veri_y,L)
print(M,B)
plt.scatter(veri_x,veri_y)
plt.plot(list(range(0,200)),[M*i+B for i in range(0,200)])
plt.show()
