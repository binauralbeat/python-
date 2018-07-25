class Loot_bag():

    def __init__(self, name):
            self.name = name
            self.loot = []    # creates a new empty list for each kid

    def add_loot(self, loot):
        self.loot.append(loot)

    def list_loot(self, name):
        return ["dog"]

    def remove_loot(self, loot):
        self.loot.remove(loot)
        return ('no loot')

kid_1 = Loot_bag('Mary')
kid_1.add_loot('dog')
kid_1.remove_loot('dog')
print(kid_1.loot)

# kid_1 = Loot_bag("Jerry", "wizard")

# print(kid_1)

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





