import csv

with open('GradesAll.csv') as infile:
    with open('GradesAllF.csv','w',newline='\n') as outfile:
        in_csv = csv.reader(infile)
        writer = csv.writer(outfile,delimiter=',')
        x,y,z = None,None,None
        for row in in_csv:
            a,b,c = row[0:3]
            if len(a) > 0:
                x = a
            if len(b) > 0:
                y = b
            if len(c) > 0:
                z = c
            row[0:3] = x,y,z
            print(row[0:3])
            writer.writerow(row)
