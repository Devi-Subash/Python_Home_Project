def parse_numbers_list(numbers):
    ret = []
    if numbers is not None and numbers != '':
        numbers = numbers.replace(' ', ',')
        print("This is numbers", numbers)
        parts = [x.strip() for x in numbers.split(',')]
        print("This is parts", parts)
        for part in parts:
            if part == '':
                raise ValueError("Empty number part detected.")
            if '-' in part:
                start, end = part.split('-')
                for num in range(int(start), int(end) + 1):
                    ret.append(num)
            else:
                ret.append(int(part))
    return ret


print("The final output", parse_numbers_list("254 3-7,9"))
