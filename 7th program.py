result = 0
for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num
print('sum is: ', result)
