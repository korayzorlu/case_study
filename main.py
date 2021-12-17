import json
import requests
import pandas as pd
from operator import itemgetter
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from google.oauth2 import service_account

#Get URL List
excelData = pd.read_excel(r"PATH_YOUR_URL'S_XLSX", header = None)
urlData = pd.DataFrame(excelData)

#Parse Links and Scrape
productList = []

for i in range(len(urlData)):
    url = "https://www.markastok.com" + urlData[0][i]
    response = requests.get(url).content
    soup = BeautifulSoup(response, "html.parser")

    if soup.find(id = "product-name"):
        print(url)
        #Product Name
        productTitle = soup.find(id = "product-name").text
        productName = productTitle.replace("\n", "")

        #Offer
        if soup.find("div", {"class":"detay-indirim"}):
            offer = soup.find("div", {"class":"detay-indirim"}).text.replace(" ", "")
        else:
            offer = ""

        #Product Price
        if soup.find("span", {"class":"currencyPrice"}):
            productPrice = soup.find("span", {"class":"currencyPrice"}).text
            for i, j in {"TL" : "",  "\n" : "", " " : ""}.items():
                productPrice = productPrice.replace(i, j)
        else:
            productPrice = ""

        #Sale Price
        if soup.find("span", {"class":"discountPrice"}):
            salePrice = soup.find("span", {"class":"discountPrice"}).text
            for i, j in {"TL" : "", "\n" : "", " " : ""}.items():
                salePrice = salePrice.replace(i, j)
        else:
            salePrice = ""

        #Availability
        if soup.find("div", {"class":"new-size-variant fl col-12 ease variantList"}):
            variants = soup.find("div", {"class":"new-size-variant fl col-12 ease variantList"}).find_all("a")
            availableSizes = []
            unavailableSizes = []

            for variant in variants:
                if variant.get("class") == ['col', 'box-border', 'passive']:
                    unavailableSizes.append(1)
                else:
                    availableSizes.append(1)

            availability = float(round(len(availableSizes)/len(variants)*100, 2))
        else:
            if soup.find("span", {"class":"discountPrice"}): #If the product in stock
                availability = 100.0
            else:
                availability = 0.0

        #Product Code
        productCodeContent = soup.find("div", {"class":"product-feature-content"})

        if productCodeContent.contents[-1] == "\n":
            productCode = productCodeContent.contents[-2].contents[-1].replace("\n", "")
        else:
            productCode = productCodeContent.contents[-1].replace("\n", "")

        #Add to Product List
        product = [url, productCode, productName, availability, offer, productPrice, salePrice]
        productList.append(product)

#Sort and edit list
productList = sorted(productList, key=itemgetter(3), reverse = True)
for x in productList:
    x[3] = str(x[3]) + "%"

#Share with Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = "PATH_YOUR_JSON"

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = "SPREADSHEET_ID"
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

body = {
    'values': productList
}

result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range='A2',
    valueInputOption="RAW", body=body).execute()