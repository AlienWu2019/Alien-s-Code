import  requests

url = "https://al.p2p.huya.com/huyalive/90001-2622305980-11262718424205230080-734400720-10057-A-0-1_440_0_66.slice?wsSecret=8fed9b7b869cf52929fd14acdf060e53&wsTime=5c9edac0&ex1=0&baseIndex=5539024527556497&wsRange=0,70&maxSeq=5539024527556623&maxSeqTime=10:59:53.094&timeStamp=2019-03-30_10:59:53.097&u=91779224136&t=100&sv=1903251456"
data= {
'Origin': 'https://www.huya.com',
'Referer': 'https://www.huya.com/kaerlol',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
req = requests.get(url,headers=data).content
print(req)