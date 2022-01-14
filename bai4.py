import re
#nhập vào giá trị
values=input("Nhập vào chuỗi: ")

temp = re.compile("([a-zA-Z]+)([0-9]+)")

str_temp = temp.match(values).groups()

print("Tuple sau khi phan tach la: ", str_temp)

array_temp = re.findall(r'[A-Za-z]+|\d+', values)

print("Danh sach sau khi phan tach: ", array_temp)




