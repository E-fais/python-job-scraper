from bs4 import BeautifulSoup
import requests
import time
from web_url import url



requests.get(url) #it will give status code
html_text=requests.get(url).text
soup=BeautifulSoup(html_text,"lxml") #creating a soup instance


def scrape_jobs():
    jobs=soup.find_all('div',class_='jf-companycontent')
    # to get the index of the iteratiob ,enumerate is used.
    for index,job in enumerate(jobs): 
        category=job.find('a',class_='jf-fulltimejob').text.replace(' ','')
        apply_link=job.find('a',class_='jf-btnlike')['href'] #get only href from a tag
        if(category=='FullTime'): 
            title=job.find('h3').text
            company=job.find('span').text
            
            #write jobs in a new file
            with open(f'jobs/job{index}.txt','w') as file:
              file.write(f"Job : {title.strip()}\n")
              file.write(f"company : {company.strip()}\n")
              file.write(f'Apply link: {apply_link}')
            print(f'file saved {index}')
            
#run program at regular intervel of time
if __name__=='__main__':
     while True:
      scrape_jobs()
      time_interval=5
      print(f"scraper will reload after {time_interval} minutes")
      time.sleep(time_interval*60)
    
