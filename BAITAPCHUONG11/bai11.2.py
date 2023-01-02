teams = []
j = []
k = []
l = []
a = int(input("nhập số lượng đội 1: "))
for i in range(1,a+1):
    print("điền thông tin từng người: ")
    a1 = input()
    j.append(a1)
teams.append(j)
b = int(input("nhập số lượng thành viên đội 2: "))
for i in range(1,b+1):
    print("điền thông tin từng người: ")
    a1 = input()
    k.append(a1)
teams.append(k)
c = int(input("nhập số lượng thành viên đội 3: "))
for i in range(1,c+1):
    print("điền thông tin từng người: ")
    a1 = input()
    l.append(a1)
teams.append(l)
print(teams)
print("đội trưởng đội tệ nhất là: ",l[1])