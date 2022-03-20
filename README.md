# Scraping

## Voting_list_scrape 
    Voting_list of registered data
    This script/module scrapes data from nepal government 
    website:"https://election.gov.np/np/page/voter-list-db" 
    ,parse the data and save it to a json file.
    -----------------------------------------------
    eg:
    state = {'name':'Provision_1','no':1}
    district = {'name':'Sunsari','no':10}
    vcd_mun = {'name':'ईटहरी उपमहानगरपालिका','no':5092}  
        // vdc/mun name appears in the data so for better provide in nepali
    ward_no = [2]
        // can provide lists of ward

    \\Note: state no, ward no, district no & vcd_mun no can be found on the original site html file 

    >>>> Itahari_data = voting_list(state,district,vdc_mun,ward_no)  //Returns a list of dictionaries
    >>>> save('itahari_data',Itahari_data) // It save data to itahari_data.json file 
    
    OR ``can scrape multiple munipalities and save to a single file``
    
    >>>> kathmandu_metro_data = voting_list(state,district,vdc_mun,ward_no)
    >>>> save('Itahari_&_kathmandu_data',kathmandu_metro_data,Itahari_data)
            // It saves both itahari and ktm data 

## Annapurna_Scraper 
    It scrapes the posts on the given search_keyword parameter page by page
    Scrape up to arround 20 pages at a time for better perfomance.

    How to use:
    -- Create an instance of Annapurna_Scraper class
    -- While creating instance provide three parameters shown below
    -- Call Scrape() method with the instance
    -- This method returns data but if save_to_file=True then it also saves to 'scrape.json' 
        file on the current directory 
    
    >>>> s = Annapurna_Scraper(,page_no=5,search_keyword = 'चुनाव',save_to_file=True)
    >>>> data = s.Scrape()