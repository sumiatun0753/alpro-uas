dict1={100:10,50:10,20:10,10:10,5:10,2:10,1:10}
print('Pembayaran barang')
print('jumlah uang yang dibayarkan :')
uang=0
list1=[100,50,20,10,5,2,1]
for i in range(len(list1)):
    x=int(input('jumlah uang-%i:' %list1[i]))
    if list1[i]==100 or 50 or 20 or 10 or 5 or 2 or 1 and x!=0:
        dict1[list1[i]]+=x
        uang+=(list1[i]*x)
d1=dict1[100]
d2=dict1[50]
d3=dict1[20]
d4=dict1[10]
d5=dict1[5]
d6=dict1[2]
d7=dict1[1]
hb=int(input('harga barang ='))
kembalian=uang-hb
print('total uang kembalian',kembalian)
print('uang kembalian untuk pelanggan :')
while kembalian !=0:
    if kembalian >=100 :
        kembalian-=100
        dict1[100]-=1
    elif kembalian >=50 and kembalian<100 :
        kembalian-=50
        dict1[50]-=1
    elif kembalian >=20 and kembalian<50:
        kembalian-=20
        dict1[20]-=1
    elif kembalian >=10 and kembalian<20 :
        kembalian-=10
        dict1[10]-=1
    elif kembalian >=5 and kembalian<10 :
        kembalian-=5
        dict1[5]-=1
    elif kembalian >=2 and kembalian<5 :
        kembalian-=2
        dict1[2]-=1
    elif kembalian >=1 and kembalian<2 :
        kembalian-=1
        dict1[1]-=1
        
if d1!=dict1[100]:
    z=d1-dict1[100]
    print('uang 100 k = ',z,'buah')
if d2!=dict1[50]:
    a=d2-dict1[50]
    print('uang 50 k = ',a,'buah')
if d3!=dict1[20]:
    b=d3-dict1[20]
    print('uang 20 k = ',b,'buah')
if d4!=dict1[10]:
    c=d4-dict1[10]
    print('uang 10 k = ',c,'buah')
if d5!=dict1[5]:
    d=d5-dict1[5]
    print('uang 5 k = ',d,'buah')
if d6!=dict1[2]:
    e=d6-dict1[2]
    print('uang 2 k = ',e,'buah')
if d7!=dict1[1]:
    f=d7-dict1[1]
    print('uang 1 k = ',f,'buah')

print(dict1)
