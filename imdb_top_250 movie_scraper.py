from bs4 import BeautifulSoup #imports beautifulsoup to scrap data
import requests #requests library for getting URL information
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250 '
resp = requests.get(url) #requests to url for obtaining information
soup = BeautifulSoup(resp.text,"html5lib")
lister_list = soup.find('tbody', {'class':'lister-list'}) #body section lies in the lister-list class in the URL
tr_section = lister_list.findAll('tr') #stores all information of "tr" section
for tr in tr_section:
    tr.find('td',{'class':'titleColumn'})
movies=[]
for tr in tr_section:
    title=tr.find('td',{'class':'titleColumn'}).text
    movies.append(title)
for name in movies:
    print(name)
