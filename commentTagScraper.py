#!/usr/bin/python3 env

# Berkan ER
# https://github.com/erberkan/

# Prepared for use in test envoirements.
# Be careful for web site's Terms and Conditions before use this script to live website(s).


import sys

try:
    from bs4 import BeautifulSoup, Comment
except:
    print("[!] You will need to install BeautifulSoup")
    raise SystemExit

try:
    import urllib.request
except:
    print("[!] You will need to install urllib")
    raise SystemExit


def commentScan(x):
    soup = BeautifulSoup(urllib.request.urlopen(x), 'html.parser')
    # soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'lxml')
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))

    print("url: " + x)

    for c in comments:
        print("--> " + c.extract() + "\n")
        # print (type(comments))

def main():
    try:
        argv = sys.argv[1]
        commentScan("http://" + argv)
    except:
        print("--> Usage: python3 commentTagScraper.py <url> or <IP>\n")
        print("[*] Example: python3 commentTagScraper.py website.com")
        print("[*] Example: python3 commentTagScraper.py 127.0.0.1 ")


if __name__ == "__main__":
    main()
