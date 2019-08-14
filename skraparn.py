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

    def find_links(self):
        # Find all links in self.content
        links = set()
        exp = re.compile(r"(https://|http://|www\.).+?(\.se|\.com?=^,)")
        for cont in self.content.values():
            matchIter = exp.finditer(cont.text)
            for match in matchIter:
                links.add(match.group())
        print(*links, sep="\n")

    def get_text(self, url):
        #Returns HTML
        return self.content[url].text

    def count_occurence(self, substring):
        # Counts number of occurences of substring in content
        for key, value in self.content.items():
            print("{} was found {} times in {}".format(substring, value.text.count(substring), key))

print("\nSkraparn 3000\n\n")

#List of urls to visit
urls = ["www.expressen.se", "www.aftonbladet.se", "www.dn.se", "www.svt.se", "www.di.se"]
#Create new Skraparn object
sk = Skraparn()
#Get content of urls
sk.get(urls)
sk.count_occurence("Trump")
sk.find_links()
#Print content
#print(sk.get_text("www.expressen.se"))