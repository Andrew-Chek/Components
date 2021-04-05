import requests
from bs4 import BeautifulSoup
value = input("Enter a path to web: ")
try:
    r = requests.get("https://{0}".format(value))
    if r.ok:
        page = BeautifulSoup(r.text, 'html.parser')
        images = page.findAll('img')
        links = page.findAll('a')
        word = input("Enter a word for checking: ")
        numberOfWords = 0
        text = page.body.text
        text = text.replace('|', '')
        text = text.replace('.', '')
        text = text.replace('-', '')
        text = text.replace('`', '')
        text = text.replace('"', '')
        text = text.replace('?', '')
        text = text.replace('!', '')
        text = text.replace(')', '')
        text = text.replace('(', '')
        text = text.replace(',', '')
        newText = text.replace(':', '')
        array = newText.split()
        for i in range(len(array)):
            if array[i] == word:
                numberOfWords += 1
        frequency1 = numberOfWords / len(array)
        print("Frequency of word {0} in text of news is {1}".format(word, frequency1))
        tag = input("Enter a tag for checking: ")
        numberOfTags = page.findAll('{0}'.format(tag))
        numberOfAllTags = page.findAll()
        frequency2 = len(numberOfTags) / len(numberOfAllTags)
        print("Frequency of tag {0} is {1}".format(tag, frequency2))
        print("Total number of images is {0}".format(len(images)))
        print("Total number of links is {0}".format(len(links)))
    else:
        print("url isn't correct")
except:
    print("url isn't correct")
