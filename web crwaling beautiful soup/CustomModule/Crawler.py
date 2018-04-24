from bs4 import BeautifulSoup 
import requests
import pandas as pd
class Crawler:
    mylist=[]
    
    def __init__(self,url="https://www.uiu.ac.bd"):
        self.url=url
        
    
    def alllinks(self):
        
        
        try:
            self.req=requests.get(self.url)
            self.soup = BeautifulSoup(self.req.text, 'lxml')
            for self.url in self.soup.find_all("a"):
                 self.mylist.append(self.url.get("href"))
                 print(self.url.get("href"))
        except:
            print("invalid url")
        
        #self.url=url
#         self.req=requests.get(self.url)
#         self.soup = BeautifulSoup(self.req.text, 'lxml')
#         for self.url in self.soup.find_all("a"):
#              self.mylist.append(self.url.get("href"))
#              print(self.url.get("href"))

    def alllinksgenerator(self):
        try:
            self.req = requests.get(self.url)
            self.soup = BeautifulSoup(self.req.text, 'lxml')
            for self.url in self.soup.find_all("a"):
                self.mylist.append(self.url.get("href"))
                yield(self.url.get("href"))
        except:
            print("invalid url")

    def savetofile(self,name):
        #self.alllinks()
        self.alllinksgenerator()
        
        if len(self.mylist)>0:
            self.mydataframe={
            
            "alllinks":self.mylist
            
            }

            self.masud=pd.DataFrame(self.mydataframe)
            print(self.masud)
            self.masud.to_csv(name)
            
        else:
            print("empty list")
        
