def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0

    if "," not in numbers_str and "\n" not in numbers_str:
        if int(numbers_str) < 0:
            raise ValueError("negative numbers not allowed " + numbers_str)
        return int(numbers_str)
    
    delimiter = ","
    if numbers_str.startswith("//"):
        delimiter, numbers_str = numbers_str.split("\n", 1)
        delimiter = delimiter[2:]
    
    numbers_str = numbers_str.replace("\n", delimiter)
    numbers = numbers_str.split(delimiter)

    s = 0
    for number in numbers:
        if number == "":
            continue
        if int(number) < 0:
            raise ValueError("negative numbers not allowed " + number)
        s += int(number)

    return s