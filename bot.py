import pywikibot
import os
from pywikibot.login import ClientLoginManager

def run_purge():
    site = pywikibot.Site()
    password = os.environ.get('PYWIKIBOT_PASSWORD')
    
    manager = ClientLoginManager(site=site, password=password)
    manager.login()

    page = pywikibot.Page(site, "Main Page")
    if page.purge():
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    run_purge()
