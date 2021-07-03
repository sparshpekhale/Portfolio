from requests import get
from bs4 import BeautifulSoup
from ..models import Project
from concurrent.futures import ThreadPoolExecutor

def get_projects():
    url = 'https://github.com/sparshpekhale?tab=repositories'
    soup = BeautifulSoup(get(url).content, 'html.parser')

    links = []

    for i in soup.findAll(class_= 'wb-break-all'):
        links.append('https://github.com' + i.find('a')['href'])

    return links

def get_project(url):
    # url = 'https://github.com/sparshpekhale/Steganography'

    soup = BeautifulSoup(get(url).content, 'html.parser')
    # title = soup.find('strong').find('a').contents[0]
    title = url.split('/')[-1]

    readme = soup.find(class_='Box-body px-5 pb-5')
    # del soup

    desc_short = readme.find('h2').contents[1]
    desc_long = readme.find('p').contents[0]
    image_link = readme.find('img')['src']

    return title, image_link, desc_short, desc_long

def save_project(url):
    soup = BeautifulSoup(get(url).content, 'html.parser')
    title = url.split('/')[-1]

    readme = soup.find(class_='Box-body px-5 pb-5')

    desc_short = readme.find('h2').contents[1]
    desc_long = readme.find('p').contents[0]
    image_link = readme.find('img')['src']

    try:
        title, image_link, desc_short, desc_long = get_project(url)
        Project(title=title, image_link=image_link, desc_short=desc_short, desc_long=desc_long).save()
        print('saved', url)
    except:
        print('passed', url)

def test(n):
    print('concurr'+n)

def scrape():
    Project.objects.all().delete()

    links = get_projects()
    for proj in links:
        try:
            title, image_link, desc_short, desc_long = get_project('https://github.com' + proj)
            Project(title=title, image_link=image_link, desc_short=desc_short, desc_long=desc_long).save()
        except:
            pass

    # links = get_projects()

    # with ThreadPoolExecutor() as executor:
    #     print('in exec')
    #     executor.map(save_project, links)

    # return Project.objects.all()