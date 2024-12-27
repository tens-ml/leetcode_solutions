# LeetCode #1249: Minimum Remove to Make Valid Parentheses

## **Problem Statement**
Given a string consisting of `'('`, `')'`, and lowercase characters, perform the **minimum number of character removals** needed to make the parentheses balanced or valid. Return the resulting string.  
If multiple solutions exist, return any one of them.

---

## **Initial Thoughts / First Solution**
Parentheses problems often make me think of using a **stack**. Here's the thought process:

1. **Tracking Opens and Closes**:
   - Add **open parentheses** (`'('`) to the stack.
   - Pop the stack when we encounter a **close parenthesis** (`')'`).

2. **Invalid Parentheses**:
   - If the stack is empty and we encounter a **close parenthesis**, it means the parenthesis is invalid and must be removed.
   - At the end of the string, any remaining indices in the stack (unmatched open parentheses) are invalid and must also be removed.

3. **Two-Pass Approach**:
   - **First Pass**: 
     - Track indices of invalid parentheses using:
       - A `stack` for unmatched open parentheses.
       - A `remove` list for invalid close parentheses.
   - **Second Pass**:
     - Remove all invalid indices (both from the stack and the `remove` list) from the string.

4. **Efficiency**:
   - Using a **set** to store indices of characters to remove ensures that the final pass to construct the valid string is O(n).

---

### **Plan for the Solution**
1. Perform a **first pass** over the string:
   - Use a `stack` to track indices of unmatched open parentheses (`'('`).
   - Use a `remove` list to track indices of invalid close parentheses (`')'`).

2. At the end of the first pass:
   - Any indices left in the `stack` (unmatched opens) must also be removed.

3. Combine the indices from the `stack` and `remove` list into a **set**.

4. Perform a **second pass** to construct the resulting string, skipping all indices in the invalid set.

---

### **Key Insights**
- The problem can be solved in **two linear passes**:
  - **First Pass**: Identify invalid indices.
  - **Second Pass**: Construct the valid string.
- By using a **stack** for open parentheses and a **set** for invalid indices, the solution is efficient and simple.

---

### **Time Complexity**
- **First Pass**: O(n), where \( n \) is the length of the string.
- **Second Pass**: O(n) to construct the valid string.
- **Overall**: O(n).

### **Space Complexity**
- The `stack` and `remove` list/store take O(n) space in the worst case.
- **Overall**: O(n).

---
