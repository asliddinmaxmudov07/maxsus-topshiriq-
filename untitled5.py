# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L4TAiv66HWb-i04T0DWDvmimoFioY-Fi
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,21,9, 2,5, 8,  9, 7,5,7,9,8,2, 6, ])
y = np.array([1,9,13,21,9, 2,5, 8, 9, 6, 8 ,4, 9,2,6,3,9])
plt.scatter(x,y)
plt.show()

# Sinus funksiyasining grafigini chizish uchun kerakli kutubxonalarni import qilamiz
import numpy as np
import matplotlib.pyplot as plt

# Sinus funksiyasining x qiymatlarini belgilaymiz
x = np.linspace(0, 10, 100)  # 0 dan 10 gacha bo'lgan 100 ta nuqta
y = np.sin(x)  # sinus funksiyasining qiymatlari

# Grafikni chizamiz
plt.figure(figsize=(8, 5))  # grafik o'lchami
plt.plot(x, y, label="Sinus(x)", color="blue")  # sinus grafigi
plt.title("Sinus Funksiyasining Grafikasi")  # sarlavha
plt.xlabel("X qiymatlari")  # x o'qi nomi
plt.ylabel("Y qiymatlari")  # y o'qi nomi
plt.grid(True)  # tarmoq chizmalari
plt.legend()  # legendani ko'rsatish
plt.show()  # grafikni ko'rsatish

