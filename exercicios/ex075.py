num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:'))
num3 = int(input('Digite um numero:'))
num4 = int(input('Digite um numero:'))
n = int(0)

nums = (num1,num2,num3,num4)

for num in nums:
    print(num)
    if(num % 2 == 0):
        n += 1

print(nums.count(9))
print(nums.index(3) + 1)

#print(nums.index(%2 ==0))

print(n)