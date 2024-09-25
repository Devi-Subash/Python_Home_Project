def parse_numbers_list(numbers):
    ret = []
    if numbers is not None and numbers != '':
        numbers = numbers.replace(' ', ',')
        parts = [x.strip() for x in numbers.split(',')]
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


