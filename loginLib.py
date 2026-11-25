
import hashlib
import csv


CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hashPassword(PPassword: str) -> str:
    result = hashlib.md5(PPassword.encode())
    return result.hexdigest()


def readCredentials():
    Users = []

    try:
        file = open(CREDENTIALS_FILE, "r")
        reader = csv.reader(file, delimiter=DELIMITER)

        for Row in reader:
            if len(Row) == 3:
                Users.append(Row)

        file.close()

    except FileNotFoundError:
        pass

    return Users


def register(PUsername: str, PPassword: str) -> None:
    Users = readCredentials()

    UserID = len(Users)
    PasswordHash = hashPassword(PPassword)

    file = open(CREDENTIALS_FILE, "a", newline="")
    writer = csv.writer(file, delimiter=DELIMITER)

    writer.writerow([UserID, PUsername, PasswordHash])

    file.close()
    return None


def login(PUsername: str, PPassword: str):
    Users = readCredentials()
    PasswordHash = hashPassword(PPassword)

    for User in Users:
        if User[1] == PUsername and User[2] == PasswordHash:
            return True

    return False


def viewProfile(PUsername: str):
    Users = readCredentials()

    for User in Users:
        if User[1] == PUsername:
            return User

    return None


def change_password(PUsername: str, PNewPassword: str) -> None:
    Users = readCredentials()

    file = open(CREDENTIALS_FILE, "w", newline="")
    writer = csv.writer(file, delimiter=DELIMITER)

    for User in Users:
        if User[1] == PUsername:
            User[2] = hashPassword(PNewPassword)

        writer.writerow(User)

    file.close()
    return None
