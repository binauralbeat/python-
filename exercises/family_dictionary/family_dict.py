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

# print (my_family["sister"])
print (sister_age)