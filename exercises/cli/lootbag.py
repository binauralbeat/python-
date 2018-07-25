class Loot_bag():



    def add_loot(self, name, loot):
        result = f'{name} gets a {loot}'
        return result
    def list_loot(self, name):
        return ["dog"]


kid_1 = Loot_bag("Jerry", "wizard")

print(kid_1)

# def add_loot(name, loot):
#     for i in loot_bag:
#         if i == name:
#             print ('error')
#             return
#     loot_bag[name] = loot

# def remove_loot(name, loot):
#     for i in loot_bag:
#         if i == name:
#             print ('error')
#             return
#     loot_bag[name] = clear()

# add_loot("james","wasps")
# add_loot("Tommy","rocks")

# remove_loot("Tommy","rocks")





