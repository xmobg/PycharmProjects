words = input().split()
palindrome = input()
palindrome_test = [word for word in words if word == word[::-1]]
print(palindrome_test)
print(f"Found palindrome {palindrome_test.count(palindrome)} times")