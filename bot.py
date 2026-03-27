import pywikibot
import os

def run_purge():
    site = pywikibot.Site('industrialist', 'miraheze')
    
    password = os.environ.get('PYWIKIBOT_PASSWORD')
    username = 'TRCDBot@TRCDBot_AutoPurge'
    
    site.login(user=username, password=password)
    
    if not site.logged_in():
        print("Error: Login failed, still acting as IP.")
        return

    # 3. Purge the page
    page = pywikibot.Page(site, "Main Page")
    if page.purge():
        print("Success: Page purged as logged-in user.")
    else:
        print("Failure: Purge failed.")

if __name__ == "__main__":
    run_purge()
