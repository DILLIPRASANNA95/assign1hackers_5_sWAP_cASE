str = "HackerRank.com presents 'Pythonist 2'"
str.islower()


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
def swap_case(s):
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)