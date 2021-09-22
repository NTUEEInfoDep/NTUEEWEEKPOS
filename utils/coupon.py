import requests, json, string, secrets, argparse
from prettytable import PrettyTable

class API:
    def __init__(self):
        with open("./token.json", "r") as f:
            token = json.load(f)
        self.token = token["token"]
        self.url = "https://weekpos.ntuee.org/api/coupons"
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token,
        }
    
    def show_coupons(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            print("Request successful!")
            print("All coupon information is listed below:")
            data = response.json()["data"]
            
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Code", "Discount", "Redemptions", "Status", "Auto Apply"]
            
            for coupon in data:
                ID = coupon["id"]
                attributes = coupon["attributes"]
                name = attributes["name"]
                code = attributes["code"]
                discount = attributes["discount"]
                redemptions = attributes["redemptions"]  
                status = attributes["status"]
                auto_apply = attributes["auto_apply"]
                table.add_row([ID, name, code, discount, redemptions, status, auto_apply])
            print(table)
        elif response.status_code == 401:
            message = response.json()["message"]
            print("Action Failed: %s\n" % message)        
        else:
            print("Action Failed: %s\n" % response.status_code)

    def generate_code(self):
        alphabet = string.ascii_letters + string.digits
        code = ''.join(secrets.choice(alphabet) for i in range(6))  # for a 20-character password
        return code

    def add_coupons(self, args):
        [filename, n] = args

        with open(filename, 'r') as f:
            coupon_model = json.load(f)
        
        for i in range(int(n)):
            payload = coupon_model.copy()
            payload["code"] = self.generate_code()
            
            response = requests.post(self.url, headers=self.headers, params=payload)
            
            if response.status_code == 201:
                print("Request successful!")
                print(response.json()["data"])
            else:
                print(response.status_code)
                print("Action Failed: %s" % response.json()["message"])
                print("Error: %s" % response.json())
            print("")
def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--show", action="store_true",
                    help="show existing coupons")
    group.add_argument("--add", type=str, nargs=2,
                    help="add coupon with model json file")
    args = parser.parse_args()

    api = API()

    if args.show:
        api.show_coupons()
    elif args.add:
        api.add_coupons(args.add)

if __name__ == "__main__":
    main()
