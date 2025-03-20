a = [int(input(" => ")) for i in range(int(input(" n = ")))]
k = s = 0
for i in list(range(len(a))):
    if a[i] != 0:
        k += 1
        s += a[i]
print(k, s, " среднее ариф ", s / k, )






