import os
import subprocess
import sys
import numpy as np 
import datetime 
from subprocess import STDOUT, check_call
import os 
from getOutScript import getOut


# subprocess.check_call(['apt', 'install', '-qq', 'enchant'], stdout=open(os.devnull,'wb'), stderr=STDOUT) 
# subprocess.check_call([sys.executable, "-m", "pip", "install", "pyenchant"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])

from github import Github
g = Github("")

# import enchant
# d = enchant.Dict("en_US")

def number_of_files(link):
    """
    ---------------------------
    Total Number of Files (TNF)
    ---------------------------
    The total amount of files within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_files().totalCount
        except:
            return None

    return action()