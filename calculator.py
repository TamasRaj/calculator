def add(numbers_str: str) -> int:
    if numbers_str == "":
        return 0
    
    if numbers_str.startswith("//"):
        delimiter, numbers_str = numbers_str.split("\n", 1)
        delimiter = delimiter[2:]
        numbers = numbers_str.split(delimiter)
        return sum([int(number) for number in numbers if number != ""])

    if "," in numbers_str or "\n" in numbers_str:
        numbers_str = numbers_str.replace("\n", ",")
        numbers = numbers_str.split(",")
        
        # Treat empty string to be 0 hence ignore
        return sum([int(number) for number in numbers if number != ""])

    return int(numbers_str)