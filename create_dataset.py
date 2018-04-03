import csv
f1=open("final/final_test.csv","a")

#filenames=['final/booking_n.txt','final/cleanliness_n.txt','final/no_water.txt','final/electricity.txt','final/late_n.txt','final/medical.txt','final/irctc_care.txt','final/security_n.txt','final/staff_n.txt','final/irctc_staff_n.txt']
#f3=open('final/new_features.txt','r')
#words_all=f3.read()
#words_l=words_all.split(',')
words=['name','handwash','napkin','provide','not','pregn','counter','higher',' veg ','serving',' serve ','confirmed','amount','headache','phone','drinking','physical','insulin','injection','diabe','receipt',' slip ','vomit','motion','accident','blood','suffering','tablet','crocin','condition','clean',' tea ','teasing','coffe','breakfast','cutlet','omlet','daal','concession','milk','sugar','announce','taste','salty','price','wrong','enquiry','queue','mismatch','danger','forcefully','fighting','unfair','rude','bribe','clerk','shop','stall','divyang',' loco ',' authorized','officials','corrupt','staff','bully','immediate',' old ',' aged ',' rpf ','police','harassment','lost','forgot','troubling','harassed','drunk','alcohol','attack','stolen','theft','force','molest','robbery','badgering','unwanted','rude','behaviour','crime','loot','illegal','abuse','used',' wet ','assault','harm','money','refund','email','mistake','medical','emergency','heart','critical','doctor','bleeding', ' ill','medicine','train','fever','fatigue','late','delay','hrs','hour','food','eat','unhyg','irctc','meal','bad quality','arriv','speed','time','electri','chart','prepared','cooked','cooling','boggie','bogie','repair','laptop','mobile','switch',' air ','sold','selling',' rate','rail neer','conditioners','sweating','temperature','facility','charging','soap','socket','fan','light','parcel','overpacked','packed','no space','assistance','emergency','heart','fever','fatigue','booking','cancellation','action','allocated','toilet','dirty','filth','cleanliness','smell','stink',' pnr ',' allot ','tatkal','clogged','choke','garbage','not clean','leakage',' bug','insects','spray','bitten','cockroach','no water','seat','berth',' ac ',' tt ','ticket','broken',' torn','checker',' tc ','blanket',' tte ',' charge ','overcharge','overcharging','disgusting',' coach','more','extra',' fare ','selling','deducted',' id ',' rs ',' fine ','serious','authority','bottle','vendor','broken','vacant','allocation',' rat','jammed','senior','citizen','lower','black money','reserved','strict action','rpf','boarded','local','commuter','blocking','remove','group','missing','unsafe','not safe','safety','threatning','misbehaving','abusing','violence','unauthorized','horrible','unhealthy','passenger','issue','pillow','sick','occupied','display','stench','pungent','not working','misguide','booked','sleeper','pathetic','service','lunch','dinner','roti','paneer','pantry',' dal ','fried','maintain','catering','waste','dustbin','unautho','locals','alcohol',' pet ',' foul ','waitlist','odour','waiting list',' wl ',' id ','waiting room','retiring room','circuit','overcharge','sink','potty','overflow','lavatories','sanitary','sanitizer','urinal','unsuable','spoil','littered','blockage','blocked','washbasin',' bed',' roll ','cushion','hygie','high','bought','demanded','bribe','status','station master','pain','chest','stomach','no water','unauthorized passenger','senior citizen','lower berth','upper berth','upper','choice','detail','cancellation charge','penalty',' rac ','penalise','website','sitting','app','online','process','wallet','unsuccess','debit','credit','paytm','payment',' upi ','server','down','transaction','tatkal','charging socket','charging point','no electricity','unhygienic food','tasteless','food quality','worst food','bad quality','charger socket','unauthorized passenger','unreserved passenger']
#phrase=['unauthorized passenger','unreserved passenger','charging socket','charging point','no electricity','unhygienic food','tasteless','food quality','worst food','bad quality','not working','charger socket','medical assistance','cancellation charge','no space']
#imp_words=['bribe','corrupt',' tte ',' tc ','drunk','alcohol','stolen','lost',' ill ','fever','fatigue','late','delay','booking','electricity','irctc','food',' fan ',' light ','medical','meal','toilet','dirty','filth','stink','smell','overcharging','vendor','catering','socket',' fan ',' light ']
    #for wrd in words_l:
 #   words.append(wrd)
print(len(words))
filenames=['C:/Users/niraj/Downloads/optimus-master/optimus-master/tweet.txt']
i=1
for name in filenames:

    f=open(name,"r")
    text=f.read()
       #header=['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','display','type']
    lines=text.split("\n")
    print(len(words))


    #f2=open("none.txt","w")
    csvwriter = csv.writer(f1)
    #csvwriter.writerow(header)
    print(name)
    for line in lines:
        row=[]
        flag=0
        for word in words:
            if word in line:
                #if word in phrase:
                row.append(1)
#                 elif word in imp_words:
#                     row.append(0.5)
#                 else:
#                     row.append(0.2)
            else:
                row.append(0)
        #row.append(i)

        csvwriter.writerow(row)

    print(i)
    i+=1
    f.close()
f1.close()