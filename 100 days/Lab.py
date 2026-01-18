record_in_second = float(input())
distance_in_meters = float(input())
time_in_seconds_for_meter = float(input())
deley_in_second = (distance_in_meters // 15 ) * 12.5
swimming_record = (distance_in_meters * time_in_seconds_for_meter) + deley_in_second
if record_in_second > swimming_record:
    print(f"Yes, he succeeded! The new world record is {swimming_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {swimming_record - record_in_second:.2f} seconds slower.")