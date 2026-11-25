
import loginLib


def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")
    return None


def showUserMenu() -> None:
    print("\nUser menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")
    return None


def AskChoice():
    choice = int(input("Your choice: "))
    return choice


def userMenu(User):
    while True:
        showUserMenu()
        choice = AskChoice()

        if choice == 0:
            print("Logging out...")
            break

        elif choice == 1:
            print(f"Profile ID {User[0]} - {User[1]}")

        elif choice == 2:
            newPassword = input("Insert new password: ")
            loginLib.change_password(User[1], newPassword)
            print("Password changed successfully!")

        else:
            print("Unknown option!")


def main():
    print("Program starting.")

    FirstTime = True

    while True:

        if not FirstTime:
            print()

        showOptions()
        FirstTime = False

        choice = AskChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            username = input("Insert username: ")
            password = input("Insert password: ")

            User = loginLib.viewProfile(username)

            if User is None or not loginLib.login(username, password):
                print("Authentication failed!")
            else:
                print("Authentication successful!")
                userMenu(User)

        elif choice == 2:
            username = input("Insert username: ")
            password = input("Insert password: ")

            loginLib.register(username, password)

            print("User registration completed!")

        else:
            print("Unknown option!")

    print("\nProgram ending.")


main()
