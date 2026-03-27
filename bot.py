import pywikibot
import os

def run_purge():
    site = pywikibot.Site()
    
    password = os.environ.get('PYWIKIBOT_PASSWORD')
    site.login(password=password)

    page = pywikibot.Page(site, "Main Page")
    page.purge()

if __name__ == "__main__":
    run_purge()
