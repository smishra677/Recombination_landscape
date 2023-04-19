import numpy as np
import pandas as pd
from collections import Counter
import os

r= open('/home/gbob/Desktop/Recombination_landscape/ReLERNN-master/examples/example.pool')

li = r.read().split('\n')
li1=[]
print(1)
for i in li:
    li1+=[i.split('\t')[:2]]

df1= pd.DataFrame(li1,columns=['Genome','Position'])

#val = df1.groupby([df1['Position'](50), 'Frequency']).count()
#print(val)

def Count_SNP(window,df1):
    lis2=[]
    for i in df1['Position']:
        if i!=None:
            lis2.append(np.floor(int(i)/window))
            
 
    frequ = dict(Counter(lis2))
    return frequ

#details =Count_SNP(150000,df1)
#print(details)

np.savetxt(r'/home/gbob/Desktop/Recombination_landscape/ReLERNN-master/examples/example1.pool', df1.values, fmt='%s %s')
'''
with open("/home/gbob/Desktop/Recombination_landscape/ReLERNN-master/examples/example1.pool", 'w') as f: 
    for key, value in details.items(): 
        f.write('%s:%s\n' % (key, value))
'''