"""
Create a program that asks the user to enter ratings (out of 10)
for their favorite movies. The user also specifies first how many movies they will rate.
Calculate the average rating.

Hint: you need to find the sum of all ratings with a loop and then find the average from that sum.
"""
rating = 0
movies_for_rating = int(input("Enter the number of movies: "))
average_rating = 0
for i in range(movies_for_rating):
    rating += int(input("Please, enter a rating from 1 to 10: "))

average_rating = rating / movies_for_rating
print(average_rating)