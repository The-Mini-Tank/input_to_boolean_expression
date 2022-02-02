#!/usr/bin/env python
# coding: utf-8

# In[285]:


import string as str
import numpy as np

ipt = []
ins = 0;

alphabet = ['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters = []
sheet = []
biSheet = []

# Leitura do arquivo.txt, os valores são armazenados em uma lista unidimensional.

with open('input.txt', 'r') as f:
    for item in f:
        ipt.append(int(item))

# Definição das entradas em base 2.

def DefineIns():
    for i in range(32):
        if 2**i == len(ipt):
            return i
        elif i == len(ipt):
            print('Por Favor Insira um Valor Válido de Saída')
            return -1;

# Conversão númerica para alfabética, cada número representa uma letra do alfabeto, tendo início no 0.

def ConvertToAlphabet():
    for i in range(ins):
        letters.append(alphabet[i])
        
# Geração de uma lista unidimensional contendo os 0 e 1 por coluna, sendo separados pela letra correspondente.
        
def GenerateSheet():
    state = False
    switch = 2**ins/2
    ct = 0
    
    for i in range(ins):
        sheet.append(letters[i])
        ct = 0
        
        for x in range(2**ins):
            ct+=1   
            if state == False:
                sheet.append(0)
            elif state == True:
                sheet.append(1)
            
            if ct >= switch:
                state = not state
                ct = 0
                
        if switch != 1:
            switch = switch/2

# Conversão da lista bidimensional gerada acima para
    
def Convert1DTo2D(st, ip):
    return [st[i:i + ip] for i in range(0, len(st), ip)]

# Conversão para para expressão booleana utilizando uma lista bidimensinal utilizando a regra do mintermo.

def ConvertToExpression():
    out = ''
    for l in range(2**ins):
        for c in range(ins):
            if(ipt[l] == 1):
                if(biSheet[c][l+1] == 0):
                    out += letters[c] + "'" 
                elif(biSheet[c][l+1] == 1):
                    out += letters[c]
                if(c == ins-1 and l != 2**ins-1):
                    out += " + "
    print(out)

    
# Verificação de entradas na base 2, se o valor inserido não for correspondente o resto do código não roda.

ins = DefineIns()
if(ins != -1):
    ConvertToAlphabet()
    GenerateSheet()
    biSheet = Convert1DTo2D(sheet, 2**ins+1)
    ConvertToExpression()
    
    #Prints para Infos Adicionais
    
    #print(ipt)
    #print(biSheet)
    #print(ins)
    #print(letters)


# In[ ]:




