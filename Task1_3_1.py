from bs4 import BeautifulSoup
import json
import time
import tqdm

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 OPR/87.0.4390.25 (Edition Yx 05)',
    'Accept-Language':'ru',
    'Referer':'https://hh.ru/'    
}

data = {
    "data":[]
}
from requests_tor import RequestsTor
req = RequestsTor()

counter=0
for page in range(0,40):
    url = f"https://hh.ru/search/vacancy?text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&area=113&ored_clusters=true&enable_snippets=true&page={page}&hhtmFrom=vacancy_search_list"
    resp = req.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    for iter in tqdm.tqdm(tags):
        time.sleep(2)
        counter = counter + 1 
        url_object = iter.attrs["href"]
        resp_object = req.get(url_object, headers = headers)
        
        soup_object = BeautifulSoup(resp_object.text, "lxml")
        tag_experience = soup_object.find(attrs={"class":"vacancy-description-list-item"}).find(attrs={"data-qa":"vacancy-experience"})
        if tag_experience is None:
            tag_experience1 = "Требуемый опыт не указан"
        else:
            tag_experience1 = tag_experience.text
        
        tag_price = soup_object.find(attrs={"data-qa":"vacancy-salary"}).find(attrs={"data-qa":"vacancy-salary-compensation-type-net"})

        if tag_price is None:
            tag_price1 = "ЗП не указана"
        else:
            tag_price1 = tag_price.text
        
        tag_region = soup_object.find(attrs={"data-qa":"vacancy-view-location"})
        if tag_region is None:
            tag_regionraw = soup_object.find(attrs={"data-qa":"vacancy-view-link-location"}).find(attrs={"data-qa":"vacancy-view-raw-address"})
            if tag_regionraw is None:
                tag_region1 = "Регион не указан"
            else:
                tag_region1 = tag_regionraw.text
        else:
            tag_region1 = tag_region.text
        data["data"].append({"Counter":counter, "Title":iter.text, "Work experience":tag_experience1, "Salary":tag_price1, "Region":tag_region1})
        #print(counter, iter.text, tag_price1, tag_region1)
        with open("data_hh.json","w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)        