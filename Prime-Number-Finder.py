#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Asal Sayı Bulucu")
        
        grid = QGridLayout()

        grid.addWidget(QLabel("Sayı Giriniz:"),1,0)
        
        self.sayi = QLineEdit()
        grid.addWidget(self.sayi,1,1,1,2)
        
        self.buton = QPushButton("Bul")
        grid.addWidget(self.buton,2,1,1,2)
        self.buton.clicked.connect(self.hesapla)
        
        self.yazi = QLabel("")
        grid.addWidget(self.yazi,4,1)
        
        self.setLayout(grid)
        self.resize(300,100)
        self.show()
        
    def hesapla(self):
        sayi = 0
        try:
            sayi = int(self.sayi.text())
        except:
            pass
        
        if(sayi == 0):
            self.yazi.setText(str(sayi) + " sayısı asal değildir.")
        elif(sayi != 0 and sayi > 0):
            sayac = 0
            for i in range(2,sayi):
                if(sayi % i == 0):
                    sayac += 1
            
            if(sayac == 0):
                self.yazi.setText(str(sayi) + " sayısı asaldır.")
            else:
                self.yazi.setText(str(sayi) + " sayısı asal değildir.")
        elif(sayi < 0):
            self.yazi.setText("Pozitif bir sayı giriniz.")
        else:
            self.yazi.setText("Bir sayı giriniz.")
            
            
uygulama = QApplication(sys.argv)
pencere = pencere()
sys.exit(uygulama.exec_())

# In[ ]:




