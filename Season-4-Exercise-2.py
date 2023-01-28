import requests
from bs4 import BeautifulSoup

r = requests.get('https://divar.ir/s/tehran')
soup = BeautifulSoup(r.text,'html.parser')
vals = soup.find_all('div' , attrs={'class' : 'post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46'})
for val in vals:
    val_info = str(val)
    soup = BeautifulSoup(val_info,'html.parser')
    val_descriptions = soup.find_all('div' , attrs={'class' : 'kt-post-card__description'})
    val_title = soup.find('h2')
    flag = False
    for val_desc in val_descriptions:
        val_text = str(val_desc.text).strip()
        if val_text == 'توافقی' or val_text == 'توافق' :
            flag = True
            break
    if flag == True:
        print(val_title.text)
