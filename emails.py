import requests

#This is an EMAIL FINDER
#Tested Website... SHOP.BANCOCN.COM

EMAILS = []
for i in range(36):
    #("http://shop.bancocn.com./rest/products/{}/reviews")
    # this {} was supposed to be number 1, but I put a range of 36 because that's the number of products it has,
    # so looking emails on all products
    response = requests.get("http://shop.bancocn.com./rest/products/{}/reviews".format(i))
    data_json = response.json()
    for review in data_json["data"]:
            email = review["author"]
            if email not in EMAILS:
                print(review["author"])
                EMAILS.append(email)
#HOW TO USE?
#on your Terminal:
#      python3 emails.py