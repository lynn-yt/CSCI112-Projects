"""
File name: testList.py
Authors: Sam Bluestone and Zahin Reaz
"""
from arrayList import ArrayList
from linkedList import LinkedList
def testList(listType):

    print("Create a list with 1-9")
    lyst = listType(range(1, 10))
    print("Length:", len(lyst))
    print("Items: ", lyst)

    print("\nInserting 10 at position 3: ", end  = "")
    lyst.insert(3, 10)
    print(lyst)

    print("\nInsert 0 at position 0: ", end  = "")
    lyst.insert(0, 0)
    print(lyst)

    print("\nInsert 11 at the end of the list: ", end  = "")
    lyst.insert(len(lyst), 11)
    print(lyst)

    print("\nInserting 12 at an index > len(lyst): ", end = "")
    lyst.insert(len(lyst) + 1, 12)
    print(lyst)

    print("\nInserting -1 at an index < 0: ", end = "")
    lyst.insert(-1, -1)
    print(lyst)
    

    print("\nPopping at position 3: ", end  = "")
    lyst.pop(3)
    print(lyst)

    print("\nPopping at position 0: ", end  = "")
    lyst.pop(0)
    print(lyst)

    print("\nPopping at the end of the list: ", end  = "")
    lyst.pop()
    print(lyst)

    print("\nPopping at len(lyst) + 1, error expected:")
    try:
        lyst.pop(len(lyst) + 1)
    except:
        print("Success! Program crashed")

    print("\nPopping at -1, error expected:")
    try:
        lyst.pop(-1)
    except:
        print("Success! Program crashed")

    print("\nAppending 13 to the list: ", end = "")
    lyst.append(13)
    print(lyst)

    print("\nAdding 14 to the list (works the same as append): ", end = "")
    lyst.add(14)
    print(lyst)

    print("\nRemoving 9 from the list: ", end = "")
    lyst.remove(9)
    print(lyst)

    print("\nAttempt to remove 100 from the list, error expected:")
    try:
        lyst.remove(100)
        print(lyst)
    except:
        print("Success! program crashed")

    print("\nClearing list: ", end = "")
    lyst.clear()
    print(lyst)
    print("Length:", len(lyst))
    

    
    
def testListIterator(listType):
    print("Create a list with 1-9")
    lyst = listType(range(1, 10))
    print("Length:", len(lyst))
    print("Items (first to last): ", lyst)

    listIterator = lyst.listIterator()
    
    print("\nForward traversal: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        print(listIterator.next(), end = " ")

    print("\n\nBackward Traversal: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        print(listIterator.previous(), end = " ")

    print("\n\nInserting 10 before 3: ", end = "")
    listIterator.first()
    for count in range(3):
        listIterator.next()
    listIterator.insert(10)
    print(lyst)

    print("\nRemoving 2: ", end = "")
    listIterator.first()
    for count in range(2):
        listIterator.next()
    listIterator.remove()
    print(lyst)

    print("\nTry to insert and remove for one next, error expected:")
    try:
        listIterator.next()
        listIterator.remove()
        listIterator.remove()
    except:
        print("Success! Program crashed")

    print("\nGo next, then previous, then remove 10:")
    listIterator.next()
    listIterator.previous()
    listIterator.remove()
    print(lyst)

    
    print("\nRemoving all items")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()

    print("Length:", len(lyst))

    print("\nInsert 100 into original list (not using list iterator), then try to remove at pointer, error expected:")
    try:
        lyst.insert(len(lyst) - 1, 100)
        listIterator.next()
        listIterator.remove()
    except:
        print("Success! Program crashed")

    

if __name__ == "__main__":
    
    #testList(ArrayList)
    #testList(LinkedList)
    testListIterator(LinkedList)
    #testListIterator(ArrayList)
