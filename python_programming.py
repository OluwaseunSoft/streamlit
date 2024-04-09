# While and Continue

x = 12
while x < 100:
    x = x + 1
    if x % 13 != 0:
        continue
    #print(x)

# While and Continue
# while True:
#     guess = int(input('Enter a lucky number: '))
#     if guess == 7:
#         print('Winner!!!')
#         break
#     print(f'{guess} was not the lucky number')

#List slicing
# print('#' * 10 + ' LIST SLICING' + '#' * 10)
# numbers = [1, 2, 3, 4, 5]
# nums = numbers[1:4]
# numbers[0:2] = ['x', 'y', 'z']
# print(f'nums: {numbers}')
# print(nums[::-1])
# print('#' * 10 + ' LIST ITERATION' + '#' * 10)
# for x in nums:
#     print(f'{x}')

#List Comprehension
clicks = [10, 6, 4, 5]
doubled_list = list()
for c in clicks:
    doubled_list.append(c * 2)
print(doubled_list)

doubled_numbers = [c * 2 for c in clicks]
print(doubled_numbers)

name = 'Andrei'
l1 = [char for char in name]
print(l1)