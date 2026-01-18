price_video_card = int(input())
price_prehodnik = int(input())
price_electric = float(input())
profit_video_card = float(input())

video_card_total_price = price_video_card * 13
prehodnik_total_price = price_prehodnik * 13
total_sum = video_card_total_price + prehodnik_total_price + 1000
profit = profit_video_card - price_electric
profit_sum = profit * 13
budget = total_sum / profit_sum
print(total_sum)
print(round(budget))