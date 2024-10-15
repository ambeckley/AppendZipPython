#Aaron Beckley
#Oct 14 2024
#Python 3.12.7
#Append custom zip file data to end of image files python

import os
from zipfile import ZipFile
import io



zfile = "nasb.zip"
zipfile = io.open(zfile, "rb")
zipcontent = zipfile.read()
zipfile.close()



#For jpegs cause uses jpeg file end

filename = "test copy.jpg"
fio = io.open(filename, "rb")
removeEOF = fio.read()[:-1]
fio.close()
with open(filename, "wb") as f:  
    data = removeEOF + zipcontent + b'\xd9'
    f.write(data)


