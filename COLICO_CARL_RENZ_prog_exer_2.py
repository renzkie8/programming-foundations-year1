x = int(input('Enter a number for x: '))
y = int(input('Enter a number for y: '))
x,y = y,x
is_even_x = x % 3 == 0
is_odd_y = y % 3 == 1
z = x + y
left_shifted_z = z << 2
logical_result = x >y & y < 10
remainder = z % 7
print(f'x: {x}')
print(f'y: {y}')
print(f'even: {is_even_x}')
print(f'odd: {is_odd_y}')
print(f'z: {z}')
print(f'left_shifted_z: {left_shifted_z}')
print(f'logical_result: {logical_result}')
print(f'remainder: {remainder}')
