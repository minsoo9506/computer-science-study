# https://leetcode.com/problems/reverse-string/

# 투포인터
def reverse_str(str_list):
    left, right = 0, len(str_list) - 1 
    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
        
str_list = input(list(input()))
print(str_list)
reverse_str(str_list)
print(str_list)