from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):

    def __init__(self, sourceCollection = None):
        """Constructor for the ArrayPriorityQueue class """
        super().__init__(sourceCollection)


    def add(self, item):
        """Adds an item in to the queue at the correct position,
            and overrides the parent class's add() method"""
        if len(self._items) == self._size:
            self.grow()

        if len(self) == 0 or self._items[self._rear] <= item:
            super().add(item)
               
        elif self._items[self._front] > item:
            self._front -= 1
            self._front %= len(self._items)
            self._items[self._front] = item
            self._size += 1

        else:
            cursor = 0
            while cursor < len(self):
                if self._items[(cursor + self._front + 1) % len(self._items)] > item:
                    cursor += 1
                    break
                else:
                    cursor += 1


            for x in range(len(self), cursor, -1):
                self._items[(x + self._front) % len(self._items)] = self._items[((x + self._front) % len(self._items)) - 1]
            self._items[cursor] = item
            self._size += 1
            self._rear +=  1
            self._rear %= len(self._items)

                
            
               




        

        

        
