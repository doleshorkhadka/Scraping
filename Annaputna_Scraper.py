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
        if not os.path.exists('annapurna-scrape'):
            os.mkdir("annapurna-scrape")
        with open(f'annapurna-scrape/{page}.json','w',encoding='utf8') as f:
            json.dump(data,f,ensure_ascii=False)
        return data

    def Scrape(self): 
        for page in range(1,self.page_no+1):
            try:
                with open(f'annapurna-scrape/{page}.json','r') as f:
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


'''This below method saves data of all the pages in one file'''
# class Annapurna_Scraper:
#     def __init__(self,page_no,search_keyword = 'चुनाव',save_to_file=True):
#         self.search_keyword = search_keyword
#         self.page_no = page_no
#         self.save_to_file = save_to_file
#         self.data = []
#         self.response_data = []
#         self.file_data = []
        
#     def request_data(self,page):
#         url = f"https://bg.annapurnapost.com/api/search?title={self.search_keyword}&page={page}"
#         header = {
#             'authority': 'bg.annapurnapost.com',
#             'content-type': 'application/json',
#             'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
#             'cache-control': 'no-cache',
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',

#         }
#         return requests.get(url,headers=header)
    
#     def fetch_data(self,page):
#         print(f'Downloading page {page+1}....')
#         response = self.request_data(page+1)
#         if response.status_code != 200 :
#             raise Exception('Connection error !!!')
#         else:
#             data = response.json()['data']['items']
#             data.append({'page' : page+1}) 
#             self.response_data = self.response_data + data
            
#     def save_data(self):
#         self.data= self.file_data + self.response_data 
#         if self.save_to_file == True:
#             if len(self.response_data) == 0:
#                 return self.file_data 
#             with open('scrape.json','w') as f:
#                 print('Saving ...')
#                 json.dump(self.data,f)
#             return self.data
#         else:
#             return self.data

#     def Scrape(self):
#         s_index = 0
#         try:
#             with open('scrape.json','r') as f:
#                 data_from_file = json.loads(f.read())
#             file_flag = True
#         except:
#             file_flag = False
#         for page in range(self.page_no):
#             if file_flag == True:  
#                 try:  
#                     for file in data_from_file:
#                         try:
#                             if (len(file) == 1 and file['page'] == page+1):
#                                 f_index = data_from_file.index(file)
#                                 print(f'page {page+1} already found in the disk.....')
#                                 self.file_data+=data_from_file[s_index:f_index+1]
#                                 s_index = f_index+1
#                                 page_flag = True
#                                 break
#                             else:
#                                 page_flag = False
#                         except:
#                             continue
#                     if page_flag == True:
#                         continue
#                 except Exception as e:
#                     print(e)
#             self.fetch_data(page)
#         return self.save_data()
