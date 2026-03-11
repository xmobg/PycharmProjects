def loading_bar(some_number:int) -> int:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_precents = some_number // 10
    loaded_dots = 10 - loaded_precents
    return f"{some_number}% [{'%' * loaded_precents}{'.' * loaded_dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))
