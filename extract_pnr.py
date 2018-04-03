import re
f = open("final/test.txt","r")
data=f.read()
lines=data.split('\n')
f1=open("final/pnr.txt","w")
for line in lines:
    pnr_no=re.findall(r"\D(\d{10})\D", line)
    train_no=re.findall(r"\D(\d{5})\D", line)
    pnr=' '.join(pnr_no)
    train_no=' '.join(train_no)
    print(pnr_no)
    print(train_no)
    
    f1.write(pnr+',')
    #if not train_no:
   # for train in train_no:
    f1.write(train_no+',')
    f1.write('\n')

#data=data.replace('b\'','')
#data=data.replace('b\"','')
#data=data.replace('\'','')
#data=data.replace('\"','')
#data=data.replace('+','')
#data=data.replace('https:/.co','')
#data=data.replace('..','.')
#data=data.replace('  ',' ')
#data=data
#data=re.sub(r'[@,\\,/]\w+',"",data)


f.close()
f1.close()