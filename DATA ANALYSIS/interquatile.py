n = int(input().strip())
values = list(map(int, input().rstrip().split()))
freqs = list(map(int, input().rstrip().split()))

size = sum(freqs)
values,freqs = zip(*sorted(zip(values,freqs))) # Sorting pairs
count = int(size/4);
for i in range(n) :
    count -= freqs[i]
    if count <= 0:
        if count<0:
            Q1 = values[i]
        elif  size%4>1:
            Q1 = values[i+1]
        else:
            Q1 = (values[i]+values[i+1])/2 # Quartile is between elements
        break;
    
count = int(size/4);
for i in range(n) :
    count -= freqs[-1-i]
    if count <= 0:
        if count<0:
            Q3 = values[-1-i] 
        elif size%4>1:
            Q3 = values[-1-i-1] 
        else:
            Q3 = (values[-1-i]+values[-1-i-1])/2 # Quartile is between elements
        break;
print("{result:.1f}".format(result=Q3-Q1))