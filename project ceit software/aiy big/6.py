def is_triangle(a, b, c):
    return new_func(a, b, c)

def new_func(a, b, c):
    return a + b > c

filename = "input.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

values = [tuple(map(int, line.split())) for line in lines]

count = 0
discount = 0
for triangle in values:
    a, b, c = triangle
    if is_triangle(a, b, c):
        count += 1
        # print(f'Triangle with sides {a}, {b}, {c} is valid.')
    else:
        discount += 1
        # print(f'Triangle with sides {a}, {b}, {c} is not valid.')

print(f"can be {count}")
print(f"can not be {discount}")