import sys
max_num = -sys.maxsize


while True:
   new_input = input()
   if new_input == "Stop":
       break

   number = int(new_input)
   if number > max_num:
       max_num = number

print(max_num)