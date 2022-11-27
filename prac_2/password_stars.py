
def main():
    password_input = get_password()
    print_stars(password_input)


def get_password():
    password = input("Enter your password: ")
    password_length = 8
    while len(password) < password_length:
        print("password error!")
        password = input(f"Enter your password with minimum {password_length} characters: ")
    return password


def print_stars(password_input):
    print(len(password_input) * '*')
    print("Thank you")

main()