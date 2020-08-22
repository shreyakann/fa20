from random import randint, choice
staff = [
    'Michael',
    'Gerald',
    'Alex',
    'Brian',
    'Julia',
    'Sophia',
    'Shreya',
    'Vandana',
    'Cameron',
    'Nick'
]
get_staff = lambda: choice(staff)
get_cone = lambda: randint(1, 6)
get_month = lambda: randint(1, 12)

values_list = ",\n".join([ '(\'{}\', {}, {}, {})'.format(get_staff(), tid, get_cone(), get_month()) for tid in range(500) ])

sql_statement = 'INSERT INTO sales (Cashier, TID, Cone, Month) VALUES {};'.format(values_list)

print(sql_statement)