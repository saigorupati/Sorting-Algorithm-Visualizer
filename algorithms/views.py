from django.shortcuts import render, HttpResponse
import random


def arrayValues():
    ar = []
    for i in range(0, 150):
        ar.append(random.randint(50, 590))
    return ar


def index(request):
    global arr
    arr = arrayValues()
    return render(request, 'index.html', {'arr': arr})


def mergesort(request):
    animations = getMergeSortAnimations(arr)
    return HttpResponse([animations])


def getMergeSortAnimations(arr):
    animations = []
    if len(arr) <= 1:
        return arr
    auxArray = arr.copy()
    mergeSortHelper(arr, 0, len(arr)-1, auxArray, animations)
    return animations


def mergeSortHelper(mainArray, start, end, auxArray, animations):
    if start == end:
        return
    mid = (start + end) // 2
    mergeSortHelper(auxArray, start, mid, mainArray, animations)
    mergeSortHelper(auxArray, mid + 1, end, mainArray, animations)
    merge(mainArray, start, mid, end , auxArray, animations)


def merge(mainArray, start, mid, end, auxArray, animations):
    k, i, j = start, start, mid + 1
    while i <= mid and j <= end:
        animations.append([i, j])
        animations.append([i, j])
        if auxArray[i] <= auxArray[j]:
            animations.append([k, auxArray[i]])
            mainArray[k] = auxArray[i]
            k += 1
            i += 1
        else:
            animations.append([k, auxArray[j]])
            mainArray[k] = auxArray[j]
            k += 1
            j += 1

    while i <= mid:
        animations.append([i, i])
        animations.append([i, i])
        animations.append([k, auxArray[i]])
        mainArray[k] = auxArray[i]
        k += 1
        i += 1

    while j <= end:
        animations.append([j, j])
        animations.append([j, j])
        animations.append([k, auxArray[j]])
        mainArray[k] = auxArray[j]
        k += 1
        j += 1

def quicksort(request):
    animations = getQuickSortAnimations(arr)
    return HttpResponse([animations])


def getQuickSortAnimations(arr):
    animations = []
    auxArray = arr.copy()
    quickSortHelper(auxArray, 0, len(auxArray) - 1, animations)
    return animations


def quickSortHelper(auxArray, start, end, animations):
    if start < end:
        pivotIndex = partition(auxArray, start, end, animations)
        quickSortHelper(auxArray, start, pivotIndex - 1, animations)
        quickSortHelper(auxArray, pivotIndex + 1, end, animations)


def partition(auxArray, start, end, animations):
    pivot = auxArray[end]
    pivotIndex = start
    for i in range(start, end):
        animations.append([i, end])
        animations.append([i, end])
        if auxArray[i] <= pivot:
            animations.append([i, auxArray[pivotIndex]])
            animations.append([pivotIndex, auxArray[i]])
            auxArray[i], auxArray[pivotIndex] = auxArray[pivotIndex], auxArray[i]
            pivotIndex += 1
        else:
            animations.append([-1, -1])
            animations.append([-1, -1])
        animations.append([-1, -1])
        animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([pivotIndex, auxArray[end]])
    animations.append([end, auxArray[pivotIndex]])
    auxArray[pivotIndex], auxArray[end] = auxArray[end], auxArray[pivotIndex]
    return pivotIndex


def bubblesort(request):
    animations = getBubbleSortAnimations(arr)
    return HttpResponse([animations])


def getBubbleSortAnimations(arr):
    animations = []
    auxArray = arr.copy()
    bubbleSortHelper(auxArray, animations)
    return animations


def bubbleSortHelper(auxArray, animations):
    for i in range(0, len(auxArray) - 1):
        for j in range(0, len(auxArray) - 1):
            animations.append([j, j+1])
            animations.append([j, j+1])
            if auxArray[j] > auxArray[j+1]:
                animations.append([j, auxArray[j+1]])
                animations.append([j+1, auxArray[j]])
                auxArray[j], auxArray[j+1] = auxArray[j+1], auxArray[j]
            else:
                animations.append([-1, -1])
                animations.append([-1, -1])



def selectionsort(request):
    animations = getSelectionSortAnimations(arr)
    return HttpResponse([animations])


def getSelectionSortAnimations(arr):
    animations = []
    auxArray = arr.copy()
    selectionSortHelper(auxArray, animations)
    return animations


def selectionSortHelper(auxArray, animations):

    for i in range(0, len(auxArray)):
        minIndex = i
        for j in range(i+1, len(auxArray)):
            animations.append([999, j, minIndex])
            animations.append([9999, j, minIndex])
            if auxArray[j] < auxArray[minIndex]:
                minIndex = j
        animations.append([99999, minIndex, auxArray[i]])
        animations.append([99999, i, auxArray[minIndex]])

        auxArray[minIndex], auxArray[i] = auxArray[i], auxArray[minIndex]


def insertionsort(request):
    animations = getInsertionSortAnimations(arr)
    return HttpResponse([animations])


def getInsertionSortAnimations(arr):
    animations = []
    auxArray = arr.copy()
    selectionSortHelper(auxArray, animations)
    return animations


def insertionSortHelper(auxArray, animations):
    for i in range(1, len(auxArray)):
        key = auxArray[i]
        j = i - 1
        animations.append([999, j, i])
        animations.append([9999, j, i])
        while j >= 0 and auxArray[j]>key:
            animations.append([99999, j + 1, auxArray[j]])
            auxArray[j + 1] = auxArray[j]
            j -= 1
            if j >= 0:
                animations.append([999, j, i])
                animations.append([9999, j, i])
        animations.append([99999, j + 1, key])
        auxArray[j + 1] = key