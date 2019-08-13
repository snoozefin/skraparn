import requests # For http requests
import re       # For regexp

class Skraparn:
    def __init__(self):
        #Constructor
        self.content = dict() #Contains all fetched html

    def get(self, urls):
        #Visit sites and get content

        for url in urls:
            _url = "https://" + url
            print("opening: " + _url)
            #Perhaps set user agent
            self.content[url] = requests.get(_url, timeout=2.0)
            
            print("opened {} with code: {}\n".format(_url, self.content[url].status_code))

    def filter(self, url):
        #Regexp to filter content from self.content[url]

        exp = re.compile()
        match = exp.search(self.content.text)

    def filter_all(self):
        #Regexp to filter content from all urls in self.content
        exp = re.compile()
        match = exp.search(self.content.text)

    def get_text(self, url):
        #Returns HTML
        return self.content[url].text


print("\nSkraparn 3000\n\n")

#List of urls to visit
urls = ["www.expressen.se", "www.aftonbladet.se"]
#Create new Skraparn object
sk = Skraparn()
#Get content of urls
sk.get(urls)
#Print content
#print(sk.get_text("www.expressen.se"))