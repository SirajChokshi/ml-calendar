import random

# Constants

# Rows of data 
ROWS = 100
# Detail of time derived from amount in an hour
# e.g. 3600 -> seconds, 60 -> minutes, etc
HOUR_COMPLEXITY = 3600

# write or overwrite existing data.csv file
f = open("data.csv", 'w')

# write header
f.write('start,end,val')

i = 0
while i < ROWS:
    out = ""
    length = random.randint(1, 3) * HOUR_COMPLEXITY
    start = random.randint(4, 20) * HOUR_COMPLEXITY
    end = start + random.randint(1, 4) * HOUR_COMPLEXITY
    # throw out iterations of bad lengths
    if end - length > start:
        # write valid row into file
        event = random.randint(start, end - length)
        out = f"{start},{end},{event}\n"
        f.write(out)
        i += 1

f.close()