my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}
sister = my_family.get("sister")
sister_age = sister.get("age")
sister_name = sister.get("name")


print ((sister_name) + " is my sister and is " + str(sister_age) + " years old")