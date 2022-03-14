from email.policy import default
import requests
import json

class Annapurna_Scraper:
    def __init__(self,page_no,search_keyword = 'चुनाव',save_to_file=True):
        self.search_keyword = search_keyword
        self.page_no = page_no
        self.save_to_file = save_to_file
        self.responses = []
        self.data = {}
        
    def fetch_data(self,search_key,page):
        url = f"https://bg.annapurnapost.com/api/search?title={search_key}&page={page}"
        header = {
            'authority': 'bg.annapurnapost.com',
            'content-type': 'application/json',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',

        }
        return requests.get(url,headers=header)
    
    def Scrape(self):
        try:
            for page in range(self.page_no):
                # self.responses.append(self.fetch_data(self.search_keyword,page+1))
                response = self.fetch_data(self.search_keyword,page+1)
                if response.status_code != 200 :
                    raise Exception('Connection error !!!')
                else:
                    data = response.json()['data']
                    self.data[page+1] = data 

            if self.save_to_file == True:
                with open('scrape.json','a') as f:
                    json.dump(data,f)
            else:    
                return self.data
        except Exception as e:
            print(e)


scrape = Annapurna_Scraper(page_no=1,save_to_file=False)
data = scrape.Scrape() 
print(data)           