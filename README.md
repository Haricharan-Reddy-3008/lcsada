# lcsada

# 🧬 Longest Common Subsequence (LCS) Visualization using Python

## 📌 Project Overview

The **Longest Common Subsequence (LCS)** problem is a classical dynamic programming problem in computer science. It finds the longest subsequence present in both sequences in the same order (not necessarily contiguous). 

This project:
- Solves the LCS problem using a bottom-up Dynamic Programming approach.
- Displays the DP (Dynamic Programming) table using **Pandas** for easy understanding.
- Reconstructs and prints the LCS and its length.
- (Optional) Can be extended to export results into a PDF using **fpdf**.
- Can be run in **Google Colab**, **Jupyter Notebook**, or any standard Python environment.

---

## 🧠 Problem Statement

Given two sequences (strings), determine:
- The **length** of the longest subsequence common to both.
- The **actual subsequence** (LCS).
- A **visual representation** of the table used to compute the LCS.

> 💡 A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

---

## 🏗️ Project Architecture & Logic

### 💡 Dynamic Programming Approach

1. Create a 2D array `lcs_table` of size `(m+1) x (n+1)` where `m` and `n` are the lengths of the input strings.
2. Initialize all values to 0.
3. Iterate through the strings:
   - If characters match:  
     `lcs_table[i][j] = lcs_table[i-1][j-1] + 1`
   - Else:  
     `lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])`
4. Backtrack from `lcs_table[m][n]` to reconstruct the LCS.

### 🔁 Strings Used

```python
str1 = "AGGTA"
str2 = "GXTXAYB"



sample output :-
LCS Table:
(Displayed as a formatted Pandas DataFrame)

Length of LCS is: 3
The LCS is: GTA
