import itertools

def generator(min=1, max=3):
    for num in itertools.count(min):
        if num == max + 1:
            break
        yield num

for num in generator():
    print(num)

def generator_2():
    for sign in itertools.cycle('ABC'):
        yield sign


signs_list = []
for sign in generator_2():
    if len(signs_list) == 9:
        break
    signs_list.append(sign)
print(signs_list)


hello_list = []
for element in itertools.repeat('Hello There!', 3):
    hello_list.append(element)
print(hello_list)


combi_list = []
for combi in itertools.combinations('ABC', 2):
    combi_list.append(combi)
print(combi_list)