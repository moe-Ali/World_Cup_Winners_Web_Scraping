from bs4 import BeautifulSoup
import requests
import csv

url="https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"
results=requests.get(url)

soup= BeautifulSoup(results.text,"html.parser")
p_1=soup.find("table",class_="sortable")
p_2=p_1.find_all("tr")
        
with open("main.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in range(len(p_2)):
        if i in [23,24,25]:
            pass
        elif i==0:
            writer.writerow(["Year","Winner","Score"])
        else:
            year_end=str(p_2[i].find("th")).find("</a>")
            year_start=year_end-4
            year=str(p_2[i].find("th"))[year_start:year_end]
            
            country_end=str(p_2[i].find("td")).find("</a>")
            country_start=str(p_2[i].find("td")).find(">",80)+1
            country=str(p_2[i].find("td"))[country_start:country_end]
            
            score_start=str(p_2[i].find_all("td")[1]).find(">",50)+1
            score_end=str(p_2[i].find_all("td")[1]).find("</a>")
            score=str(p_2[i].find_all("td")[1])[score_start:score_end]
            writer.writerow([year,country,score])