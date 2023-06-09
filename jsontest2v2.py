import os 
import time
import json

file = 'test.json'

def delete(n):
    with open( file, 'r') as fr:
        lines = fr.readlines()
        
        ptr = 1
        
        with open(file, 'w') as fw:
            for line in lines:
                if not ptr > n-1:
                    fw.write(line)
                ptr += 1
                fw.close()

def main():
    while True:
        if os.stat(file).st_size == 0:
            time.sleep (1)
        else:
                dataList = []
                with open(file) as f:
                    for jsonObj in f:
                        dataDict = json.loads(jsonObj)
                        dataList.append(dataDict)
            
                        for data in dataList:
                            i = 0
                            n = len(dataList)
                            delete(n)
                            while i < n:
                                data = dataList[i]
                                if data["model"] == "PMV-107J":
                                    print(data["id"])
                                    del dataList[i]
                                    n = n - 1
                                else:
                                    print("Got Citroen")
                                    del dataList[i]
                                    n = n-1
    
if __name__ == '__main__':
    main()