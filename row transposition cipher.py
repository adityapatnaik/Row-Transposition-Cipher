
#Aditya Patnaik
#Row Transposition Cipher


from collections import defaultdict
import operator

kei=list(input())
text =list(input())
text.append('\0')
k = defaultdict(list)
n = len(text)

i = 0
for j in range(len(kei)):
    for i in range(j,n,len(kei)):
        if(text[i]=='\x00'): break
        k[kei[j]].append(text[i])    

li = []
li = sorted(k.values())
for i in li:
   m = []
   m=i
   for j in m:
      print(j,end='')
