def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0
    if "," in numbers_str:
        numbers = numbers_str.split(",")
        return sum([int(number) for number in numbers])
    return int(numbers_str)