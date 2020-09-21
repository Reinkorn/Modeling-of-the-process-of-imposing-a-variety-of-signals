# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
import numpy as np
import math
Ac=[]
As=[]
Ua=[]
tp=0.001
def cos():
    res=[]#garmonica
    for k in np.arange(0,10):
        z = [(math.cos(x)+1) for x in np.arange(-(math.pi)*2,(math.pi)*2,(math.pi)*10*tp)]
        res+=z
        res=res[0:1999]
    return res
def f():
    res=[]#амплитуда навзявания пилы
    for i in range(0,10):
        z = [float(x) for x in np.arange(0,1,0.005)]
        res+=z
    res=res[0:1999]
    return res
def f1(tp):
    res=[]#pila
    for k in np.arange(0,6000*tp):
    	z = [float(x) for x in np.arange(0,1,tp)]
    	res+=z
    res=res[0:1999]
    return res 
def f2():
    faza=[]#faza навязывания
    for i in range(0,1999,1):
        faza.append(random.random()*2*math.pi)
    return faza
def f3():
    res=[]#Считываем случайную амплитуду пришедшую зонирующую
    massiv=[]
    massiv = np.loadtxt("amplitude.dat", delimiter='\t', dtype=np.float)
    for i in np.arange(1,156001,26):
        res.append(massiv[i])
    m=(res/max(res))
    m=m[0:1999:1]
    return m
def f4():
    res=[]#Считываем случайную фазу пришедшую фаза зондирующая
    massiv=[]
    i=1
    massiv = np.loadtxt("ksi.txt", delimiter='\t', dtype=np.float)
    for i in np.arange(1,156001,26):
        res.append(((massiv[i])*2*math.pi/360)+(math.pi/2))
    m=res
    m=m[0:1999:1]
    return m 
def f5():
    res=[]#Считываем случайную фазу пришедшую фаза зондирующая
    massiv=[]
    i=1
    massiv = np.loadtxt("ksi.txt", delimiter='\t', dtype=np.float)
    for i in np.arange(1,156001,26):
        res.append((massiv[i])*2*math.pi/360)
    m=res
    m=m[0:1999:1]
    return m 
def reley():
    #навязывание Релея!
    res=[]
    massiv=[]
    massiv = np.loadtxt("amplitude2a.dat", delimiter='\t', dtype=np.float)
    for i in np.arange(1,156001,26):
        res.append(massiv[i])
    m=((res/max(res))*3.8)
    m=m[0:1999:1]
    return m
#*************************************
datUe=reley()
datfie=f4()
datU=f3()
datfi=f5()
#*************************************
def P():
#Cчитаем мощьности
    a=0
    b=0
    for i in range(0,1999,1):
        a+=(datUe[i]**2)
    a=a/1999
    for i in range(0,1999,1):
        b+=(datU[i]**2)
    b=b/1999
    return (f" Мощность навязываемого сигнала:{a}\n Мощность зондидующего сигнала:{b}\n Отношение Pe/Ps:{a/b}\n Отношение в Децебелах:{10*(math.log10(a/b))} dB ")
#plt.plot(datfie)
for i in range(0,1999,1):
    Ac.append((datU[i]*(math.cos(datfi[i])))+(datUe[i]*(math.cos(datfie[i]))))
    As.append((datU[i]*(math.sin(datfi[i])))+(datUe[i]*(math.sin(datfie[i]))))
for i in range(0,1999,1):
    Ua.append(math.sqrt(((Ac[i])**2)+((As[i])**2)))
def pirson():
    result=np.corrcoef(Ua,datUe)
    coef=result[0][1]
    return coef
print(f"{P()}\n Коэффициент Корреляции:{pirson()}")
plt.rcParams['figure.figsize'] = (14,8)    
fig, (q1)=plt.subplots(1,1)
fig.subplots_adjust(hspace=0.4)

#fig.suptitle('Data')

q1.plot(Ua,color='black')
plt.rcParams.update({'font.size': 21})
q1.set_ylabel('Уровень сигнала')
q1.set_xlabel('Отсчёты')
q1.grid(True)

