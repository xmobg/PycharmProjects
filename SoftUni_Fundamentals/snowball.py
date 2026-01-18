number_of_snowballs = int(input())
max_weight_snowball = 0
max_time_snowball = 0
max_quality_snowball = 0
max_value_snowball = 0
for i in range(number_of_snowballs):
    weight_of_snowball = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (weight_of_snowball // snowball_time) ** snowball_quality
    if max_value_snowball < snowball_value:
        max_value_snowball = snowball_value
        max_weight_snowball = weight_of_snowball
        max_time_snowball = snowball_time
        max_quality_snowball = snowball_quality
print(f"{max_weight_snowball} : {max_time_snowball} = {max_value_snowball} ({max_quality_snowball})")
