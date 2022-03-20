import json,os,requests

'''saves file in a folder on the basis of page.'''
class Annapurna_Scraper:
    '''
        Annapurna posts scraper: 
            It scrapes the posts on the given search_keyword parameter page by page
            Scrape up to arround 20 pages at a time; 
        
        How to use:
        -- Create an instance of Annapurna_Scraper class
        -- While creating instance provide three parameters shown below
        -- Call Scrape() method with the instance
        -- This method returns data but if save_to_file=True then it also saves to 'scrape.json' 
            file on the current directory 
        
        >>>> s = Annapurna_Scraper(,page_no=5,search_keyword = 'चुनाव',save_to_file=True)
        >>>> data = s.Scrape()
    '''
    def __init__(self,page_no,search_keyword = 'चुनाव',save_to_file=True):
        self.search_keyword = search_keyword
        self.page_no = page_no
        self.save_to_file = save_to_file
        self.response_data = []
        
    def request_data(self,page):
        url = f"https://bg.annapurnapost.com/api/search?title={self.search_keyword}&page={page}"
        header = {
            'authority': 'bg.annapurnapost.com',
            'content-type': 'application/json',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',

        }
        return requests.get(url,headers=header)
    
    def fetch_data(self,page):
        print(f'Downloading page {page}....')
        response = self.request_data(page)
        if response.status_code != 200 :
            raise Exception('Connection error !!!')
        else:
            return response.json()['data']['items']
            
    def save_data(self,data,page):
        print('saving...')
        if not os.path.exists(f'annapurna-scrape/{self.search_keyword}'):
            os.mkdir(f"annapurna-scrape/{self.search_keyword}")
        with open(f'annapurna-scrape/{self.search_keyword}/{page}.json','w',encoding='utf8') as f:
            json.dump(data,f,ensure_ascii=False)
        return data

    def Scrape(self): 
        for page in range(1,self.page_no+1):
            try:
                with open(f'annapurna-scrape/{self.search_keyword}/{page}.json','r') as f:
                    data_from_file = json.loads(f.read())
                file_flag = True
            except:
                file_flag = False
            
            if file_flag == True:
                if len(data_from_file) != 0 :
                    print(f'page {page} already found in the disk.....')
                    continue

            else:
                data = self.fetch_data(page)
                self.response_data.append(self.save_data(data,page))
                    
        if self.save_to_file == True:
            return None
        else:
            return self.response_data

scrape = Annapurna_Scraper(search_keyword='कांग्रेस',page_no=6,save_to_file=True)
data = scrape.Scrape() 