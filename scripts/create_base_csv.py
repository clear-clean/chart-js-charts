import csv
import datetime as dt


YEAR = 2021
DEFAULT = 'null'
output = 'sonit-mdm-time-{}.csv'.format(YEAR)


if __name__ == "__main__":
    reader = [[kw, DEFAULT] for kw in range(1, 54)]

    writer = csv.writer(open(output, 'w'), delimiter=',')

    header = ['kw', 'ts', 'particles']
    writer.writerow(header)

    for row in reader:
        kw = int(row[0])
        wts = '{year}-W{kw:02d}-1'.format(year=YEAR, kw=kw)
        ts = dt.datetime.strptime(wts, '%Y-W%W-%w')
        particles = row[1]
        writer.writerow([str(kw), str(ts), particles])
