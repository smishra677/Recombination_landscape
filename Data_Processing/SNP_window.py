import numpy as np
import pandas as pd
from collections import Counter


r= open('..\ReLERNN-master\examples\example.pool')
li = r.read().split('\n')
li1=[]
print(1)
for i in li:
    li1+=[i.split('\t')]

df1= pd.DataFrame(li1,columns=['Genome','Position','Frequency'])
print(df1)
#val = df1.groupby([df1['Position'](50), 'Frequency']).count()
#print(val)

def Count_SNP(window,df1):
    lis2=[]
    for i in df1['Position']:
        if i!=None:
            lis2.append(np.floor(int(i)/window))

    frequ = dict(Counter(lis2))
    return frequ

print(Count_SNP(50,df1)[0])
