import csv

def main():
    with open('user.txt', 'r') as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    user = input('Enter your username: ')
    for i in file:
        if i[0] == user:
            print('Username found.', user)
            user_found = [i[0], i[1]]
            pass_check(user_found)
            break
        else:
            print('Not found.')

def pass_check(user_found):
    user = input('Enter your password: ')
    if user_found[1] == user:
        print('Password match.')
    else:
        print('Incorrect password.')

main()