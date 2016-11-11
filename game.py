def get_input():
    a = raw_input("Enter a number: ")
    try:
        a = int(a)
    except ValueError:
        print "Invalid number. Please enter a correct number"
        a = get_input()
    return a

def check_if_number_is_less_than_5(number):
    if number < 5:
        print "%s is less than 5" % number
    elif number == 5:
        print "%s is equal to 5" % number
    else:
        print "%s is greater than 5" % number


def main():
    while True:
        number = get_input()
        check_if_number_is_less_than_5(number)
        a = raw_input("Do you want to continue (y/n): ")
        if a == 'y':
            continue
        else:
            print "exiting..."
            break

main()
