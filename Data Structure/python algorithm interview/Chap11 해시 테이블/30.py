# 중복문자 없는 가장 긴 부분 문자열
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장한 문자면 start 갱신
        if char in used and start <= used[char]:
           start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)
        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length