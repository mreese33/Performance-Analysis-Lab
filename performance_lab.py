# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return max(counts, key=counts.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) since every number has to be counted.
- Worst-case: O(n) because the whole list gets checked.
- Average-case: O(n) since each number is looked at once.
- Space complexity: O(n) because the dictionary keeps
  track of each number and how many times it appears.
- Why this approach? A dictionary makes it easier to
  count how often numbers show up without having to
  go through the list multiple times.
- Could it be optimized? Another option would be to
  sort the list and count repeated numbers. This could
  use less extra memory but would take more time.
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



"""
Time and Space Analysis for problem 2:
- Best-case: O(n) because the list still has to be checked.
- Worst-case: O(n) since every number needs to be looked at.
- Average-case: O(n) because the loop goes through each item.
- Space complexity: O(n) because a set and another list
  are used to store the numbers.
- Why this approach? The set helps check which numbers
  have already appeared, while the list keeps everything
  in the same order.
- Could it be optimized? Using only a list would save
  some memory, but checking for duplicates would take
  longer as the list gets bigger.
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
    pairs = []

    for num in nums:
        difference = target - num

        if difference in seen:
            pairs.append((difference, num))

        seen.add(num)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) because the function checks every number.
- Worst-case: O(n) since it goes through the full list.
- Average-case: O(n) because each number is checked once.
- Space complexity: O(n) because the set stores numbers
  and the list stores the matching pairs.
- Why this approach? Using a set makes it easier to
  find numbers that add up to the target without
  needing to compare every possible pair.
- Could it be optimized? Sorting the list and using
  two pointers is another option. It could save
  memory but would take longer because of sorting.
"""



# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.


def add_n_items(n):
    capacity = 2
    items = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

        items[size] = i
        size += 1

    return items[:size]




"""
Time and Space Analysis for problem 4:
- Best-case: O(n) because all n items need to be added.
- Worst-case: O(n) because even with resizing, the total
  amount of copying grows with the number of items.
- Average-case: O(n) since each item gets added once.
- When do resizes happen? The list resizes whenever
  it reaches its capacity. It starts at 2 and doubles
  to 4, 8, 16, and so on.
- Worst-case for a single append: O(n) because resizing
  means copying all the existing items into a new list.
- Amortized time per append: O(1) because most of the
  time items are added without needing to resize.
- Space complexity: O(n) since the list grows with
  the number of items being added.
- Why does doubling reduce the cost overall?
  Doubling gives the list more room so it doesn't
  have to resize every time another item is added.
  This also means less copying happens overall.
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
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result



"""
Time and Space Analysis for problem 5:
- Best-case: O(n) because all the numbers get added.
- Worst-case: O(n) since the function goes through
  the entire list.
- Average-case: O(n) because each number is added once.
- Space complexity: O(n) because a new list is made
  to hold the running totals.
- Why this approach? Keeping a total while going
  through the list makes it possible to calculate
  each new sum without starting over every time.
- Could it be optimized? The original list could
  be updated instead of making a new one. This
  would save memory but would also change the
  numbers in the original list.
"""


# Optimized version of Problem 5
def running_total_optimized(nums):
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        nums[i] = total

    return nums


"""
Optimization Comparison for Problem 5:
- Original time complexity: O(n)
- Optimized time complexity: O(n)
- Original space complexity: O(n)
- Optimized space complexity: O(1)

The original solution creates a new list to store
the running totals. The optimized version updates
the numbers in the original list instead.

This reduces the extra memory needed because a
second list is no longer created. Both solutions
still go through every number once, so the time
complexity stays the same.

The trade-off is that the optimized version changes
the original list instead of keeping it unchanged.
"""



print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([5, 5, 2, 2]))
print(most_frequent([7]))
print(most_frequent([]))


print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([2, 3, 4, 5]))
print(remove_duplicates([]))


print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([2, 4, 6, 8], 10))
print(find_pairs([1, 2, 3], 10))
print(find_pairs([], 5))
print(find_pairs([-3, -1, 1, 3], 0))


print(add_n_items(6))
print(add_n_items(2))
print(add_n_items(0))
print(add_n_items(10))


print(running_total([1, 2, 3, 4]))
print(running_total([5, 10, 15]))
print(running_total([2]))
print(running_total([]))
print(running_total([-2, 5, -1]))
