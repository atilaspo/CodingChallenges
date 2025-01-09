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
---

## Contact

If you have any suggestions or want to discuss a particular solution, feel free to:

- Open an **issue** or create a **pull request**.
- Reach out via [GitHub](https://github.com/atilaspo).

---
