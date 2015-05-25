import urllib
import re
print "The URL crawler starts.."
myurl ="http://www.sliit.lk/"
x = 1
urlcontent = urllib.urlopen(myurl).read()
imgUrls = re.findall('img .*?src="(.*?)"',urlcontent)
for imgUrl in imgUrls:
    img = imgUrl
    print img
    urllib.urlretrieve(img,str(x)+".jpg")
    x= x + 1
