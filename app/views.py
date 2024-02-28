from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def filter_by_id_length(tag):
    return tag.name == 'tr' and len(tag.get('id', '')) == len('b5bb13d2-8a79-43a8-a538-ffd1e2e21009')

def scrap(request):
    url = 'https://rate.am/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    trs_with_matching_length = soup.find_all(filter_by_id_length)
    di=[]
    for num,tr in enumerate(trs_with_matching_length):
        columns = tr.find_all(['th', 'td'])
        n=''
        for col in columns:
            n+=col.text.strip()+','
        di.append(n)
    nextli=[]
    for i in di:
        nextli.append(i.split(','))
    return render(request, 'scrap.html',{'data':nextli})