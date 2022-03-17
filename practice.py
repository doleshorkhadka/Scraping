import requests
import json
from bs4 import BeautifulSoup
# class Annapurna_Scraper:
#     '''
#         Annapurna posts scraper: 
#             It scrapes the posts on the given search_keyword parameter page by page
#             Scrape up to arround 20 pages at a time; 
        
#         How to use:
#         -- Create an instance of Annapurna_Scraper class
#         -- While creating instance provide three parameters shown below
#         -- Call Scrape() method with the instance
#         -- This method returns data but if save_to_file=True then it also saves to 'scrape.json' 
#             file on the current directory 
        
#         >>>> s = Annapurna_Scraper(,page_no=5,search_keyword = 'चुनाव',save_to_file=True)
#         >>>> data = s.Scrape()
#     '''
#     def __init__(self,page_no,search_keyword = 'चुनाव',save_to_file=True):
#         self.search_keyword = search_keyword
#         self.page_no = page_no
#         self.save_to_file = save_to_file
#         self.data = {}
#         self.response_data = []
#         self.file_data = []
#         self.temp = {}
        
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
#         print(f'Downloading page {page}....')
#         response = self.request_data(page)
#         if response.status_code != 200 :
#             raise Exception('Connection error !!!')
#         else:
#             data = response.json()['data']['items']
#             self.temp['page_no'] = page
#             self.temp['items'] = data
            
#     def save_data(self):
#         # self.data= self.file_data + self.response_data 
#         # if self.save_to_file == True:
#         #     if len(self.response_data) == 0:
#         #         return self.file_data 
#         #     with open('scrape.json','w') as f:
#         #         print('Saving ...')
#         #         json.dump(self.data,f)
#         #     return self.data
#         # else:
#         #     return self.data
#         with open('scrape.json','w') as f:
#             json.dump(self.data,f)
#         return self.data
#     def Scrape(self):
#         try:
#             with open('scrape.json','r') as f:
#                 data_from_file = json.loads(f.read())
#             file_flag = True
#         except:
#             file_flag = False
#         for page in range(self.page_no):
#             self.temp = {}
#             if file_flag == True:  
#                 for value in data_from_file.values():
#                     if value['page_no'] == page+1:
#                         print(f'page {page+1} already found in the file.....')
#                         self.file_data = 
#                         page_flag = True
#                         break
#                     else:
#                         page_flag = False
#                 if page_flag == True:
#                         continue
#             self.fetch_data(page+1)
#             self.data[f'search item {page+1}'] = self.temp
#         return self.save_data()


# scrape = Annapurna_Scraper(page_no=2,save_to_file=True)
# data = scrape.Scrape()

# def voting_list():
#     payload = {
#         'state':'3',
#         'district':'26',
#         'vdc_mun':'5278',
#         'ward':'1',
#         'reg_centre':''
#             }
#     url = 'https://voterlist.election.gov.np/bbvrs/view_ward_1.php'
#     response = requests.post(url,data=payload)
#     soup = BeautifulSoup(response.text,"html.parser") 
#     div = soup.find('div',class_='div_bbvrs_data')
#     table = div.find("table")
#     head_table_data = table.thead.find_all('th')
#     body_table_data = table.tbody.find_all("tr")  
#     data = {}
#     count = 0
#     # print(body_table_data[0].find_all("td"))
#     for th in head_table_data[:-1]:
#         value = []
#         for i in range(len(body_table_data)):
#             value.append(body_table_data[i].find_all("td")[count].get_text())
#         count+=1
#         data[th] = value
#     with open('voting_list.json','w') as f:
#         json.dump(data,f)

# voting_list()

def voting_list():
    payload = {
        'state':'3',
        'district':'26',
        'vdc_mun':'5278',
        'ward':'1',
        'reg_centre':''
            }
    url = 'https://voterlist.election.gov.np/bbvrs/view_ward_1.php'
    response = requests.post(url,data=payload)
    soup = BeautifulSoup(response.text,"html.parser") 
    div = soup.find('div',class_='div_bbvrs_data')
    table = div.find("table")
    head_table_data = table.thead.find_all('th')
    body_table_data = table.tbody.find_all("tr")  
    list_data = []
    count = 0
    for count in range(len(body_table_data)):
        dict_data = {}
        # for data in body_table_data[i].find_all("td"):
        for i,th in enumerate(head_table_data[:-1]):
            dict_data[th.get_text()] = body_table_data[count].find_all("td")[i].get_text()
            
        list_data.append(dict_data)
    
    # for th in head_table_data[:-1]:
    #     value = []
    #     for i in range(len(body_table_data)):
    #         value.append(body_table_data[i].find_all("td")[count].get_text())
    #     count+=1
    #     data[th] = value
    with open('voting_list.json','w') as f:
        json.dump(list_data,f)

voting_list()