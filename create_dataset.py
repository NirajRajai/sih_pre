import csv
f=open("medical.txt","r")
text=f.read()
words=['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','display']
header=['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','display','type']
lines=text.split("\n")
print(len(words))
f1=open("data_final.csv","a")

#f2=open("none.txt","w")
csvwriter = csv.writer(f1)
csvwriter.writerow(header)
i=0
for line in lines:
    row=[]
    flag=0
    for word in words:
        if word in line:
            row.append(1)
        else:
            row.append(0)
    row.append(11)
    i+=1
    csvwriter.writerow(row)
print(i)
f.close()
f1.close()