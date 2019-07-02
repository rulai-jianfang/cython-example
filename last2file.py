#!/usr/bin/python
import os

def main():
    dirname = '/tmp'
    allsize = []
    for (root,dirs,files) in os.walk(dirname):
        for filename in files:
            fullname  =  os.path.join(root,filename)
            filesize  =  os.path.getsize(fullname)
            allsize.append((filesize,fullname))
    allsize.sort()
    print allsize[-2:]


if __name__ == "__main__":
    main()
