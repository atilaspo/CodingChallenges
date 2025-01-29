# CodingChallenges

This repository contains my solutions to various programming and algorithmic challenges. The main goal is to **practice**, **document**, and **track** my progress to improve problem-solving skills for technical interviews and personal development.

## Table of Contents
1. [Overview](#overview)
2. [How to Use](#how-to-use)
3. [Challenges](#challenges)
4. [Contact](#contact)

---

## Overview

- **Purpose**: Collect coding challenge solutions, study common data structures and algorithms, and continually improve coding proficiency.
- **Technologies**: Primarily Python (3.x). 

---

## How to Use

1. **Clone** the repository:
   ```bash
   git clone https://github.com/atilaspo/CodingChallenges.git
   ```
2. **Navigate** to any folder to view the challenge you're interested in:
   ```bash
   cd CodingChallenges/
   ```
3. **Run** or **inspect** the Python scripts. For example:
   ```bash
   python string-encode-and-decode.py
   ```
   Or open the files in your editor (e.g., VS Code) to explore the implementation.

---

## Challenges

### 1. **[Encode and Decode Strings](string-encode-and-decode.py)**
- **Goal**: Encode an array of strings into a single string, then decode it back into the original array.
- **Approach**: For each string, store its length followed by `#`, then the string.
- **Time Complexity**: O(m) where m is the total length of all strings.
- **Space Complexity**: O(1) auxiliary (excluding the final output).

### 2. **[Valid Sudoku](valid-sudoku.py)**
- **Goal**: Validate a 9x9 Sudoku board by checking that:
  - Each row contains unique digits.
  - Each column contains unique digits.
  - Each 3x3 subgrid contains unique digits.
- **Approach**:
  - Use three dictionaries (`defaultdict(set)`) to track seen numbers in rows, columns, and subgrids.
  - If a duplicate is found in any row, column, or subgrid, return `False`.
- **Time Complexity**: O(1) (fixed size of 81 cells for a 9x9 board).
- **Space Complexity**: O(1) additional space (ignoring input size).

### 3. **[Longest Consecutive Sequence](longest-consecutive-sequence.py)**
- **Goal**: Find the length of the longest consecutive sequence of integers in an array.
- **Approach**:
  - Use a `set` to store the unique integers in the array for fast lookup.
  - For each number, check if it is the start of a sequence (`num - 1` not in the set).
  - If it is, extend the sequence by checking for consecutive numbers (`num + 1`, `num + 2`, etc.) in the set.
  - Keep track of the longest sequence found.
- **Time Complexity**: O(n), where n is the length of the input array.
- **Space Complexity**: O(n), for the `set` storing the unique numbers.

### 4. **[Contains Duplicate](contains-duplicate.py)**
- **Goal**: Determine if any value appears more than once in an array.
- **Approach**:
  - Use a dictionary (`memory`) to keep track of numbers encountered so far.
  - Iterate through the array and check if a number is already in the dictionary:
    - If it is, return `True` (duplicate found).
    - Otherwise, add the number to the dictionary.
- **Time Complexity**: O(n), where n is the length of the input array.
- **Space Complexity**: O(n), for the dictionary storing encountered numbers.

### 5. **[Valid Anagram](valid-anagram.py)**
- **Goal**: Determine if two strings are anagrams of each other. Two strings are anagrams if they have the same characters with the same frequencies.
- **Approach**:
  - First, check if the lengths of the two strings are different. If they are, return `False` immediately.
  - Create two dictionaries (`mem_s` and `mem_t`) to store the frequency of each character in the strings `s` and `t`.
  - Iterate through each character in `s` and `t`, updating the dictionaries to count the occurrences of each character.
  - Compare the two dictionaries:
    - If they are equal, the strings are anagrams.
    - Otherwise, they are not.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the longer string (`s` or `t`).
- **Space Complexity**: \(O(k)\), where \(k\) is the number of unique characters in the strings.

### 6. **[Two Sum](two-sum.py)**
- **Goal**: Find two indices \(i\) and \(j\) in an array `nums` such that \(nums[i] + nums[j] = target\) and \(i \neq j\).
- **Approach**:
  - Use a dictionary (`memory`) to store numbers and their indices as you iterate through the array.
  - For each number, calculate its complement (`target - num`) and check if it exists in the dictionary:
    - If it does, return the indices of the complement and the current number.
    - Otherwise, store the current number and its index in the dictionary.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the input array.
- **Space Complexity**: \(O(n)\), for the dictionary storing encountered numbers.

### 7. **[Valid Palindrome](valid-palindrome.py)**
- **Goal**: Determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.
- **Approach**:
  - Filter out all non-alphanumeric characters from the string and convert it to lowercase.
  - Use two pointers (`i` and `j`) to compare characters from the beginning and the end of the string:
    - If any pair of characters does not match, return `False`.
    - If all characters match, the string is a palindrome.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the input string.
- **Space Complexity**: \(O(n)\), for the filtered and converted string.

### 8. **[Two Sum II - Input Array Is Sorted](two-sum-ii.py)**
- **Goal**: Find two indices \(i\) and \(j\) (1-indexed) in a sorted array `numbers` such that \(numbers[i] + numbers[j] = target\) and \(i < j\).
- **Approach**:
  - Use two pointers:
    - One pointer starts at the beginning of the array (`l`).
    - The other starts at the end of the array (`r`).
  - Calculate the sum of the numbers pointed to by `l` and `r`:
    - If the sum is greater than the target, move the right pointer (`r`) to the left.
    - If the sum is less than the target, move the left pointer (`l`) to the right.
    - If the sum equals the target, return the indices adjusted to 1-indexed.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the input array.
- **Space Complexity**: \(O(1)\), since no additional data structures are used.

### 9. **[3Sum](three-sum.py)**
- **Goal**: Find all unique triplets in the array that sum up to `0`. Each triplet should be returned only once, even if there are duplicates in the array.
- **Approach**:
  - Sort the array to simplify handling duplicates and use the two-pointer technique.
  - Iterate through the array, fixing one number at a time, and use two pointers to find pairs that sum to the opposite of the fixed number.
  - Skip duplicates for both the fixed number and the two pointers to avoid duplicate triplets.
- **Time Complexity**: \(O(n^2)\), where \(n\) is the length of the array.
- **Space Complexity**: \(O(1)\), since no additional data structures are used (excluding the result list).

### 10. **[Container With Most Water](container-with-most-water.py)**
- **Goal**: Given an array `heights` where `heights[i]` represents the height of the \(i^{th}\) bar, find two bars that form a container that can store the maximum amount of water.
- **Approach**:
  - Use the two-pointer technique:
    - Start with one pointer at the beginning (`l`) and one at the end (`r`) of the array.
    - Calculate the area of water the container can hold using the formula:
    
    - Area = min(heights[l], heights[r]) * distance (r - l)
    
    - Move the pointer pointing to the smaller height inward to try and find a taller bar.

    - Keep track of the maximum area encountered during the process.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the array.
- **Space Complexity**: \(O(1)\), since no additional data structures are used.

### 11. **[Trapping Rain Water](trapping-rain-water.py)**
- **Goal**: Given an array `height` where `height[i]` represents the elevation at index \(i\), calculate how much water can be trapped after raining.
- **Approach**:
  - Use the two-pointer technique to calculate trapped water:
    - Initialize two pointers (`l` and `r`) at the beginning and end of the array.
    - Maintain variables `max_left` and `max_right` to store the maximum height seen so far from the left and right.
    - Move the pointer pointing to the smaller height inward, and calculate the trapped water based on the difference between the current height and the maximum height on that side.
    - Add the trapped water for each step.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the array.
- **Space Complexity**: \(O(1)\), since no additional data structures are used.

### 12. **[Valid Parentheses](valid-parentheses.py)**
- **Goal**: Determine if a given string `s` consisting of the characters `(`, `)`, `{`, `}`, `[`, and `]` is valid.
  - A string is valid if:
    1. Every open bracket is closed by the same type of bracket.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
- **Approach**:
  - Use a **stack** to track unmatched open brackets:
    - When encountering an open bracket, push it onto the stack.
    - When encountering a closing bracket, check if it matches the last open bracket in the stack:
      - If it matches, pop the stack.
      - If it doesn’t match or the stack is empty, return `False`.
    - At the end, the stack should be empty if all brackets are valid.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string.
- **Space Complexity**: \(O(n)\), for the stack used to store unmatched brackets.

### 13. **[Min Stack](min-stack.py)**
- **Goal**: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- **Approach**:
  - Use two stacks:
    1. **`stack`**: Stores all the elements.
    2. **`min_stack`**: Tracks the minimum value at each point in time.
  - For every `push` operation, calculate the new minimum and add it to `min_stack`.
  - For every `pop` operation, remove the top element from both `stack` and `min_stack`.
  - The minimum element can always be retrieved from the top of `min_stack`.
- **Time Complexity**: \(O(1)\) for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity**: \(O(n)\), where \(n\) is the number of elements in the stack.

### 14. **[Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.py)**
- **Goal**: Evaluate an arithmetic expression in Reverse Polish Notation (RPN). The input is a list of tokens representing numbers and operators (`+`, `-`, `*`, `/`).
- **Approach**:
  - Use a stack to store numbers and intermediate results:
    - Push numbers onto the stack.
    - When encountering an operator, pop the top two elements from the stack, perform the operation, and push the result back onto the stack.
  - Division truncates toward zero.
- **Time Complexity**: \(O(n)\), where \(n\) is the number of tokens.
- **Space Complexity**: \(O(n)\), for the stack.

### 15. **[Generate Parentheses](generate-parentheses.py)**
- **Goal**: Generate all combinations of well-formed parentheses given an integer `n`, representing the number of pairs of parentheses.
- **Approach**:
  - Use **backtracking** to explore all possible combinations of parentheses:
    - Add a `(` if the number of open parentheses is less than `n`.
    - Add a `)` if the number of close parentheses is less than the number of open parentheses.
    - Stop when both open and close parentheses are equal to `n`, and add the current combination to the result.
  - Use a `stack` to build each combination step by step and backtrack by removing the last added element (`stack.pop()`).
- **Time Complexity**: \(O(4^n / \sqrt{n})\), due to the Catalan number property.
- **Space Complexity**: \(O(n)\), for the recursion stack and temporary `stack`.

### 16. **[Daily Temperatures](daily-temperatures.py)**
- **Goal**: Given a list of daily temperatures, determine how many days you need to wait for a warmer temperature. If no future day has a warmer temperature, the result for that day should be `0`.
- **Approach**:
  - Use a **monotonic decreasing stack** to keep track of temperatures and their indices.
  - For each temperature:
    - Compare it with the last temperature in the stack.
    - If it is warmer, pop the stack and calculate the difference in indices to update the result.
    - Push the current temperature and its index onto the stack.
  - If the stack is not empty after processing all temperatures, the remaining indices correspond to days with no warmer temperature.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the input array. Each temperature is pushed and popped from the stack at most once.
- **Space Complexity**: \(O(n)\), for the stack and result array.

### 17. **[Car Fleet](car-fleet.py)**
- **Goal**: Determine the number of car fleets that will arrive at a given target position on a single-lane highway.
- **Approach**:
  - Combine the `position` and `speed` arrays into pairs and sort them in descending order of position.
  - Use a variable `last_time` to track the time of the last fleet to arrive at the destination.
  - For each car:
    - Calculate its time to the destination.
    - If the current car's time is greater than `last_time`, it forms a new fleet.
    - Update `last_time` to the current car's time.
  - Count the number of fleets using a simple counter.
- **Time Complexity**: \(O(n \log n)\), due to the sorting step.
- **Space Complexity**: \(O(1)\), auxiliary space.

### 18. **[Largest Rectangle in Histogram](largest-rectangle-in-histogram.py)**
- **Goal**: Given an array of bar heights representing a histogram, find the area of the largest rectangle that can be formed within the histogram.
- **Approach**:
  - Use a **monotonic stack** to keep track of the heights and their starting indices.
  - For each bar:
    - If the current bar height is less than the height of the bar on top of the stack, calculate the area for the rectangle with the popped bar as the smallest height.
    - Track the starting index of each rectangle.
  - After processing all bars, calculate the area for the remaining bars in the stack.
- **Time Complexity**: \(O(n)\), as each bar is pushed and popped from the stack at most once.
- **Space Complexity**: \(O(n)\), for the stack.

### 19. **[Reverse Linked List](reverse-linked-list.py)**
- **Goal**: Reverse a singly linked list, so that the last node becomes the head and all pointers are reversed.
- **Approach**:
  - Use two pointers:
    - `prev`: Tracks the previous node, starting as `None`.
    - `curr`: Tracks the current node, starting at the head of the list.
  - Traverse the list:
    - Save the next node temporarily.
    - Reverse the current node's pointer to point to the previous node.
    - Move the pointers forward to process the next node.
  - Return `prev` as the new head when traversal is complete.
- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list.
- **Space Complexity**: \(O(1)\), as it modifies the list in place.

### 20. **[Merge Two Sorted Lists](merge-two-sorted-lists.py)**
- **Goal**: Merge two sorted linked lists into one sorted linked list.
- **Approach**:
  - Use a **dummy node** as the starting point to simplify list construction.
  - Use a pointer (`tail`) to keep track of the current end of the merged list.
  - Compare nodes from both input lists (`list1` and `list2`):
    - Append the smaller node to the merged list.
    - Advance the pointer in the corresponding list.
  - After exiting the loop, append any remaining nodes from one of the lists.
  - Return the merged list starting from `dummy.next` to exclude the dummy node.
- **Time Complexity**: \(O(n + m)\), where \(n\) and \(m\) are the lengths of `list1` and `list2`.
- **Space Complexity**: \(O(1)\), as the merging is done in place.

### 21. **[Linked List Cycle Detection](linked-list-cycle-detection.py)**
- **Goal**: Determine if a linked list contains a cycle. A cycle exists if any node can be revisited by continuously following the `next` pointers.
- **Approach**: Use the **two pointers technique** (slow and fast):
  - `slow` pointer moves one step at a time.
  - `fast` pointer moves two steps at a time.
  - If there is a cycle, the `fast` pointer will eventually meet the `slow` pointer.
  - If there is no cycle, the `fast` pointer will reach the end of the list (`None`).
- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list.
- **Space Complexity**: \(O(1)\), as no additional data structures are used.

### 22. **[Reorder Linked List](reorder-linked-list.py)**
- **Goal**: Reorder a given singly linked list such that the new order alternates between the first node, the last node, the second node, the second last node, and so on.
- **Approach**:
  1. **Find the middle of the list**:
     - Use the **two-pointer technique** (`slow` and `fast`) to locate the midpoint of the list.
  2. **Reverse the second half**:
     - Starting from the node after the midpoint, reverse the second half of the list using a three-pointer approach (`prev`, `curr`, and `temp`).
  3. **Merge the two halves**:
     - Alternate nodes from the first half and the reversed second half to form the reordered list.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the linked list.
- **Space Complexity**: \(O(1)\), as the reordering is done in place.

### 23. **[Remove Node From End of Linked List](remove-nth-node-from-end.py)**
- **Goal**: Remove the \(n\)-th node from the end of a singly linked list and return the updated list.
- **Approach**:
  1. **Create a dummy node**:
     - A dummy node is created and points to the head of the list to simplify edge cases.
  2. **Use two pointers (`slow` and `fast`)**:
     - Move the `fast` pointer \(n + 1\) steps ahead to create a gap of \(n\) nodes between `slow` and `fast`.
  3. **Traverse the list**:
     - Move both `slow` and `fast` pointers until `fast` reaches the end of the list. At this point, `slow` is just before the node to be removed.
  4. **Remove the node**:
     - Adjust the `next` pointer of `slow` to skip the node to be removed.
  5. **Return the updated list**:
     - Return `dummy.next`, which points to the updated list.

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list.
- **Space Complexity**: \(O(1)\), as no extra space is used beyond the pointers.

### 24. **[Copy Linked List with Random Pointer](copy-random-list.py)**
- **Goal**: Create a deep copy of a linked list where each node has a `val`, a `next` pointer, and a `random` pointer that may point to any node in the list or `None`.

- **Approach**:
  1. **Use a HashMap**:
     - Create a dictionary (`old_copy`) to map each original node to its corresponding copied node.
  2. **First Pass**:
     - Traverse the original list and create a copy of each node.
     - Store the mapping between the original node and its copy in the dictionary.
  3. **Second Pass**:
     - Traverse the original list again to set up the `next` and `random` pointers for each copied node using the dictionary.
  4. **Return**:
     - Return the copied head node stored in the dictionary.

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list. The list is traversed twice.
- **Space Complexity**: \(O(n)\), due to the dictionary used for mapping original nodes to copied nodes.

### 25. **[Add Two Numbers](add-two-numbers.py)**
- **Goal**: Add two numbers represented as reversed linked lists and return their sum as a linked list.
- **Approach**:
  1. **Create a Dummy Node**:
     - Start with a dummy node to simplify list construction.
  2. **Traverse the Lists**:
     - Traverse both input linked lists while keeping track of the carry.
  3. **Calculate the Sum**:
     - For each node, calculate the sum of the values from both lists and the carry.
     - Update the carry for the next iteration.
  4. **Build the Result List**:
     - Create a new node for each digit of the sum and append it to the result list.
  5. **Handle Remaining Carry**:
     - If a carry remains after processing both lists, add an additional node with the carry value.

- **Time Complexity**: \(O(\max(m, n))\), where \(m\) and \(n\) are the lengths of the input linked lists.
- **Space Complexity**: \(O(\max(m, n))\), for the result linked list.

### 26. [Merge K Sorted Linked Lists](merge-k-sorted-linked-lists.py)
- **Goal**: Merge an array of `k` linked lists, where each list is sorted in ascending order, into one sorted linked list.
- **Approach**: 
  - Use a divide-and-conquer strategy:
    1. Merge pairs of linked lists iteratively until there is only one list left.
    2. For each pair of lists, merge them using the `mergeLists` function (similar to merging two sorted lists).
  - Use a dummy node to simplify the merging process.
- **Time Complexity**: \(O(n⋅log k)\)
  - \(n\): Total number of nodes across all linked lists.
  - \(k\): Number of linked lists.
- **Space Complexity**: \(O(1)\) (in-place merging, not counting the output linked list).

### 27. [Longest Substring Without Repeating Characters](longest-substring.py)
- **Problem**: Given a string, find the length of the longest substring that contains no duplicate characters.
- **Approach**:
  - Use the **sliding window technique** with two pointers (`start` and `end`).
  - Maintain a set to keep track of characters in the current substring.
  - Expand the window by moving `end` and shrink it by moving `start` whenever a duplicate is found.
  - Keep track of the maximum window size during the process.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string.
- **Space Complexity**: \(O(m)\), where \(m\) is the number of unique characters in the string.

### 28. [Longest Repeating Character Replacement](longest-repeating-character-replacement.py)
- **Problem**: Given a string `s` and an integer `k`, find the length of the longest substring that can be formed by replacing at most `k` characters with the same character.
- **Approach**:
  - Use the **sliding window technique** with two pointers (`L` and `R`).
  - Maintain a frequency dictionary (`memory`) to count characters in the current window.
  - Check if the current window is valid by ensuring:
    
    \\(\text{window size} - \text{frequency of most common character} \leq k\)

  - If the window becomes invalid, move the `L` pointer to shrink the window.
  - Keep track of the maximum window size during the process.
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string.
- **Space Complexity**: \(O(m)\), where \(m\) is the number of unique characters in the string.

### 29. [Search a 2D Matrix](search-2D-matrix.py)
- **Problem**: Given an \(m 	imes n\) 2D integer array `matrix`, return `True` if `target` exists within the matrix, otherwise return `False`.
- **Approach**:
  - Perform **binary search** to find the correct row where `target` may exist.
  - Perform another **binary search** within the selected row.
- **Time Complexity**: \(O(\log(m 	imes n))\), where \(m\) is the number of rows and \(n\) is the number of columns.
- **Space Complexity**: \(O(1)\).

### 30. [Binary Search](binary-search.py)
- **Problem**: Given a sorted array of distinct integers `nums` and a target value, return the index of the target if it exists, otherwise return `-1`.
- **Approach**:
  - Use the **binary search technique** with two pointers (`L` and `R`).
  - Calculate the middle index `M`.
  - Compare the middle element `nums[M]` with the `target`:
    - If `nums[M] == target`, return the index `M`.
    - If `nums[M] > target`, move the right pointer `R` to `M - 1`.
    - If `nums[M] < target`, move the left pointer `L` to `M + 1`.
- **Time Complexity**: \(O(\log n)\), where \(n\) is the length of the array.
- **Space Complexity**: \(O(1)\).

### 31. [Koko Eating Bananas](koko-eating-bananas.py)
- **Goal**: Given an array `piles` where `piles[i]` is the number of bananas in the *i*-th pile, and an integer `h` (the number of hours), find the minimum integer `k` (eating speed) such that Koko can finish all bananas within `h` hours. Each hour, she can eat up to `k` bananas from exactly one pile (if a pile has fewer than `k`, she finishes that pile in less than an hour and cannot use the remaining time on another pile).
- **Approach**:
  - Use **binary search** on the eating speed `k`, from `1` to `max(piles)`.
  - For each candidate `k`, compute the total hours needed by summing `(pile + k - 1) // k` for each pile (this is effectively `ceil(pile / k)`).
  - If the total hours is `<= h`, move the upper bound down to try a smaller `k`; otherwise, move the lower bound up to try a larger `k`.
- **Time Complexity**: `O(n log m)`, where `n = len(piles)` and `m = max(piles)`.
- **Space Complexity**: `O(1)`, since we only use a few variables for the binary search.


---



## Contact

If you have any suggestions or want to discuss a particular solution, feel free to:

- Open an **issue** or create a **pull request**.
- Reach out via [GitHub](https://github.com/atilaspo).

---
