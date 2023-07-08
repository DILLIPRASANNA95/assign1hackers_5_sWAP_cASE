# assign1hackers_5_sWAP_cASE
sWAP cASE
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
str = "HackerRank.com presents 'Pythonist 2'"
str.islower()

def swap_case(s):
    def swap(s):
        string = ""
        for i in s:
          if i.islower():
            i = i.upper()
            string+=i
          elif i.isupper():
            i=i.lower()
            string+=i
          else:
            string+=i
        return string
      
s="HackerRank.com presents 'Pythonist 2'"
swap(s)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    Input (stdin)
HackerRank.com presents "Pythonist 2".
Expected Output
hACKERrANK.COM PRESENTS "pYTHONIST 2".
