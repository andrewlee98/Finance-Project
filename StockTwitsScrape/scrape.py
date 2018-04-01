from selenium import webdriver
from html.parser import HTMLParser
import time


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


driver = webdriver.PhantomJS()
driver.get('https://stocktwits.com/symbol/ETH.X')

html = driver.page_source

parser = MyHTMLParser()
parser.feed(html)
