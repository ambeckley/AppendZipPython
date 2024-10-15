#Aaron Beckley
#Oct 14 2024
#Python 3.12.7
#extracting the content from jpegs
#zip file signature PK\x03\x04\x14\x00\x08

import os
import io

filename = "FileWithZip.jpg"
fio = io.open(filename, "rb")
filecontent = fio.read()
fio.close()

if b'PK\x03\x04\x14\x00\x08' in filecontent:
    print("File contains potential zip")
    bytesforzip = filecontent[filecontent.find(b'PK\x03\x04\x14\x00\x08'):]

    open('test.zip', 'wb').write(bytesforzip)
