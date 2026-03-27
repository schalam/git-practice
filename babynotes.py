import datetime

families = []

parent_name = input("what's your name? ")

while parent_name != 'no':
    kid_name = input('Whats your kids name? ')
    birthday = datetime(input("What's their birthday? "))
    current_family = {
            'parent_name': parent_name
            'children': [
                {
                'name': kid_name,
                'birthday': birthday
            }
            ]
    }
    families.append(child)
    more_kids = input('Do you have any more kids? ')

for child in families:
    print(f"{child['parent_name']})
    total = total + food['amount']    

if total <= 2200:
    remaining = 2200-total
    print(f'You have {remaining} calories left')
else:
        print('youre done for the day')