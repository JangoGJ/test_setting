from urllib.request import urlopen


class WebPage(object):
    def __init__(self,url):
        self.url=url
        self._content=None
    

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content=urlopen(self.url).read()
        return self._content
    


import time
webpage=WebPage("http://www.github.com/")
nowtime=time.time()
content01=webpage.content
t01=time.time()-nowtime
nowtime=time.time()
content02=webpage.content
t02=time.time()-nowtime
if content01==content02:
    x=1
else:
    x=0
print(t01,t02,x)


class AverageList(list):
    @property
    def average(self):
        result=sum(self)/len(self)
        return result


a=AverageList([1,2,3,4,5,6])
print(a.average)



import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace(object):
    def __init__(self,filename,search_string,replace_string):
        self.filename=filename
        self.search_string=search_string
        self.replace_string=replace_string
        self.temp_dictionary=Path("unzipped-{}".format(filename))


    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()


    def unzip_files(self):
        self.temp_dictionary.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_dictionary))
        

    def find_replace(self):
        for filename in self.temp_dictionary.iterdir():
            with filename.open() as file:
                contents=file.read()
            contents=contents.replace(self.search_string,self.replace_string)
            with filename.open('w') as file:
                flie.write(contents)
    

    def zip_files(self):
        with zipfile.ZipFile(self.filename,'w') as file:
            for filename in self.temp_dictionary.iterdir():
                file.write(str(filename),filename.name)
        shutil.rmtree(str(self.temp_dictionary))


if __name__=="__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()


