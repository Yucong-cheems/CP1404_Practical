def main():
    emails_name = []
    email = input("Enter emails: ")
    while email != " ":
        name = get_name(email)
        check = input(f"Is your name {name}? (Y/N) ")
        if check != "Y" and check != " ":
            name = input("Name: ")
        emails_name[email] = name
        email = input("Enter emails: ")

    for email, name in emails_name.items():
        print(f"{name}({email})")


def get_name(email):
    part = prefix.split(".")
    name = " ".join(part).title()
    return name


main()
