age_of_user = int(input("What is your age? "))
time_of_movie = int(input("What is your time of movie? "))
price_ticket = 30
discount = 0.0

if age_of_user < 12 or age_of_user >= 65 or time_of_movie <= 10:
    discount = 30 * 0.20
    price_ticket -= discount
    print(price_ticket)

else:
    print(price_ticket)