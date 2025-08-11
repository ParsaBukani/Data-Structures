import sys

def longest_suffix(s1, s2):
    combined = s2 + s1
    n = len(combined)
    lps = [0] * n  
    i = 1
    length = 0
    
    while i < n:
        if combined[i] == combined[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps[-1]
 

input = sys.stdin.read
words = input().split()
n = int(words[0])
code = words[1]

for i in range(2, n + 1):
    overlap_len = longest_suffix(words[i-1], words[i])
    code += words[i][overlap_len:]

print(code)