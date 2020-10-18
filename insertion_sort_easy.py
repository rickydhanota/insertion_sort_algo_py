#Insertion Sort
#Write a function that takes in an array of integers and returns a sorted version of that array. Use the insertion array method
#array = [8, 5, 2, 9, 5, 6, 3]
#output = [2, 3, 5, 5, 6, 8, 9]

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            # swap(j, j-1, array)
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))