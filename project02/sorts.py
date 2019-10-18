"""
Author: Sam Bluestone and Zahin Reaz
File: sorts.py

Defines the selection sort and the quick sort.
Also defines the insertion sort algorithim
"""
from counter import Counter
from tools import getRandomList

def selectionSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a selection sort."""
    
    n = len(lyst)
    for i in range(n):
        minIndex = minInRange(lyst, i, n, comps)
        if minIndex != i:
            swap(lyst, i, minIndex, swaps)

def minInRange(li, i, n, comps):
    """Finds the minimum value in a given range """
    minValue = li[i]
    minIndex = i
    for j in range(i, n):
        if comps: comps.increment()
        if li[j] < minValue:
            minValue = li[j]
            minIndex = j

    return minIndex
    

def quickSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a quick sort."""
    recurse(lyst, 0, len(lyst) - 1, comps, swaps)

def recurse(lyst, left, right, comps, swaps):
    """Recurses on both sides of the partitioned list """
    if comps: comps.increment()
    if left < right:
        pivotPosition = partition(lyst, left, right, comps, swaps)

        recurse(lyst, left, pivotPosition - 1, comps, swaps)
        recurse(lyst, pivotPosition + 1, right, comps, swaps)

def partition(lyst, left, right, comps, swaps):
    """Partitions the list and returns the pivot point """
    middle = (left + right) // 2

    swap(lyst, middle, right, swaps)

    boundary = left

    for index in range(left, right):
        if comps: comps.increment()
        if lyst[index] < lyst[right]:
            swap(lyst, index, boundary)
            boundary += 1

    swap(lyst, boundary, right, swaps)

    return boundary

def insertionSort(lyst, comps = None, swaps = None):
    """Performs insertion sort"""
    j = 0
    temp = 0
    for i in range(1, len(lyst)):
        j = i - 1
        temp = lyst[i]
        if comps: comps.increment()
        while j >= 0 and temp < lyst[j]:
            if swaps: swaps.increment()
            if comps: comps.increment()
            lyst[j + 1] = lyst[j]
            j-= 1

        lyst[j+1] = temp 
                


def swap(lyst, i, j, counter = None):
    """Exchanges the items at i and j in lyst and increments
    the counter if it exists."""
    if counter: counter.increment()
    lyst[i], lyst[j] = lyst[j], lyst[i]       

def test(sort, n = 15):
    """Runs some tests on a sort function."""
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)

def testWithCounters(sort, n = 15):
    """Runs some tests on a sort function."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))
    comps.reset()
    swaps.reset()
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))


def main():
    """To test, pass the name of the sort function to test."""
    test(selectionSort)
    testWithCounters(selectionSort)
    testWithCounters(selectionSort, n = 150)
    test(quickSort)
    testWithCounters(quickSort, n = 150)
    test(insertionSort)
    testWithCounters(insertionSort, n = 15)

if __name__ == "__main__":
    main()
