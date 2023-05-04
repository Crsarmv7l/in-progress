import os 
import time
import json
import subprocess

file = 'test.json'

def delete(i):
    with open( file, 'r') as fr:
        lines = fr.readlines()
        
        ptr = i
        
        with open(file, 'w') as fw:
            for line in lines:
                if not ptr == i:
                    fw.write(line)
                fw.close()

def main():
    #subprocess.Popen(['rtl_433', '-f', '433.92M', '-F', 'json:test.json'])
    subprocess.Popen(['rtl_433', '-f', '315.00Mhz', '-R', '60', '-R', '90', '-R', '89', '-R', '82', '-R', '110', '-F', 'json:test.json'])
    
    while True:
        if os.stat(file).st_size == 0:
            time.sleep (3)
            print("Waiting........")
        else:
                dataList = []
                with open(file) as f:
                    for jsonObj in f:
                        dataDict = json.loads(jsonObj)
                        dataList.append(dataDict)
            
                        for data in dataList:
                            n = len(dataList)
                            for i in range(n):
                                data = dataList[i]
                                if data["model"] == "PMV-107J":
                                    print("Got Toyota: %s" % data["id"])
                                    del dataList[i]
                                    delete(i)
                                    n = n - 1
                                elif data["model"] == "Citroen":
                                    print("Got Citroen: %s" % data["id"])
                                    del dataList[i]
                                    delete(i)
                                    n = n - 1
                                elif data["model"] == "Ford":
                                    print("Got Ford: %s" % data["id"])
                                    del dataList[i]
                                    delete(i)
                                    n = n - 1
                                elif data["model"] == "Renault":
                                    print("Got Renault: %s" % data["id"])
                                    del dataList[i]
                                    delete(i)
                                    n = n - 1
                                elif data["model"] == "Schrader-SMD3MA4":
                                    print("Got Schrader: %s" % data["id"])
                                    del dataList[i]
                                    delete(i)
                                    n = n - 1
                                else:
                                    print("Got Other")
                                    del dataList[i]
                                    delete(i)
                                    n = n-1
    
if __name__ == '__main__':
    main()