import unittest
import sys
from lootbag import Loot_bag

class Loot_test(unittest.TestCase):



    def test_add_loot_exists(self):
        result = Loot_bag.add_loot(self,"tommy", "whistle")
        self.assertEqual(result, "tommy gets a whistle")

    def test_can_get_loot(self):
        result = 'dog'
        result_2 = Loot_bag.list_loot(self, "Rob")

        self.assertIn(result, result_2)

    def test_can_remove_loot(self):
        result = 'no loot'
        result_2 = Loot_bag.remove_loot(self, "Rob")






if __name__ == '__main__':
    unittest.main()








