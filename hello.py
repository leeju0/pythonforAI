weight = int(input('Enter weight: '))
height = int(input('Enter height: '))

if weight >= 90 and height <= 150:
    print('fat!', 'exercise!')
elif weight >= 60 or 160 <= height <180:
    print('normal')
else:
    print('overweight')
