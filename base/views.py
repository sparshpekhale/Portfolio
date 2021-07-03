import os
from django.shortcuts import render
from django.http import HttpResponse, Http404, FileResponse
from .models import Project
# from .scripts.scrapeproject import get_project
# from .scripts.scrapegithub import get_projects, scrape
from .scripts.scrape import checkgit

# Create your views here.
def get_context_home():
    checkgit()
    context = {
        'projects': Project.objects.filter(is_proper = True).order_by('?')[:4]
    }
    return context

def home(req):
    return render(req, 'base/home.html', context=get_context_home())

def contact(req):
    return render(req, 'base/contact.html')

# class Projectt:
#     def __init__(self, id, text) -> None:
#         self.id = id
#         self.text = text

def get_context():
    # title, image_link, desc_short, desc_long = get_project('https://github.com/sparshpekhale/Steganography')
    # Project(title=title, image_link=image_link, desc_short=desc_short, desc_long=desc_long).save()
    
    # check_changes()
    # scrape()
    # Project.objects.all().delete()
    checkgit()
    context = {
        'projects': Project.objects.filter(is_proper = True)
        # 'projects': scrape()
    }
    # context['projects'].extend([Projectt(i, 'description '+str(i)) for i in range(1, 4)])
    return context

def projects(req):
    return render(req, 'base/projects.html', context=get_context())

def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404