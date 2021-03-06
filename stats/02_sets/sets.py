
# # list/set trick doesn't maintain order
# s1 = list(set([7,8,9,0,1,2,3,4,7,8,9,0]))
# s2 = list(set([7,8,9,0,2,3]))

s1 = [7,8,9,0,1,2,3,4,7,8,9,0]
s2 = [7,8,9,0,2,3]

def dedupe(lst):
    deduped_inorder = []
    for element in lst:
        if element not in deduped_inorder:
            deduped_inorder.append(element)
    return deduped_inorder

# print(dedupe(s1))
# print(dedupe(s2))


''' star arguments: *args'''
def star_args(*args):
    for item in args:
        print(item)
    return None

# star_args('hey', 5, int, [1,2,3,4,5])


''' Simple Union function for lists using "sets" '''
list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def union(set1, set2):
    set_union = []
    for item in set1:
        set_union.append(item)
    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))

def union_mult_sets(*args):
    set_union = []

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

# print(union_mult_sets(list1, list2, list3))


''' Slide 8 Breakout '''

four_sided_die = [1,2,3,4]
coin_flip = ['H', 'T']

samp_space = []

for roll in four_sided_die:
    for flip1 in coin_flip:
        for flip2 in coin_flip:
            samp_space.append([roll, flip1, flip2])

# for outcome in samp_space:
#     print(outcome)

A = [] # die roll shows exactly one pip
for outcome in samp_space:
    if outcome[0] == 1:
        A.append(outcome)

# print(A)

B = [] # at least one coin flip results in heads
for outcome in samp_space:
    if outcome.count('H') >= 1:
        B.append(outcome)

# print(B)

# print(union(A, B))


''' Intersection '''
def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)
    return set_intersect

# print(intersection(list1, list2))

def intersection_mult(*args):
    set_intersect = []

    if len(args) > 0:
        for item in args[0]:
            flag = True
            for set_ in args:
                if item not in set_:
                    flag = False
            if flag == True:
                set_intersect.append(item)

        return set_intersect
    else:
        return set_intersect

# print(intersection_mult())
# print(intersection_mult(list1, list2, list3))


''' Complement Function '''
sample_space = union_mult_sets(list1, list2, list3)

def complement(samp_space, set_):
    comp = []

    for item in samp_space:
        if item not in set_:
            comp.append(item)
    return comp

# print(complement(sample_space, list3))


''' Breakout Slide 13 '''
coin_flips = ['H', 'T']

sample_space = []

for flip1 in coin_flips:
    for flip2 in coin_flips:
        for flip3 in coin_flips:
            for flip4 in coin_flips:
                sample_space.append([flip1, flip2, flip3, flip4])

# for samp in sample_space:
#     print(samp)

A, B, C = [], [], []

for outcome in sample_space:
    if outcome.count('H') >= 3:
        A.append(outcome)
    if outcome.count('T') <= 2:
        B.append(outcome)
    if outcome.count('H') == 4 or outcome.count('T') == 4:
        C.append(outcome)

# print('A')
# for outcome in A:
#     print(outcome)

# print()
# print('B')
# for outcome in B:
#     print(outcome)

# print()
# print('C')
# for outcome in C:
#     print(outcome)

# for outcome in intersection(A, complement(sample_space, C)):
#     print(outcome)

# for outcome in complement(sample_space, intersection(A, C)):
#     print(outcome)


''' Set Difference '''
def difference(set1, set2):
    set_diff = []
    for item in set1:
        if item not in set2:
            set_diff.append(item)
    return set_diff

# print(difference(list1, list2))
# print(difference(list2, list1))


''' breakout slide 17 '''
# sample_space = []

# for roll1 in range(1, 6+1):
#     for roll2 in range(1, 6+1):
#         sample_space.append([roll1, roll2])

# for outcome in sample_space:
#     print(outcome)

# A, B = [], []

# for outcome in sample_space:
#     if sum(outcome) >= 10:
#         A.append(outcome)
#     if sum(outcome) % 2 == 0:
#         B.append(outcome)
# print('A')
# for outcome in A:
#     print(outcome)
# print()
# print('B')
# for outcome in B:
#     print(outcome)

# print(difference(A, B))
# print(difference(B, A))