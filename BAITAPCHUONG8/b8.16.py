# tính bội chung nhỏ nhất của 2 số nhập vào
a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
c = a*b
for i in range(b,c+1):
    if i%a == 0 and i%b==0:
        d = i
        break
print(i)