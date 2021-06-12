import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    url = f'https://in.indeed.com/jobs?q=python+developer&l=India&start={page}'
    res = requests.get(url)
    # return res.status_code
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


job_list = []


def transfrom(soup):
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')

    for i in divs:
        title = i.find('a').text.strip()
        print(title)
        company = i.find('span', class_='company').text.strip()
        print(company)
        summary = i.find(
            'div', class_='summary').text.strip().replace('\n', '')
        print(summary)

        job = {
            'title': title,
            "company": company,
            "summary": summary
        }
        job_list.append(job)


for i in range(0, 50, 10):
    print(f'Getting Page,{i}')

    c = extract(0)
    transfrom(c)

# print(len(job_list))

df = pd.DataFrame(job_list)
print(df.head())
df.to_csv('indeed.csv')
