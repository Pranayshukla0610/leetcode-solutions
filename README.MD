# Reverse String | Two Pointers

A Python solution to the **Reverse String** problem using the **Two Pointers** technique. The algorithm reverses the input character array **in-place**, achieving optimal time and space complexity.

## Problem Statement

Given an array of characters, reverse the array **in-place** without using additional memory.

## Approach

- Initialize two pointers:
  - `left` at the beginning of the array.
  - `right` at the end of the array.
- Swap the characters at both pointers.
- Move `left` forward and `right` backward.
- Continue until the pointers meet.

## Algorithm

1. Set `left = 0` and `right = len(s) - 1`.
2. Swap `s[left]` and `s[right]`.
3. Increment `left` and decrement `right`.
4. Repeat until `left >= right`.

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Key Concepts

- Two Pointers
- In-place Array Manipulation
- String Processing
- Pointer Traversal

## Tech Stack

- Python 3

## Learning Outcome

This problem introduces the **Opposite-End Two Pointers** pattern, a fundamental technique used in many array and string interview problems.
