stu={'john':86.5,'jack':91.2,'jill':84.54,'harry':72.1,'joe':80.5}
avgDict = {}
for k,v in stu.items():
    # v is the list of grades for student k
    avgDict[k] = sum(v)

    
