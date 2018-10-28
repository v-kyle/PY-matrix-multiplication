
def umn_mat (q,p):
    qn=len(q)
    qm=len(q[0])
    pn=len(p)
    pm=len(p[0])
    tmp=[]
    itog=[]
    w=[[0 for j in range(pm)] for i in range(qn)]
    if qm==pn:
        for i in range(qn):
            for j in range(pm):
                for k in range (qm):
                    w[i][j]+=q[i][k]*p[k][j]
    else: w = 'NO'
    return w
                
            



an=int(input('Кол-во строк первой матрицы '))
am=int(input('Кол-во столбцов первой матрицы '))
bn=int(input('Кол-во строк второй матрицы '))
bm=int(input('Кол-во столбцов второй матрицы '))

a=[[0 for j in range(am)] for i in range(an)]
b=[[0 for j in range(bm)] for i in range(bn)]

for i in range(an):
    for j in range(am):
        a[i][j]=int(input('Введите [%d][%d]ый элемент '%(i,j)))

for i in range(bn):
    for j in range(bm):
        b[i][j]=int(input('Введите [%d][%d]ый элемент '%(i,j)))

c=umn_mat(a,b)







