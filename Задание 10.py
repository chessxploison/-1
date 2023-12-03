def read_from_file(filename):
    matrix = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split()
            if all(num.isdigit() for num in row):
                matrix.append([int(num) for num in row])
    return matrix

def write_to_file(filename, matrix):
    with open(filename, 'w', encoding='utf-8') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def sort(matrix):
    for row in matrix:
        row.sort()

input_filename = "/home/user/Сандракова_Дарья_Андреевна_У-234_vvod.txt"
output_filename = "/home/user/Сандракова_Дарья_Андреевна_У-234_vivod.txt"

matrix = read_from_file(input_filename)

sort(matrix)

write_to_file(output_filename, matrix)
