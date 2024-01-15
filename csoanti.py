from ast import Pass
import requests
import json
from AntiB import AntiB

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"  
urlEnd =       "/JSON-stat/2.0/en" 

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset):   
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file=fp)
  

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {}

    print("Length of sizes:", len(sizes))
    
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}
        
        print(label0)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            #print("\t",label1)
            result[label0][label1]={}
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                #print("\t\t",label2)
                result[label0][label1][label2]={}

                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    #print("\t\t",label3)
                    result[label0][label1][label2][label3]={}
           
                    for dim4 in range(0, sizes[4]):
                        currentId = ids[4]
                        index = dimensions[currentId]["category"]["index"][dim4]
                        label4 = dimensions[currentId]["category"]["label"][index]
                        #print("\t\t\t",label4, " ", values[valuecount])
                        result[label0][label1][label2][label3][label4]= {}

                        for dim5 in range(0, sizes[5]):
                            currentId = ids[5]
                            index = dimensions[currentId]["category"]["index"][dim5]
                            label5 = dimensions[currentId]["category"]["label"][index]
                            #print("\t\t\t",label4, " ", values[valuecount])
                            result[label0][label1][label2][label3][label4][label5]= {}

                            for dim6 in range(0, sizes[6]):
                                currentId = ids[6]
                                index = dimensions[currentId]["category"]["index"][dim6]
                                label6 = dimensions[currentId]["category"]["label"][index]
                                #print("\t\t\t",label4, " ", values[valuecount])
                                result[label0][label1][label2][label3][label4][label5][label6]= int(values[valuecount])
                        
                        db_values = (label1, label2, label3, label4, label5, label6, int(values[valuecount]) )
                        AntiB.create(db_values)
                        
                        valuecount+=1

        
    return result
    


if __name__ == "__main__":
    #getAllAsFile("FP001")
    getFormattedAsFile("DHA40")


##https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/DHA40/JSON-stat/2.0/en








##https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/HSPAE143/JSON-stat/2.0/en