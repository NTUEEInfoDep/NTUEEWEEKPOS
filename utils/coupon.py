import requests, json



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
            for coupon in data:
                ID = coupon["id"]
                attributes = coupon["attributes"]
                name = attributes["name"]
                code = attributes["code"]
                discount = attributes["discount"]
                redemptions = attributes["redemptions"]
                print(f'ID: {ID}, Name: {name:15} ,Code: {code:10}, Discount: {discount:5} $, Redemptions: {redemptions}')
            print("")
        
        elif response.status_code == 401:
            message = response.json()["message"]
            print("Action Failed: %s\n" % message)
        
        else:
            print("Action Failed: %s\n" % response.status_code)

    def add_coupon(self,):
        payload = {
            "name": "Test",
            "code": "test",
            "type": "F",
            "discount": 10,
            "redemptions": 0,
            "customer_redemptions": 0,
            "validity": "forever",
            "status": 1
        }
        
        response = requests.post(self.url, headers=self.headers, params=payload)
        
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.status_code)
            print("Action Failed: %s" % response.json()["message"])
            print("Error: %s" % response.json())

def main():
    api = API()
    api.show_coupons()
    api.add_coupon()


if __name__ == "__main__":
    main()
