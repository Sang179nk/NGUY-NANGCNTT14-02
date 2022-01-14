full_name = input(" Nhập tên đầy đủ:  ")
print(full_name)

def isThuanNghich(n):
    str1 = str(n);  # ep kieu so n thanh chuoi
    str2 = str1[::-1];  # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;

array_of_name = full_name.split()

str_n = ""
for name in array_of_name:
   str_n += str(len(name))

print("n = ", str_n)
if isThuanNghich(int(str_n)):
    print("n la so thuan nghich")
else:
    print("n khong la so thuan nghich")
