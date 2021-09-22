import sys, getpass, requests


def generate_token(username, password, device_name=""):
    data = {
    'username': username,
    'password': password,
    'device_name': device_name
    }

    response = requests.post('https://weekpos.ntuee.org/api/token', data=data)

    if response.status_code == 201:
        print("Successfully acquired token! Saving ...")
        with open("./token.json", "w") as f:
            f.write(response.text)
        print("Successfully saved.")
        print("Now, you have access to other apis.")
    else:
        print("Action Failed!!! Please try again.")



def main():
    if sys.stdin.isatty():
        print("Enter credentials")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        device_name = input("中文姓名: ")
    else:
        username = sys.stdin.readline().rstrip()
        password = sys.stdin.readline().rstrip()
        device_name = sys.stdin.readline().rstrip()
    
    generate_token(username, password, device_name)


    

if __name__ == "__main__":
    main()