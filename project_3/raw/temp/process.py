import csv

cw1 = open('nuclear.csv', 'w', newline='', encoding='utf8')
csvWriter1 = csv.writer(cw1)
csvWriter1.writerow(['Country', 'Year', 'TWh'])

cw2 = open('nuclear_delta.csv', 'w', newline='', encoding='utf8')
csvWriter2 = csv.writer(cw2)
csvWriter2.writerow(['Country', 'Year', 'Delta'])

with open('nuclear_raw.csv', newline='', encoding='utf8') as c:
  cr = csv.reader(c, delimiter=',')
  header = next(cr)
  for row in cr:
    it = iter(row)
    country = next(it)
    previous = 0.0
    for head, col in zip(header[1:], it):
      if not (col == 'n/a' or col == '-'):
        csvWriter1.writerow([country, head, 0.05 if col == '^' else col])
        if col == '^':
          floatCol = 0.05
        else:
          floatCol = float(col)
        if previous == 0:
          csvWriter2.writerow([country, int(head)+1, 'Infinity'])
        else:
          csvWriter2.writerow([country, int(head)+1, '%.3f' % (100*(floatCol-previous)/previous)])
        previous = floatCol
      if previous != 0 and (col == 'n/a' or col == '-'):
        csvWriter2.writerow([country, int(head)+1, '-100'])
        previous = 0
cw1.close()
cw2.close()