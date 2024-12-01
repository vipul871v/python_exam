# Debugging Calendar Design

## Overview
This document explains the debugging process for the `Calendar` class implementation, identifies issues in the original code, describes the fixes applied, and outlines the testing methodology.

## Debugging Steps

### Identified Issues
1. **Incorrect Overlap Detection**:
   - The condition for overlap in the `Node.insert()` method was incorrect.
   - Original code used:
     ```python
     if node.start <= self.end:
         ...
     elif node.end >= self.start:
         ...
     ```
     This logic led to improper detection of overlaps and incorrect tree structure.

2. **Improper Tree Structure**:
   - Non-overlapping events were not placed correctly in the binary tree.
   - Events should be placed in the left subtree if they end before the current node starts, and in the right subtree if they start after the current node ends.

3. **Missing Edge Case Handling**:
   - The code did not handle edge cases, such as when the tree is empty or when events are back-to-back.

### Fixes Applied
1. **Corrected Overlap Detection**:
   - The overlap detection condition was fixed to:
     ```python
     if not (node.end <= self.start or node.start >= self.end):
         return False
     ```
     This ensures that overlapping intervals are correctly identified.

2. **Ensured Proper Tree Structure**:
   - Non-overlapping events are now placed in the appropriate subtree:
     ```python
     if node.end <= self.start:
         ...
     elif node.start >= self.end:
         ...
     ```

3. **Handled Edge Cases**:
   - Explicitly checked for `None` nodes and ensured the root node is initialized properly.