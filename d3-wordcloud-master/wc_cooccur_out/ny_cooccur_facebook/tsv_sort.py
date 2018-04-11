from operator import itemgetter
import csv
reader = csv.reader(open("part-00000"), delimiter="\t")

f = open("sorted_data.tsv", "w")
f.write('%s\t%s\n'%("text", "size"))
for line in sorted(reader, key=lambda row: int(row[1]), reverse=True):
    f.write( '%s\t%s\n' %(line[0],line[1])  )      # str() converts to string
f.close()
    #print '%s\t%s' %(line[0],line[1])
