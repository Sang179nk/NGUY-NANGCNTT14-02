def show(s):


    print("Ten:", s)

    print("So ky tu:", len(s))


s = str(input())
show(s)

d = dict()
for i in range(1, len(s) + 1):
    d[i] = i * i

print(d)