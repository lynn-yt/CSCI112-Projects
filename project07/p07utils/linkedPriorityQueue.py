"""
File: linkedPriorityQueue.py
Authors: Sam Bluestone and Zahin Reaz
"""
from .linkedQueue import LinkedQueue
from .node import Node

class LinkedPriorityQueue(LinkedQueue):

    def __init__(self, sourceCollection = None):
        """Constructor for the LinkedPriorityQueue class """

        super().__init__(sourceCollection)

    def add(self, item):
        """Adds an item to the queue in the correct location
            and overrides the parent class's add() method"""
        newNode = Node(item)
        if self.isEmpty() or item >= self._rear.data:
            super().add(item)

        elif item < self.peek():
            newNode.next = self._front
            self._front = newNode
            
        else:
            probe = self._front
            
            while probe.next.data <= item:
                probe = probe.next

            newNode.next = probe.next
            probe.next = newNode

        super().incModCount()
        self._modCount = super().getModCount()
        self._size += 1
