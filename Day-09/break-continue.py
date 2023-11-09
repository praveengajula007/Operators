numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers :
    if i == 2:
        break
    print(i)

#numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers :
    if i == 2:
        continue
    print(i)

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)