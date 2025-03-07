def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0
    if "," in numbers_str:
        numbers = numbers_str.split(",")
        return int(numbers[0]) + int(numbers[1])
    return int(numbers_str)