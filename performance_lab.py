# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    from collections import Counter
    if not numbers:
        return None
    counts = Counter(numbers)
    most_common = counts.most_common(1)[0][0]
    return most_common

# Test Cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected Output: 3
print(most_frequent([4, 4, 4, 2, 2, 3]))     # Expected Output: 4
print(most_frequent([]))                     # Expected Output: None

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - even with uniform data or a single element,
we still need to go through the entire list to count occurances.
- Worst-case:O(n) - Counting frequencies required you to go ove all
"n" elements. Finding the max in the frequency dictionary is O(k),
where k is the number of unique elements, which is at most n.
- Average-case: O(n) - On average, we still need to count all elements.
- Space complexity: O(n) - The Counter creates a dictionary storing counts
for each unique element. In the worst case, all elements are unique.
- Why this approach?
Using a hash-based counter makes sure that we go over the list once
achieveing O(n) time complexity. The Counter class is straight forward
readable and efficient for this purpose.
- Could it be optimized?
Not significantly for time complexity, as counting frequencies
requires O(n) time. For number ranges that are small, a fixed-size array
could be used instead of a dictionary to save space. Using the Counter increases
space usage (O(n)), but provides fast lookups for frequency counts.
Using an array reduces memory but only works for bounded ranges.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
       if num not in seen:
           seen.add(num)
           result.append(num)
    return result

#Test Cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected Output: [4, 5, 6, 7]
print(remove_duplicates([1, 2, 2, 3, 1]))     # Expected Output: [1, 2, 3]
print(remove_duplicates([]))                  # Expected Output: []

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - Even if there are no duplicates, we have 
to go through all "n" elements once.
- Worst-case: O(n) - In the worst case, all elements are unique,
so each check and and insertion into the seen set occurs once.
- Average-case: O(n) - On average, we still need to process all elements.
- Space complexity: The seen set stores all unique elements. The result list
also stores all unique elements. In the worst case, all elements are unique
requiring O(n) space.
- Why this approach?
This approach removes duplicated while preserving the original order
by using a set to track seen elements and a list to store the result. 
Using these data structures allows the fuction to run in O(n) time,
which is much fast than checking the list repeatedly (O(n^2)). It's considered
optimal because it balances speed and correctness with minimal extra memory.
- Could it be optimized?
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    output = []
    
    for num in nums: 
        complement = target - num
        if complement in seen:
            output.append((num, complement))
        seen.add(num)
        
    return output
   
#Test Cases
print(find_pairs([1, 2, 3, 4], 5))  # Expected Output: [(1, 4), (2, 3)]
print(find_pairs([0, -1, 2, -3, 1], -2))  # Expected Output: [(1, -3)]
print(find_pairs([1, 2, 3], 6))  # Expected Output: []

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) - Each element is processed once. The complement check in the set is O(1).
- Worst-case: o(n) - Even if the numbers form a valid pair, the function still only loops
through the list once, performing O(1) operations for each element.
- Average-case: O(n) - On average, for typical inputs, the loop runs once per element and
set opperations remain constant time.
- Space complexity: The seen set stores all the numbers encounters so far (up to n elements).
The output list stores the resulting pairs, which could roughly be up to n/2 pairs in the worst case.
thus, space complexity is O(n).
- Why this approach?
using a set allows constant time lookups for the complement of each number.
This avoids the need for nested loops, which would take O(n^2) time.
- Could it be optimized?
If the input lists were sorted, we could use as two-pointer approach, which scans from both ends towards
the middle. This would reduce the extra memory usage to O(1) while still finding all pairs in linear time.
The current method uses extra memory (O(n)) but is simple and very fast. Two pointer method saves memory but requires
sorting fitst which takes O(n log n) time.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    lst = []

    for i in range(n):
        if len(lst) == capacity:
            capacity *= 2
            print(f"Resized to capacity {capacity}")
        lst.append(i)

# Test Case
add_n_items(6)  # Expected Output: Resized to capacity 2, Resized to capacity 4, Resized to capacity 8

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
Every time the number of elements reaches a certain capacity. For a list capacity
this happens at the sizes 1, 2, 4, 8, etc.
- What is the worst-case for a single append?
O(n) - occurs when a resize happends because all existing elements must be copied to the new list.
- What is the amortized time per append overall?
O(1) - While individual appends may take O(n) time during a resize,
most appends take O(1) time. Over many appends, the average cost per operation remains constant.
- Space complexity: O(n) - The list eventually stores all "n" elements. Extra space is temporarily
used during resizing, but this is proportional to the number of elements.
- Why does doubling reduce the cost overall?
By doubling the capacity each time, the number of resizes grows logarithmically with n. This ensures
that the total cost of all resizes is proportional to n, making the amortized cost per append O(1)
rather than O(n).
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0
    for num in nums:
        current_sum += num
        totals.append(current_sum)
    return totals

# Test Cases
print(running_total([1, 2, 3, 4]))  # Expected Output: [1, 3, 6, 10]
print(running_total([-10]))     # Expected Output: [-10]
print(running_total([]))            # Expected Output: []   
print(running_total([-1, 1, -1, 1]))  # Expected Output: [-1, 0, -1, 0]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) - We have to iterate through every element at least once, even if the list is short.
- Worst-case: O(n) - we still need to process all "n" elements. Each element requires a simple addition
and append operation.
- Average-case: The function must process each element once to compute the running total. Each addition
and append opperation takes constant time, so performace scales linearly with the size of the list.
- Space complexity: O(n) - We create a new list to stope the running totals, which requires additional
memory proportional to the input size
- Why this approach? 
It is simple and efficient because it maintains a running sum insteas of recalculating sums repeatedly.
Using sum(nums[:i+1]) would be much slower (O(n^2)), since each sum would traverse a portion of the list.
- Could it be optimized?
This approach is already time optimal at O(n). If allowed, we could modify the original list in-place to
save memory, reducing space complexity to O(1), but this would overwrite the input data.
"""


"""
Refactored Code (Problem 5[running totals])
"""

def running_total_inplace(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

#test cases
print(running_total_inplace([1,2,3,4]))         #Expected [1, 3, 6, 10]
print(running_total_inplace([-10]))             #Expected [-10]
print(running_total_inplace([-1,1,-1,1]))       #Expected [-1, 0, -1, 0]

"""
Comparison:
Original - 
    Time Complexity: O(n) - iterate through all elements at once
    Space Complexity: O(n) - creates a new list of size n

Refractored (in-place) - 
    Time Complexity: O(n) - iterate through all elements once
    Space Complexity: O(1) - no additional list created, modifies input directly

Optimization:
The refactored version reduces memory usage by avoiding creation of a new list.
The trade-off is that it modifies the original list, which may no be desireable if the
original data must be preserved.
"""