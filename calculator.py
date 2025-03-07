def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0

    if "," in numbers_str or "\n" in numbers_str:
        numbers_str = numbers_str.replace("\n", ",")
        numbers = numbers_str.split(",")
        
        # Treat empty string to be 0 hence ignore
        return sum([int(number) for number in numbers if number != ""])

    return int(numbers_str)