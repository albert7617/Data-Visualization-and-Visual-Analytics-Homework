import csv

cw = open('nuclear.csv', 'w', newline='', encoding='utf8')
csvWriter = csv.writer(cw)
csvWriter.writerow(['Country', 'Year', 'TWh'])
with open('nuclear_raw.csv', newline='', encoding='utf8') as c:
  cr = csv.reader(c, delimiter=',')
  header = next(cr)
  for row in cr:
    it = iter(row)
    country = next(it)
    for head, col in zip(header[1:], it):
      if not (col == 'n/a' or col == '-'):
        # print(country, head, 0.0 if col == 'n/a' or col == '-' else 0.05 if col == '^' else col) 
        csvWriter.writerow([country, head, 0.05 if col == '^' else col])
cw.close()