# Conditional Logic

# Simple IF, always indented
if 100 < 10:
    print('100 is greater than 10')

print('This line will always print because is not indented')

# Two conditionals using IF
value = 'green'

if value == 'green':
    print('Go')
if value == 'red':
    print('Stop')

# Two conditional with IF and ELSE
value = 'red'

if value == 'green':
    print('Go')
else:
    print('Stop')

# Three conditional with IF, ELIF and ELSE
value = 'yellow'

if value == 'green':
    print('Go')
elif value == 'yellow':
    print('Prepare to stop')
else:
    print('Stop')