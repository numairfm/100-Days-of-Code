import requests

head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0"
}

def get_billboard_data():
    response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/", headers=head)
    return response

def main():
    r = get_billboard_data()
    print(r.content)
    # date_to_travel_to = input("What year would you like to travel to? Input in this format YYYY-MM-DD: ")

if __name__ == "__main__":
    main()


# oh bruh you have to pay for access to the charts now
# cant do todays project