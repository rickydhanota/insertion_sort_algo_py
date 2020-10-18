#Insertion Sort
#Write a function that takes in an array of integers and returns a sorted version of that array. Use the insertion array method
#array = [8, 5, 2, 9, 5, 6, 3]
#output = [2, 3, 5, 5, 6, 8, 9]

def insertionSort(array):
    for i in range(1, len(array)): #We start at 1 because we're basically creating a sub array within the array which consists of 1 value at the start. We then look at every proceeding value and sort it within the sub array. We're not, however, actually creating a sub array.
        j = i
        while j > 0 and array[j] < array[j - 1]:
            # swap(j, j-1, array)
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1 #we do j -= 1 because we want it to sort with the preceeding numbers and not the proceeding numbers because that would be incorrect. basically loop forward with the iniital for loop and then loop backwards with this while loop
    return array

# def swap(i, j, array):
#     array[i], array[j] = array[j], array[i]

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))