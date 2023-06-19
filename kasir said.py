def h(j,t) :
  global k
  k=[100000,50000,20000,10000,5000,2000,1000,500,200,100]
  #for x in open ("data.txt") :
    #k+=[x.split()]
  kembali=t-j
  print("kembalian", kembali)
  for y in range (9):
    s=0
    while kembali>=k[y]:
        kembali=kembali-k[y]
        s+=1
        #if kembali<k[y]: 
        if s>0:
              if kembali<k[y]:
                print (k[y],"sebanyak",s,"buah")
        else :
            print('selesai')
a=int(input("masukan harga= " ))
b=int(input("pembayaran = " ))
h(a,b)
