import csv, json, string

dataset = {}

countiesOrder = []
countiesDict = {'連江縣': 'Z',
  '宜蘭縣': 'G',
  '彰化縣': 'N',
  '南投縣': 'M',
  '雲林縣': 'P',
  '基隆市': 'C',
  '臺北市': 'A',
  '新北市': 'F',
  '臺中市': 'B',
  '臺南市': 'D',
  '桃園市': 'H',
  '苗栗縣': 'K',
  '嘉義市': 'I',
  '嘉義縣': 'Q',
  '金門縣': 'W',
  '高雄市': 'E',
  '臺東縣': 'V',
  '花蓮縣': 'U',
  '澎湖縣': 'X',
  '新竹市': 'O',
  '新竹縣': 'J',
  '屏東縣': 'T'}

with open('Dengue_Daily.csv', newline='', encoding='utf8') as c:
  cr = csv.reader(c, delimiter=',')
  next(cr)
  # Save coordinates data to JSON file
  for row in cr:
    if not row[0] in dataset:
      dataset[row[0]] = {}
      dataset[row[0]]['d'] = []
    if row[9] != 'None' and row[10] != 'None':
      dataset[row[0]]['d'].append((row[9], row[10]))

with open('T.csv', newline='', encoding='utf8') as c:
  cr = csv.reader(c, delimiter=',')
  header = next(cr)
  # Generate countries to character dictionary
  it = iter(header)
  next(it)
  for col in it:
    countiesOrder.append(countiesDict[col])
  # Save temperature data to JSON file
  for row in cr:
    if not row[0] in dataset:
      dataset[row[0]] = {}
    dataset[row[0]]['t'] = {}
    for field, val in zip(countiesOrder, row[1:]):
      if val != '-99':
        dataset[row[0]]['t'][field] = val
with open('Precp.csv', newline='', encoding='utf8') as c:
  cr = csv.reader(c, delimiter=',')
  next(cr)
  # Save temperature data to JSON file
  for row in cr:
    if not row[0] in dataset:
      dataset[row[0]] = {}
    dataset[row[0]]['p'] = {}
    for field, val in zip(countiesOrder, row[1:]):
      if val != '-99':
        dataset[row[0]]['p'][field] = val
output = {}
countiesID = {}
for key in countiesDict:
  countiesID[countiesDict[key]] = key
output['counties'] = countiesID
output['entries'] = []
for key in dataset:
  if 'd' in dataset[key]:
    output['entries'].append({
      'd': key,
      'c': dataset[key]['d'],
      't': dataset[key]['t'],
      'p': dataset[key]['p']
      })
  else:
    output['entries'].append({
      'd': key,
      't': dataset[key]['t'],
      'p': dataset[key]['p']
      })

#[["None", "None"]]
j = json.dumps(output, ensure_ascii=False)#.replace('[["None", "None"]]', '')
with open('dataset.json', 'w', encoding='utf8') as fp:
  fp.write(j)