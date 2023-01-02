j = []
v = 0
c = int(input("nhập số lượng con thú: "))
for i in range(1,c+1):
    print("nhập con thú thứ: ",i)
    a = input()
    j.append(a)
print(j)
print("số lượng thú là: ",c)
b = input("Nhập con thú cần tìm: ")
for i in j:
    if b == i:
        v = v+1
if v==0:
    print("con thú bạn tìm không có, bạn thật đen đủi")
else:
    print("con thú bạn tìm có ",v,"con")