base_5 = [0,1,2,3,4,]
basic_counting = []
for num in base_5:
    for num2 in base_5:
        for num3 in base_5:
            for num4 in base_5:
                for num5 in base_5:
                    basic_counting.append([num,num2,num3,num4,num5,])

# for number in basic_counting:
#     print(number)

sample_space = []

for lst in basic_counting:
    valid_for_sample_space = True
    for number in lst:
        if lst.count(number) > 1:
            valid_for_sample_space = False
            break
    
    if valid_for_sample_space:
        sample_space.append(lst)

# for samp in sample_space:
#     print(samp)
# print('base 5: ',len(basic_counting))
# print('5 factorial: ',len(sample_space))


''' factorial '''
def factorial(num):
    prod = 1

    for i in range(1, num+1):
        prod *= i

    return prod

# print(factorial(52))

