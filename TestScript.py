from RealEstateAnalysis.data import DataCsv
from decimal import Decimal, getcontext

path = "/Users/cbremer/Projects/TensorFlow/RealEstateAnalysis/RealEstateAnalysis/EBR_Building_Permits.csv"
getcontext().prec = 2

def parseGeo(coords):
    parsed = coords.split("\n")[-1].replace("(", "").replace(")", "").split(",")
    if len(parsed) == 2:
        return [float(p) for p in parsed]
    else:
        return None


def parseMoney(money):
    return Decimal(money.replace("$", ""))
    
data = DataCsv.new(path, encoding="latin-1").process(geolocation=parseGeo, project_value=parseMoney).load()
              
sample = data.sample(4*len(data) //5 )
export = sample.export(['geolocation', 'project_value'])
count = 0
for item in export:
    if item[0] is not None and (item[0][0] != 0 or item[0][1] != 0) and item[1]>0:
        count += 1
        print(item)
print("Count is {0}".format(count))
