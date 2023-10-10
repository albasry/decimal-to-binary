def main():
    enter = int(input('Enter the Decimal Number: '))
    print(f'The Binary Number is: {convert(enter)}')

# TODO
def convert(decimal):
    binary = ''
    while decimal > 0:

        if decimal % 2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        decimal = int(decimal / 2)

    return binary

main()
