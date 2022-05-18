# https://leetcode.com/problems/valid-palindrome

word = input()

word_list = []
for c in word:
    if c.isalnum():
        word_list.append(c.lower())

length = len(word_list)
flag = True
for i in range(length // 2):
    if word_list[i] != word_list[length - i - 1]:
        flag = False
        
print(flag)

# 이렇게하면 거꾸로 string return
# print(word[::-1])