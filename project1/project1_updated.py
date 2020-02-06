"""
ECE 590
Project 1
Fall 2019

Partner 1: Yuhang Liu
Partner 2: Kuan Wang
Date: Oct 27th 2019
"""
"""
SelectionSort
"""
def SelectionSort(listToSort):
    # each first pointer points from start index i and to the final index minus 1.
    for i in range(0, len(listToSort) - 1):
        # select the first unsorted number as the minimum one.
        min = listToSort[i]
        index = i
        # each second pointer points from i + 1 to final index
        # in this for loop we will finally find the minimum one in the unsorted array.
        for j in range(i+1, len(listToSort)):
            if listToSort[j] < min:
                min = listToSort[j]
                index = j
        # swap the minimum with the first element in the originally unsorted list.
        listToSort[i], listToSort[index] = listToSort[index], listToSort[i]
    # after each loop the 0 to i - 1 elements are sorted
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    # the pointer starts from i to the final index
    for i in range(0, len(listToSort)):
        # the value will continue comparing the value with elements in front of it, once it is large than it, stop and go to next loop.
        while i >= 1:
            if listToSort[i] >= listToSort[i - 1]:
                break
            else:
                listToSort[i], listToSort[i - 1] = listToSort[i - 1], listToSort[i]
                i = i - 1

    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    # need is a boolean value and serves as a flag, once need is true, we need to scan the array.
    # after each iteration, the largest element will go to the end of the array.
    need = 1
    j = 0
    while need:
        j += 1
        need = 0
        for i in range(0, len(listToSort) - j):
            if listToSort[i] > listToSort[i + 1]:
                listToSort[i], listToSort[i + 1] = listToSort[i + 1], listToSort[i]
                """ if a swap happen in this scanning, we must need a new process
                    if no swap happens in this scanning, we can make sure that all elements are sorted.
                """
                need = 1
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    l = 0
    r = len(listToSort) - 1
    # The condition for the next dividing is that there ae more than one element in this array
    if l < r:
        m = (l + r) // 2
        # put the element from 0 to m in the first array
        # put the element from m + 1 to last in the second array.
        l1 = listToSort[:m + 1]
        l2 = listToSort[m + 1:]
        MergeSort(l1)
        MergeSort(l2)

        i = l
        index1 = 0
        index2 = 0
        # This while loop is used to compare the minimum from two arrays and then combine then
        # The end of this loop is that one of the array has been used, which means that all the element have putted in the original one.
        while index1 < len(l1) and index2 < len(l2):
            if l1[index1] <= l2[index2]:
                listToSort[i] = l1[index1]
                index1 = index1 + 1
            else:
                listToSort[i] = l2[index2]
                index2 = index2 + 1
            i += 1

        # Put the remaining of the array (maybe l1 or l2) into the original one.
        if index1 < len(l1):
            for j in range (index1, len(l1)):
                listToSort[i] = l1[j]
                i = i + 1

        elif index2 < len(l2):
            for j in range (index2, len(l2)):
                listToSort[i] = l2[j]
                i = i + 1

    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    # Make sure that there is at least two elements in the array
    if i > j - 1:
        return

    # Left the the index of first element, right is the index of the last element
    left = i
    right = j - 1
    mid = (left + right) // 2
    # Select the middle element in the array as pivot
    pivot = listToSort[mid]
    # Change the value of right and left when they are both stopped
    while left <= right:
        while listToSort[right] > pivot and right >= left:
            right -= 1
        while listToSort[left] < pivot and right >= left:
            left += 1
        if left <= right:
            listToSort[right], listToSort[left] = listToSort[left], listToSort[right]
            right -= 1
            left += 1
    # When the left pointer is on the right of right pointer, the while loop will stops
    # select the first part as from i to right
    # select the second part as from left to j
    QuickSort(listToSort, i, right + 1)
    QuickSort(listToSort, left, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests_updated import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
