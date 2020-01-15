import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd

file1 = pd.read_csv('dane1.csv')
data1 = file1[['Wojewodztwo', 'Bezrobotni']]
file2 = pd.read_csv('dane2.csv')
data2 = file2[['RokKwartal', 'Cena']]


fig = plt.figure(figsize=(40, 20))
greedSpace = gridspec.GridSpec(nrows=4, ncols=1, height_ratios=[1, 3, 1, 1], hspace=0.3)

ax0 = fig.add_subplot(greedSpace[0, 0])
ax0.bar(data1.Wojewodztwo, height=data1.Bezrobotni)
ax0.set_title('Liczba osób bezrobotnych dla danego wojewodztwa(w tysiacach)')
ax0.legend(['Liczba ludności'])
ax0.set_ylabel('Liczba osób', fontsize=15)
ax0.set_xlabel('Nazwa województwa', fontsize=15)

ax1 = fig.add_subplot(greedSpace[1, 0])
ax1.pie(data1.Bezrobotni, explode=None, labels=data1.Wojewodztwo, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.legend(data1.Wojewodztwo)
ax1.set_title('Procent bezrobocia w Polsce')

ax2 = fig.add_subplot(greedSpace[2, 0])
ax2.plot(data2.RokKwartal, data2.Cena, color='green')
ax2.legend(['Cena'])
ax2.set_title('Cena 1m2 powierzchni uzytkowej budynku mieszkalnego w latach 2013-2019')
ax2.set_xlabel('Rok-Kwartał')
ax2.set_ylabel('Cena')
ax2.grid()

ax3 = fig.add_subplot(greedSpace[3, 0])
ax3.scatter(data2.RokKwartal, data2.Cena, color='red')
ax3.legend(['Cena'])
ax3.set_title('Cena 1m2 powierzchni uzytkowej budynku mieszkalnego w latach 2013-2019')
ax3.set_xlabel('Rok-Kwartał')
ax3.set_ylabel('Cena')

fig.set_tight_layout(False)
plt.show()
