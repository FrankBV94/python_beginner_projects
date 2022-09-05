# collect email from user
# split the email using the @, the first part as the user name, the second part is gonna be saved as domain
# split domain using .,

from distutils import extension


def main():
    print("Welcom to the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (user, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: " + user)
    print("Domain: " + domain)
    print("Extension: " + extension)


while True:
    main()
