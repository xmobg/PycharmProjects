def check_employee_happiness(happiness_list,factor):
    improved_happiness = [current_value * factor for current_value in happiness_list]
    avrg_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(num >= avrg_happiness for num in happiness_list)
    total_count = len(happiness_list)
    massage = "happy" if happy_count >= total_count else "not happy"
    return f"Score: {happy_count}/{total_count}.Employees are {massage}"

happiness_list = list(map(int,input().split()))
happiness_factor = int(input())
result = check_employee_happiness(happiness_list,happiness_factor)
print(result)