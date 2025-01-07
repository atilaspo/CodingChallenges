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

---

## Contact

If you have any suggestions or want to discuss a particular solution, feel free to:

- Open an **issue** or create a **pull request**.
- Reach out via [GitHub](https://github.com/atilaspo).

---
