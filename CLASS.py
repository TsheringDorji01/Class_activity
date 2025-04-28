""""def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()"""

"""# 1. Linear search function
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
arr = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")

# 2. Insertion point for a target value 
def find_insertion_point(sorted_list, target):

    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        
        if sorted_list[mid] == target:
            return mid 
        elif sorted_list[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return left  


# Example usage:
my_list = [2, 5, 7, 8, 11, 12]
target_value = 9

insertion_index = find_insertion_point(my_list, target_value)
print(f"The insertion point for {target_value} is: {insertion_index}") 

my_list2 = [1,3,5,7,9]
target_value2 = 6
insertion_index2 = find_insertion_point(my_list2, target_value2)
print(f"The insertion point for {target_value2} is: {insertion_index2}") 

# 3. Count the number of comparisons
def countCamparisions(n, arr, m, qry) :

	index = {}
	for i in range(1, n + 1) :

		index[arr[i]] = i
	
	# Count of comparisons for left to right and right to left 
	ltr, rtl = 0, 0
	for i in range(1, m + 1) :
		x = qry[i]
		ltr += index[x] 
		rtl += n - index[x] + 1
	
	return (ltr, rtl) 

# Driver Code
if __name__ == "__main__" :

	arr = [ -1, 2, 4, 5, 1 ] 
	n = len(arr) - 1

	q = [ -1, 4, 2 ] 
	m = len(q) - 1

	res = countCamparisions(n, arr, m, q) 
	print(res[0], res[1])
	
# Jump search algorithm
import math

def jump_search(arr, x):  
  n = len(arr)
  step = int(math.sqrt(n)) # Calculate the jump step size

  # Find the block containing the target value
  prev = 0
  curr = step
  while curr < n and arr[curr] <= x:
    prev = curr
    curr += step
  
  # Perform linear search in the block
  for i in range(prev, min(curr, n)):
    if arr[i] == x:
      return i
    
  return 2"""

x = input("Enter the number:")
if (x < 5 and x > 2 or x == 3):
    print("S")