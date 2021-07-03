from requests import get
from .scrapeproject import get_commit
from .scrapegithub import get_projects
from ..models import Project

def check_changes():
    print(get_projects())