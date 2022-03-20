import json
import requests
from bs4 import BeautifulSoup

# ''' Method 1. List of Dictionaries '''
# def voting_list(state,ward_no):
#     payload = {
#         'state':f'{state}',
#         'district':'26',
#         'vdc_mun':'5278',
#         'ward':f'{ward_no}',
#         'reg_centre':''
#             }
#     url = 'https://voterlist.election.gov.np/bbvrs/view_ward_1.php'
#     response = requests.post(url,data=payload)
#     soup = BeautifulSoup(response.text,"html.parser") 
#     div = soup.find('div',class_='div_bbvrs_data')
#     table = div.find("table")
#     head_table_data = ['voter_id','voter_name','age','gender','wife/husband_name','father/mother_name']
#     body_table_data = table.tbody.find_all("tr")  
#     list_data = []
#     for count in range(len(body_table_data)):
#         dict_data = {}
#         # for data in body_table_data[i].find_all("td"):
#         for i,th in enumerate(head_table_data):
#             dict_data[th[i]] = body_table_data[count].find_all("td")[i+1].get_text()   
#         list_data.append(dict_data)
#     string_list_data = str(list_data)
#     numbers_map = {'0': '०','1': '१','2': '२','3': '३','4': '४','5': '५','6': '६','7': '७','8': '८','9': '९'}
#     for eng_num,unicode in numbers_map.items():
#         string_list_data = string_list_data.replace(eng_num,unicode)
#     # bytestring = string_list_data.encode("utf-8")
#     # json_str = json.dumps(string_list_data,ensure_ascii=False).encode('utf8')
#     # with open(f'voting_list_wards{ward_no}.json','wb',encoding='utf8') as file:
#     #     file.write(bytestring)
#     with open(f'voting_list_wards{ward_no}.json','w',encoding='utf8') as file:
#         json.dump(string_list_data,file,ensure_ascii=False)


# state = {"प्रदेश १" : "1",
#     "मधेश प्रदेश" : "2",
#     "बागमती प्रदेश" : "3",
#     "गण्डकी प्रदेश" : "4",
#     "लुम्बिनी प्रदेश" : "5",
#     "कर्णाली प्रदेश" : "6",
#     "सुदूरपश्चिम प्रदेश" : "7"
#     }
# districts = {
#     '1': {"ईलाम" : "3",
#     "उदयपुर" : "14",
#     "ओखलढुङ्गा" : "13",
#     "खोटाङ" : "12",
#     "झापा" : "4",
#     "ताप्लेजुङ" : "1",
#     "तेह्रथुम" : "6",
#     "धनकुटा" : "8",
#     "पाँचथर" : "2",
#     "भोजपुर" : "7",
#     "मोरङ" : "9",
#     "संखुवासभा" : "5",
#     "सुनसरी" : "10",
#     "सोलुखुम्बु" : "11"
#     },
#     '2':
#     {
#     "धनुषा" : "20",
#     "पर्सा" : "34",
#     "बारा" : "33",
#     "महोत्तरी" : "21",
#     "रौतहट" : "32",
#     "सप्तरी" : "15",
#     "सर्लाही" : "22",
#     "सिराहा" : "16" 
#     },
#     '3':
#     {
#     "काठमाण्डौ" : "26",
#     "काभ्रेपलान्चोक" : "29",
#     "चितवन" : "35",
#     "दोलखा" : "17",
#     "धादीङ्ग" : "24",
#     "नुवाकोट" : "25",
#     "भक्तपुर" : "27",
#     "मकवानपुर" : "31",
#     "रसुवा" : "23",
#     "रामेछाप" : "18",
#     "ललीतपुर" : "28",
#     "सिन्धुपाल्चोक" : "30",
#     "सिन्धुली" : "19",
#     },
#     '4':
#     {
#     "कास्की" : "39",
#     "गोरखा" : "36",
#     "तनहुँ" : "40",
#     "नवलपरासी (बर्दघाट सुस्ता पूर्व)" : "45",
#     "पर्वत" : "51",
#     "बाग्लुङ" : "50",
#     "मनाङ्ग" : "37",
#     "मुस्ताङ्ग" : "48",
#     "म्याग्दी" : "49",
#     "लम्जुङ्ग" : "38",
#     "स्याङ्जा" : "41",
#     },
#     '5':
#     {
#     "अर्घाखाँची" : "44",
#     "कपिलवस्तु" : "47",
#    "गुल्मी" : "42",
#     "दाङ" : "56",
#     "नवलपरासी (बर्दघाट सुस्ता पश्चिम)" : "77",
#     "पाल्पा" : "43",
#     "प्युठान" : "54",
#     "बर्दिया" : "66",
#     "बाँके" : "65",
#     "रुकुम पूर्व" : "52",
#     "रुपन्देही" : "46",
#     "रोल्पा" : "53",
#     },
#     '6':
#     {
#     "कालिकोट" : "60",
#     "जाजरकोट" : "62",
#     "जुम्ला" : "59",
#     "डोल्पा" : "57",
#     "दैलेख" : "63",
#     "मुगु" : "58",
#     "रुकुम पश्चिम" : "76",
#     "सल्यान" : "55",
#     "सुर्खेत" : "64",
#     "हुम्ला" : "61",
#     },
#     '7':
#     {
#     "अछाम" : "68",
#     "कन्चनपुर" : "75",
#     "कैलाली" : "71",
#     "डडेलधुरा" : "74",
#     "डोटी" : "70",
#     "दार्चुला" : "72",
#     "बझाङ्ग" : "69",
#     "बाजुरा" : "67",
#     "बैतडी" : "73",
#     }
# }

# vdc_mun = {
#     'ईलाम' : {
#     "इलाम नगरपालिका" : "5018",
#     "चुलाचुली गाउँपालिका" : "5019",
#     "देउमाई नगरपालिका" : "5020",
#     "फाकफोकथुम गाउँपालिका" : "5021",
#     "माई नगरपालिका" : "5022",
#     "माईजोगमाई गाउँपालिका" : "5023",
#     "माङसेबुङ गाउँपालिका" : "5024",
#     "रोङ गाउँपालिका" : "5025",
#     "सन्दकपुर गाउँपालिका" : "5026",
#     "सूर्योदय नगरपालिका" : "5027",
#     }
# }


# def voting_list(state,district,vdc_mun,ward_no):
#     # state_name = state['name']
#     state_no = state['no']
#     # district_name = district['name']
#     district_no = district['no']
#     vdc_mun_name = vdc_mun['name']
#     vdc_mun_no = vdc_mun['no']
#     list_data = []
#     for ward in ward_no:
#         payload = {
#             'state':f'{state_no}',
#             'district':f'{district_no}',
#             'vdc_mun':f'{vdc_mun_no}',
#             'ward':f'{ward}',
#             'reg_centre':''
#                 }
#         url = 'https://voterlist.election.gov.np/bbvrs/view_ward_1.php'
#         response = requests.post(url,data=payload)
#         soup = BeautifulSoup(response.text,"html.parser") 
#         div = soup.find('div',class_='div_bbvrs_data')
#         table = div.find("table")
#         head_table_data = ['voter_id','voter_name','age','gender','spouse_name','parent_name','vdc_mun','ward']
#         body_table_data = table.tbody.find_all("tr")  
#         for count in range(len(body_table_data)):
#             dict_data = {}
#             for i,th in enumerate(head_table_data):
#                 if i <=5:
#                     dict_data[th] = body_table_data[count].find_all("td")[i+1].get_text()   
#                 elif i == 6:
#                     dict_data[th] = vdc_mun_name
#                 else:
#                     dict_data[th] = ward
#             list_data.append(dict_data)
#     string_list_data = str(list_data)
#     numbers_map = {'0': '०','1': '१','2': '२','3': '३','4': '४','5': '५','6': '६','7': '७','8': '८','9': '९'}
#     for eng_num,unicode in numbers_map.items():
#         string_list_data = string_list_data.replace(eng_num,unicode)
#     return list_data[1:-1]

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
        self.data = {}
        self.response_data = []
        self.file_data = []
        self.temp = {}
        
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
            data = response.json()['data']['items']
            self.temp['page_no'] = page
            self.temp['items'] = data
            
    def save_data(self):
        # self.data= self.file_data + self.response_data 
        # if self.save_to_file == True:
        #     if len(self.response_data) == 0:
        #         return self.file_data 
        #     with open('scrape.json','w') as f:
        #         print('Saving ...')
        #         json.dump(self.data,f)
        #     return self.data
        # else:
        #     return self.data
        with open('scrape.json','w') as f:
            json.dump(self.data,f)
        return self.data
    def Scrape(self):
        s_index = 0
        try:
            with open('scrape.json','r') as f:
                data_from_file = json.loads(f.read())
            file_flag = True
        except:
            file_flag = False
        for page in range(self.page_no):
            self.temp = {}
            if file_flag == True:  
                for key,value in data_from_file.items():
                    if value['page_no'] == page+1:
                        print(f'page {page+1} already found in the disk.....')
                        page_flag = True
                        break
                    else:
                        page_flag = False
                if page_flag == True:
                        continue
            self.fetch_data(page+1)
            self.data[f'search item {page+1}'] = self.temp
        return self.save_data()

scrape = Annapurna_Scraper(page_no=2,save_to_file=True)
data = scrape.Scrape() 