import csv
filenames=['final/neg.txt','final/none.txt']
f1=open("final/nlptrainb.csv","a")
f3=open("final/nlptestb.csv","a")
words=['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filth','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac',' tt','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','display','awesome','stench','pungent','complaint','not working','booked','sleeper','provided','facility','pathetic','service','maintain','increase','catering','waste','dustbin','safety','corridors','unautho','locals','alcohol',' pet ',' foul ','odour','waiting room','retiring room','circuit','overcharge','sink','potty','overflow','lavatories','sanitizer','discomfort','window','closed','open','urinal','dumping','uncomfortable','unsuable','spoil','littered','blockage','blocked','washbasin','bedsheet','cushion','spider','repair','bathroom','fully','packed','completely','without','reservation','ticket','entered','introducing','new','commuters','space','entire','floor','dal','rice','roti','pantry','hungry','filled']
header=['labels','text']
csvwriter = csv.writer(f1)
csvwriter2 = csv.writer(f3)
category=['negative','positive']
print(len(category))
csvwriter.writerow(header)
csvwriter2.writerow(header)
j=0
#f2=open("none.txt","w")
for names in filenames:
    f=open(names,"r")
    text=f.read()
    lines=text.split("\n")
    #print(len(words))
    i=0
    print(j)
    print(names)
    print(category[j])
    for line in lines:
        row=[]
        flag=0
        row.append(category[j])
        row.append(line)
        i+=1
        if i%5==0:
            csvwriter2.writerow(row)
        else:
            csvwriter.writerow(row)
    j+=1
    f.close()
f1.close()
f3.close()