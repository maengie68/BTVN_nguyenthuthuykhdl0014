#bai tap 8.4 :: Tinh dien tich tam giac ABC voi a,b,c nhap tu ban phim
# theo cong thuc heron
import math #goi thu vien match chua cac ham so toan hoc
print("Nhap so do cac canh cua tam giac:")
a = eval(input('a ='))
b = eval(input('b ='))
c = eval(input('c ='))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Dien tich tam giac la: ", s)