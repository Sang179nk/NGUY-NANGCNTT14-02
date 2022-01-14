def show(tendem):

    print("Ten dem:", tendem)

tendem = str(input())
show(tendem)
ten = "sang"

number = len(tendem) + len(ten)
sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print("n: ", number, "tong cac chu so cua n la: ", sum_of_digits )




