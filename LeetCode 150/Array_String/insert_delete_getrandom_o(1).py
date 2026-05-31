# 380. Insert Delete GetRandom O(1) - medium
class RandomizedSet:
    '''
        A set is a data structure to store unique items
          - unordered, no duplicates, mutable
        A randomizedset is pretty much a set except you can get a random item from the set in O(1)
    '''
    def __init__(self):
        self.__values = []
        self.__positions = {}

    def insert(self, val: int) -> bool:
        if val not in self.__positions:
            self.__positions[val] = len(self.__values)
            self.__values.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        # If val doesn't exist, just return False
        if val not in self.__positions:
            return False
        
        '''
            We have to remove it from values array and positions hashmap
            So we probably need to move the item around in the values array 
              - To the end to use .pop() for O(1)
        '''

        last_element = self.__values[-1]

        # Put the last element to the position of the element to remove
        self.__values[self.__positions[val]] = last_element
        self.__positions[last_element] = self.__positions[val]

        # Just delete last value and element to delete position
        self.__values.pop()
        del self.__positions[val]

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.__values)-1)
        return self.__values[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()