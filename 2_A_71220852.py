
a=input("Masukkan kata :")

b=int(len(a))

def cetak_kata(a):
    if b%2==0:
        a11=a[0:2+1]
        a12=a[-3:]
        print("Huruf yang diambil pada kata",a,"adalah",a11,"dan",a12)

    else:
        bagian=int((b-3)/2)
        a1=a[bagian:-bagian]
        print("Huruf yang diambil pada kata",a,"adalah",a1)
        
    
cetak_kata(a)

    
