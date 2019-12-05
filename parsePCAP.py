from scapy.all import *
import os
import pickle


def getFeatureFromDump(filePath):
    try:
        scapy_cap = rdpcap(filePath)
    except :
        print filePath
        return

    src_address = scapy_cap[0][1].src
    dest_address = scapy_cap[0][1].dst
    featureList = []
    featureSize = 2000
    pktList = []
    for packet in scapy_cap:
        if packet[1].src == src_address:
            featureList.append(1)
        elif packet[1].src == dest_address:
            featureList.append(-1)
        elif packet[1].dst == dest_address:
            featureList.append(1)
        elif packet[1].src == dest_address:
            featureList.append(-1)

    if len(featureList) < featureSize:
        featureList.extend([0] * (featureSize - len(featureList)))
    elif len(featureList) > featureSize:
        featureList = featureList[:featureSize]
    return featureList

path='../../../crawldataset'
directories=next(os.walk(path))[1]
pathList=[]
for d in directories:
    if d !="logs":
        path1=path+"/"+d
    else:
        continue

    for d1 in next(os.walk(path1))[1]:
        path2 = path1 + "/" + d1
        for d2 in next(os.walk(path2))[1]:
            path3 = path2 + "/" + d2
            filepath=path3+"/"+next(os.walk(path3))[2][0]
            pathList.append(filepath)
training=[]
classes=[]
i=0
for path in pathList:
    i+=1

    featureVector=getFeatureFromDump(path)
    if featureVector is not None:
        training.append(featureVector)
        classes.append(path.split("_")[1])

    if i%100==0:
        print i

        with open('data/train'+str(i)+'.pkl', 'wb') as f:
            pickle.dump(training, f)
        with open('data/class'+str(i)+'.pkl', 'wb') as filehandle1:
            pickle.dump(classes, filehandle1)


print len(training)




