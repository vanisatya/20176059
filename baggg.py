from collections import Counter
import os
files=[]
matrix=[]
for file in os.listdir('.'):
   
    if (os.path.isfile(file)) and(file.endswith(".txt")):
        print(file)
        files.append(file)
print(files)


for i in range (len(files)):
    l=[]
    with open(files[i],'r') as f:
        for line in(f):
            for word in line.split():
                l.append(word.lower())
            
    d=dict(Counter(l))
    print(d)

    o=[]
    for j in range(len(files)):
        p=[]
        with open(files[j],'r') as f1:
            for line in(f1):
                for word in line.split():
                    p.append(word.lower())
        d1=dict(Counter(p))
        print(d1)
        s=0
        s1=0
        s2=0
        h=[]
        for k in d.keys():
            if k in d1.keys():
                h.append(k)
        print(h)
        x=[]
        for i in h:
            if i in d:
                x.append(d[i])
        print(x)
        y=[]
        for i in h:
            if i in d1:
                y.append(d1[i])
        print(y)
        z=[a*b for a,b in zip(x,y)]
        print(z)
        for i in z:
            s2=s2+i
        print(s2)

        for k,v in d.items():
            s=s+(v**2)
            n=(s)**(1/2)
        print(s)
        print(n)

        for k1,v1 in d1.items():
            s1=s1+(v1**2)
            n1=(s1)**(1/2)
        print(n1)

        r=(s2)/(abs(n)*abs(n1))
        print(r)
        #dis=math.acos(dis)
        #print(dis)
        result=r*100
        print(result)
        o.append(result)
    matrix.append(o)
print(matrix)
