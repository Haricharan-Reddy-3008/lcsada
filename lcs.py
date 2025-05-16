# Install required libraries
!pip install pandas fpdf
# Import libraries
import pandas as pd
from fpdf import FPDF
# Define the two strings
str1 = "AGGTA"
str2 = "GXTXAYB"
# Create a 2D table initialized with zeros
m = len(str1)
n = len(str2)
lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
# Fill the LCS table using Dynamic Programming approach
for i in range(1, m + 1):
 for j in range(1, n + 1):
 if str1[i - 1] == str2[j - 1]:
 lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
 else:
 lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
# Create a DataFrame to display the LCS table
df = pd.DataFrame(lcs_table, columns=[""] + list(str2), index=[""] + list(str1))
print("LCS Table:")
display(df)
# Reconstruct the LCS from the table
lcs = []
i, j = m, n
while i > 0 and j > 0:
 if str1[i - 1] == str2[j - 1]:
 lcs.append(str1[i - 1])
 i -= 1
 j -= 1
 elif lcs_table[i - 1][j] >= lcs_table[i][j - 1]:
 i -= 1
 else:
 j -= 1
# Reverse the LCS because we built it backwards
lcs = ''.join(reversed(lcs))
# Display results
print(f"Length of LCS is: {lcs_table[m][n]}")
print(f"The LCS is: {lcs}")