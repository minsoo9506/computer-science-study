# String
# string variable는 linear collection of letters
# and the letters have indexes

strTest = "Hello world"  # '', "" 둘 다 동일
print(strTest)
print(strTest[-1])  # 음수 indexing 가능
print(strTest + " " + "Korea!")  # 문자열 더하기
print(strTest*2)  # 문자열 곱하기
print("wo" in strTest)  # 특정 문자열이 있는가
print("wo" not in strTest)
