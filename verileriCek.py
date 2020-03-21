import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as style

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

URL = 'https://www.kuveytturk.com.tr/finans-portali/'

f = open ("veriler.txt","a+")

plt.show()

for x in range(6):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    veriler = soup.find(class_='finans-portali')
    sinif = veriler.find_all('p')
    bankaSatis = sinif[6].prettify().split('\n')[1]
    bankaAlis = sinif[7].prettify().split('\n')[1]
    
    print (bankaSatis)
    print (bankaAlis)
    
    plt.scatter(x, bankaSatis)

    f.write(bankaSatis + "\n")
    f.write(bankaAlis + "\n")
    
    time.sleep(3)

f.close
