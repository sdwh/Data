import json
import requests
import clipboard

text = requests.get('https://raw.githubusercontent.com/sdwh/Data/master/Json/DSCS.json').text

data = json.loads(text)

def getFacet(facet):
    return min(control['構面編號'] for control in data if control['構面'] == facet).split('-')[0]

def getCategory(facet):
    return min(control['控制措施類別'] for control in data if control['構面'] == facet).split('-')[:2]

sorted(data, key = lambda x : x['構面編號'])

facets  = sorted(set([control['構面'] for control in data]), key = getFacet)


# 構面與分類摘要
if False:
    subDuplicates = []
    for f in facets:
        print(f'*{f}*')
        for sub in [sub for sub in data if sub['構面'] == f]:
            if sub['控制措施類別'] not in subDuplicates:
                count = len([c for c in data if c["控制措施類別"] == sub["控制措施類別"]])
                print(f'{sub["控制措施類別"]}, {count}')
                subDuplicates.append(sub['控制措施類別'])

# 卡片資訊
result = ""

for control in data:
    c = f"""<div class="sec-card">
  <div class="sec-card-head">
    <div class="sec-card-facet">{control['構面']}</div>
    <div class="sec-card-category">{control['控制措施類別']}</div>
    <div class="sec-card-index">{control['構面編號']}</div>
  </div>
  <div class="sec-card-content">{control['控制措施']}</div>
  <div class="sec-card-level">{control['等級']}</div>
</div>
"""
    result += c

clipboard.copy(result)
