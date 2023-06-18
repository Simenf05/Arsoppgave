import os
import os.path
import hashlib
import sys
import math
import decimal
import time

files = os.listdir()

class Progressbar:
    def __init__(self, operations: int, width: int = 30, title: None | str = None) -> None:
        
        if operations < 0:
            raise TypeError("width cannot be less than zero")
        
        self.width = width if operations >= width else operations
        
        dec = decimal.Decimal(self.width / (operations + 1))
        
        self.stepSize = dec.quantize(decimal.Decimal('1e-28'), rounding="ROUND_FLOOR")
        self.place = 0
        self.lastplace = self.place - 1
        self.steps = 0
        
        if title:
            print(title)
        sys.stdout.write("[%s]" % (" " * self.width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.width + 1))
        
    def update(self):
        self.place += 1
        self.steps += self.stepSize
        
        if math.floor(self.steps) > self.lastplace:
            
            sys.stdout.write("-")
            sys.stdout.flush()
            self.lastplace = math.floor(self.steps)
    
    def done(self):
        sys.stdout.write("\n")



def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.digest()

def makeHexList(list):
    
    list = list
    hexlist = []
    
    bar = Progressbar(len(list), 50, "Making hex codes...")
    
    for item in list:
        if not os.path.isfile(item):
            bar.update()
            continue
        
        hexlist.append((item, md5(item)))
        bar.update()
    
    bar.done()
    return hexlist

def checkList(list):
    list = list
    theSame = []
    hexlist = makeHexList(list)
    
    bar = Progressbar(len(hexlist) // 2, 50, "Comparing hex codes...")
    
    for i, file1 in enumerate(hexlist):
        for j, file2 in enumerate(hexlist):
            if i == j:
                continue
            
            if file1[1] == file2[1]:
                theSame.append((file1[0], file2[0]))
                break
            
        hexlist.remove(file1)
        bar.update()
    bar.done()
    return theSame


starttime = time.time()
samefiles = checkList(files)
print(f"The search took {time.time() - starttime}!")
print("\nThese files were the same:")
print(samefiles)