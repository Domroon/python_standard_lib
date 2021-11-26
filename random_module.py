import random
# import codecs

# while True:
#     try:
#         random_byte = random.randbytes(8)
#         print(random_byte)
#         random_utf_8 = codecs.decode(random_byte)
#     except UnicodeDecodeError:
#         continue
#     break

# print(random_utf_8)

print('\nrandint 0-100:')
print(random.randint(0, 100))

print('\ngetrandbits')
print(random.getrandbits(8))

print('\nrandom choice')

color_list = ['blue', 'yellow', 'green', 'orange']
print(random.choice(color_list))