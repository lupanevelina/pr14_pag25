x=[]
n=int(input("Introdu dimensiunea matricei: "))
if n>=2 and n<=10 :
    for rind in range(0,n):
        rind=[]
        for element in range(0,n):
            element=int(input("Introdu elementele matricei: "))
            rind.append(element)
        x.append(rind)
    print(x)
#diag princp
diag_princ=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i==j :
            diag_princ.append(x[i][j])
print("Suma pe diagonala principala=",sum(diag_princ))
#diag sec
diag_sec=[] 
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i+j==n-1:
            diag_sec.append(x[i][j])
            
print("Suma pe diagonala secundara=",sum(diag_sec)) 
#c
diag_princ2=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i<j :
            diag_princ2.append(x[i][j])
print("Suma elementelor mai sus de diagonala principala=",sum(diag_princ2))
#d
dp=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i>j :
            dp.append(x[i][j])
print("Suma elementelor mai jos de diagonala principala=",sum(dp))
#e
diag_sec2=[] 
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i+j<n-1:
            diag_sec2.append(x[i][j])
            
print("Suma elementelor mai sus de diagonala secundara=",sum(diag_sec2)) 
#f
ds=[] 
for i in range(len(x)):
    for j in range(len(x[0])) :
        if (i+j)>(n-1):
            ds.append(x[i][j])
            
print("Suma elementelor mai jos de diagonala secundara=",sum(ds))