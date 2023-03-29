import requests
import csv
import json
from time import sleep
from random import randint
def parse_response(transaction,contract):
    record = {}
    record["collection"]=contract
    record["salesDateEST"]=transaction["salesDateEST"]
    record["price"]=transaction["dailySummary"]["summary"]["priceUSD"]
    record["avgPrice"]=transaction["dailySummary"]["summary"]["priceUSD"]/transaction["dailySummary"]["summary"]["totalTransactions"]

    return record
def a(url):
    result=list()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url,headers=headers)
    res = response.json()[0]
    for i in res["dailyAggregations"]:
        parsed = parse_response(i,res["contractName"])
        print(parsed)
        result.append(parsed)
    return result

def write_csv(data, filename):
    with open(filename, mode='w', encoding='utf-8', newline='\n') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = data[0].keys())

        writer.writeheader()
        for event in data:
            writer.writerow(event)

links = ["https://api2.cryptoslam.io/api/sales/Bored%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-05&_=1661199524899",
         "https://api2.cryptoslam.io/api/sales/Bored%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-07&_=1661199334074",
         "https://api2.cryptoslam.io/api/sales/Bored%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-06&_=1661199495409",
         "https://api2.cryptoslam.io/api/sales/Bored%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-04&_=1661199495409",
         "https://api2.cryptoslam.io/api/sales/Bored%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-08&_=1661199495409",

         "https://api2.cryptoslam.io/api/sales/CryptoPunks/summary?query%5Bmonth%5D=2022-07&_=1661199568333",
         "https://api2.cryptoslam.io/api/sales/CryptoPunks/summary?query%5Bmonth%5D=2022-06&_=1661199602789",
         "https://api2.cryptoslam.io/api/sales/CryptoPunks/summary?query%5Bmonth%5D=2022-05&_=1661199666835",
         "https://api2.cryptoslam.io/api/sales/CryptoPunks/summary?query%5Bmonth%5D=2022-04&_=1661199666835",
         "https://api2.cryptoslam.io/api/sales/CryptoPunks/summary?query%5Bmonth%5D=2022-08&_=1661199666835",

         "https://api2.cryptoslam.io/api/sales/Mutant%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-07&_=1661199707593",
         "https://api2.cryptoslam.io/api/sales/Mutant%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-06&_=1661199713238",
         "https://api2.cryptoslam.io/api/sales/Mutant%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-05&_=1661199716292",
         "https://api2.cryptoslam.io/api/sales/Mutant%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-04&_=1661199716292",
         "https://api2.cryptoslam.io/api/sales/Mutant%20Ape%20Yacht%20Club/summary?query%5Bmonth%5D=2022-08&_=1661199716292",


         "https://api2.cryptoslam.io/api/sales/Solana%20Monkey%20Business/summary?query%5Bmonth%5D=2022-07&_=1661199783442",
         "https://api2.cryptoslam.io/api/sales/Solana%20Monkey%20Business/summary?query%5Bmonth%5D=2022-06&_=1661199803754",
         "https://api2.cryptoslam.io/api/sales/Solana%20Monkey%20Business/summary?query%5Bmonth%5D=2022-05&_=1661199818163",
         "https://api2.cryptoslam.io/api/sales/Solana%20Monkey%20Business/summary?query%5Bmonth%5D=2022-04&_=1661199783442",
         "https://api2.cryptoslam.io/api/sales/Solana%20Monkey%20Business/summary?query%5Bmonth%5D=2022-08&_=1661199783442",


         "https://api2.cryptoslam.io/api/sales/Degenerate%20Ape%20Academy/summary?query%5Bmonth%5D=2022-07&_=1661199867039",
         "https://api2.cryptoslam.io/api/sales/Degenerate%20Ape%20Academy/summary?query%5Bmonth%5D=2022-06&_=1661199873338",
         "https://api2.cryptoslam.io/api/sales/Degenerate%20Ape%20Academy/summary?query%5Bmonth%5D=2022-05&_=1661199882066",
         "https://api2.cryptoslam.io/api/sales/Degenerate%20Ape%20Academy/summary?query%5Bmonth%5D=2022-04&_=1661199882066",
         "https://api2.cryptoslam.io/api/sales/Degenerate%20Ape%20Academy/summary?query%5Bmonth%5D=2022-08&_=1661199882066",


         "https://api2.cryptoslam.io/api/sales/Okay%20Bears/summary?query%5Bmonth%5D=2022-07&_=1661199954058",
         "https://api2.cryptoslam.io/api/sales/Okay%20Bears/summary?query%5Bmonth%5D=2022-06&_=1661199962283",
         "https://api2.cryptoslam.io/api/sales/Okay%20Bears/summary?query%5Bmonth%5D=2022-05&_=1661199967115",
         "https://api2.cryptoslam.io/api/sales/Okay%20Bears/summary?query%5Bmonth%5D=2022-04&_=1661199954058",
         "https://api2.cryptoslam.io/api/sales/Okay%20Bears/summary?query%5Bmonth%5D=2022-08&_=1661199954058",


         "https://api2.cryptoslam.io/api/sales/ZED%20RUN/summary?query%5Bmonth%5D=2022-07&_=1661200035093",
         "https://api2.cryptoslam.io/api/sales/ZED%20RUN/summary?query%5Bmonth%5D=2022-06&_=1661200060645",
         "https://api2.cryptoslam.io/api/sales/ZED%20RUN/summary?query%5Bmonth%5D=2022-05&_=1661200077013",
         "https://api2.cryptoslam.io/api/sales/ZED%20RUN/summary?query%5Bmonth%5D=2022-04&_=1661200035093",
         "https://api2.cryptoslam.io/api/sales/ZED%20RUN/summary?query%5Bmonth%5D=2022-08&_=1661200035093",

         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns/summary?query%5Bmonth%5D=2022-07&_=1661200121755",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns/summary?query%5Bmonth%5D=2022-06&_=1661200116250",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns/summary?query%5Bmonth%5D=2022-05&_=1661200126962,"
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns/summary?query%5Bmonth%5D=2022-04&_=1661200121755",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns/summary?query%5Bmonth%5D=2022-06&_=1661200121755",


         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns%20Shadowcorns/summary?query%5Bmonth%5D=2022-07&_=1661200179318",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns%20Shadowcorns/summary?query%5Bmonth%5D=2022-06&_=1661200183238",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns%20Shadowcorns/summary?query%5Bmonth%5D=2022-05&_=1661200187845",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns%20Shadowcorns/summary?query%5Bmonth%5D=2022-04&_=1661200179318",
         "https://api2.cryptoslam.io/api/sales/Crypto%20Unicorns%20Shadowcorns/summary?query%5Bmonth%5D=2022-08&_=1661200179318"]

temp= list()
for i in range(len(links)):
    print(i)
    result = a(links[i])
    temp=temp+result
    sleep(randint(1,3))
print(len(temp))


write_csv(temp, "data-test-db.csv")
