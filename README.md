# W8_5

Create program which can handle basic user registrations and logins. For this exercise, study the built-in library hashlib. The passwords must be hashed with md5 and hexdigested to a string format. It isn’t necessary to implement unique constraints on usernames as all of the usernames in the tests will be unique.

## Main menu options:
- Login
- Register
- Exit

## User menu options:
- View profile
- Change password (no need to implement)
- Logout

Use `credentials.txt` filename as place to store the credentials in CSV format. The filename can be defined as constant variable on the top-level of the library file. The value separator or delimiter must be a semicolon `;`.

Example `credentials.txt`:

```text
0;admin;58d613129c5e71de57ee3f44c5ce16bc