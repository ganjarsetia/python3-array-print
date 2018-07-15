# from pprint import pprint


def process_page(start, end):
    if end < 4:
        return False

    output_data = []
    for x in range(start, end + 1):
        output_data.append(x)
        print(str(x - 1) + " = " + str(output_data[x - 1]))
        if x % 4 == 0:
            temp = output_data[x - 3]
            output_data[x - 3] = output_data[x - 2]
            output_data[x - 2] = output_data[x - 1]
            output_data[x - 1] = temp

    return output_data


if __name__ == '__main__':
    from sys import argv
    start = argv[1]
    end = argv[2]
    print(start + ' ' + end)
    # myList = ', '.join(map(str, out))
