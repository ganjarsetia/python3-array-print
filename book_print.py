from pprint import pprint


def process_page(start, end):
    if end < 4:
        return False

    input_number = []
    out = []
    for x in range(start, end + 1):
        input_number.append(x)

    for i, v in enumerate(input_number):
        j = i + 1
        if j % 4 == 0:
            out.append(input_number[j - 4])
            out.append(input_number[j - 2])
            out.append(input_number[j - 1])
            out.append(input_number[j - 3])

    return out


if __name__ == '__main__':
    from sys import argv
    start = argv[1]
    end = argv[2]
    print(start + ' ' + end)
    # myList = ', '.join(map(str, out))
