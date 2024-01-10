import numpy as t 
iou= int(input('enter 1 for encryption ,2 for decryption')) 
n = input("Enter input to be encrypted/decrypted").replace(" ","").upper() 
k = input('key?').upper() 
if iou == 2: 
    k = int(len(n))//int(k) 
ncol = int(k) 
nlen = int(len(n))    
#k==ncol for this case warna int(len(k)) 
extrachar = nlen%ncol 
if iou == 1: 
    if extrachar!=0: 
        dmychr = ncol - extrachar 
        for i in range(dmychr): 
            n+="X" 
nlen = int(len(n)) 
nrow = int(nlen//ncol) 
nm =[[0]*ncol for i in range(nrow)] 
z = 0 
for i in range(nrow): 
    for j in range(ncol): 
        nm[i][j] = n[z] 
        z+=1 
print(nm) 
s = t.transpose(nm) 
print(s) 
m = "" 
x ="" 
for i in range(ncol): 
    for j in range(nrow): 
        m+=s[i][j] 
if iou == 1: 
     print(m) 
elif iou ==2: 
    for i in m: 
        if i =='X': 
            continue 
        else: 
            x+=i 
    print(x)
