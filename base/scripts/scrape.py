from bs4 import BeautifulSoup
from requests import get
from ..models import Project

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

def add_project(url, datetime):
    try:
        # add project
        t, i, s, l = get_project(url)

        Project(title=t, image_link=i, desc_short=s, desc_long=l, is_proper=True, datetime=datetime).save()
    except:
        # add project is_proper = False
        Project(title = url.split('/')[-1], is_proper=False).save()

def update_project(url, datetime):
    if Project.objects.get(title = url.split('/')[-1]).is_proper==False:
        return
        
    obj = Project.objects.get(title = url.split('/')[-1])
    if obj.datetime != datetime:
        # update db
        t, i, s, l = get_project(url)
        Project(id = obj.id, title=t, image_link=i, desc_short=s, desc_long=l, is_proper=True, datetime=datetime).save()

# get project endpoints
def checkgit():
    url = 'https://github.com/search?q=sparshpekhale+in%3Aname&type=Repositories'
    soup = BeautifulSoup(get(url).content, 'html.parser')

    for i in soup.findAll(class_ = 'mt-n1'):
        
        # if project exist in db:
        #     if project is proper and datetime not equal:
        #      update db
        # else:
        #  add project in db

        endpoint = '/' + i.find('a')['href'].split('/')[-1]
        url = 'https://github.com/sparshpekhale' + endpoint
        datetime = i.find('relative-time')['datetime']

        try:
            Project.objects.get(title = endpoint[1:])
            update_project(url, datetime)
            # print('try', url)
        except:
            add_project(url, datetime)
            # print('except', url)

# checkgit()