#BeautifulSoap -> Web scraping framework of Python
from bs4 import BeautifulSoup

#Requests-> HTTP library to send HTTP requests
import requests

#csv.writer class is used to insert data to the CSV file
from csv import writer


url= "https://www.msmemart.com/msme/listings/company-list/advertising-materials/90/1297/Supplier" #Our target URL

#The get() method sends a GET request to the specified url.
page = requests.get(url)

#Creating object of bs4 and parsing HTML
soup = BeautifulSoup(page.content, 'html.parser')

#Finds all <div> tags having class upl_box
lists = soup.find_all('div', class_="upl_box")

#For writing data in a CSV file
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f) #object of writer class
    header = ['Sr.No.', 'Name', 'Products/Services', 'Website',  'Address', 'Contact No']
    thewriter.writerow(header)
    sr=0 #Stores Sr. Number
    for list in lists:
        sr=sr+1
        name = list.find('a').text.replace('\n', '') #Finds first occurance of <a> tag in List (in our case name)
        paras = list.find_all('p')

        info = []
        for i in paras:
            info.append(i.text.replace('\n', ''))
        
        row_data = [sr,name,info]
        thewriter.writerow(row_data)

#Run this program and a CSV file will be generated.