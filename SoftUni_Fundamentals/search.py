n = int(input())
word = input()
string = []

for i in range(n):
    current_string = input()
    string.append(current_string)

print(string)
filter_string = []
for str in string:
    if word in str:
        filter_string.append(str)
print(filter_string)
