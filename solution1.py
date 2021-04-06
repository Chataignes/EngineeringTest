import os
import glob
import csv

resfile = "Combined.csv"

# Delete the result file if already exists in target directory
if os.path.exists(resfile):
    os.remove(resfile)
# Get only csv files from directory
files = glob.glob('*.csv')
# Use a list to track duplicate value
dup = []
with open(resfile, mode='w') as f:
    writer = csv.DictWriter(f, fieldnames=['Source IP', 'Environment'], lineterminator='\n')
    writer.writeheader()
    for file in files:
        # Get the filename without full path
        fn = os.path.splitext(os.path.basename(file))[0]
        key = ''.join(i for i in fn if not i.isdigit())
        # Read each file and write info to result file
        with open(file, 'r') as src:
            csv_reader = csv.reader(src)
            header = next(csv_reader)
            for row in csv_reader:
                ip = row[0]
                if ip not in dup:
                    writer.writerow({'Source IP': ip, 'Environment': key})
                    dup.append(ip)


