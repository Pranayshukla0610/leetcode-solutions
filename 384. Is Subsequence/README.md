# Is Subsequence | Two Pointers

A Python solution to the **Is Subsequence** problem using the **Two Pointers** technique. The algorithm efficiently determines whether one string is a subsequence of another by traversing both strings simultaneously.

## Problem Statement

Given two strings `s` and `t`, determine whether `s` is a subsequence of `t`.

## Approach

- Initialize two pointers for `s` and `t`.
- Traverse `t` while comparing characters with `s`.
- Move both pointers on a match; otherwise, move only the pointer in `t`.
- If all characters of `s` are matched in order, return `True`.

## Algorithm

1. Initialize pointers `i` and `j`.
2. Compare `s[i]` and `t[j]`.
3. Move pointers according to the comparison.
4. Return whether all characters of `s` have been matched.

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Key Concepts

- Two Pointers
- Same Direction Traversal
- String Matching
- Greedy Character Comparison

## Tech Stack

- Python 3

## Learning Outcome

This problem introduces the **Same-Direction Two Pointers** pattern, a fundamental technique for efficiently comparing
