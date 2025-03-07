def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0

    if "," not in numbers_str and "\n" not in numbers_str:
        return int(numbers_str)
    
    delimiter = ","
    if numbers_str.startswith("//"):
        delimiter, numbers_str = numbers_str.split("\n", 1)
        delimiter = delimiter[2:]
    
    numbers_str = numbers_str.replace("\n", delimiter)
    numbers = numbers_str.split(delimiter)
    return sum([int(number) for number in numbers if number != ""])
