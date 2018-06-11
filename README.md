# Railway Complaints Classification

## **Abstract**
Railway complaint system is becoming better day by day. The number of complaints on social media platforms like Twitter, Facebook, etc. are increasing. The current system involves manual classification of complaint and assign it to certain department. We automated this hectic process using Machine Learning Techniques.

## Table of Contents

* [Team Members](#team-members)
* [Introduction](#introduction)

## <a name="team-members"></a>Team Members
* "Niraj Rajai" <https://github.com/NirajRajai>
* "Chinmay Patel" <https://github.com/CP-4>

## <a name="introduction"></a>Introduction

###Collecting Data
We used twitter api to collect tweets for 6-7 days. In total we collected around 20,000 tweets.
###Pre-processing Data
We removed unnecessary twitter handle mentions and hashtags. Due to encoding in UTF there certain special characters came in the format(/e00) so we filtered that also.
###Selecting Features
We used the top 300 words used in the tweets apart from common words i.e. is,the,etc.
###Training Model
We used Random Forest algorithm and it gave us an accuracy of around 88%. We are classfying each tweet into 10 categories namely food, cleanliness, security, etc.
###Fetching location of train/station
Based on current location of train we are forwarding the classified complaint to the respective official.
###App
Officials will recieve complaints forwarded to them on their app. They can close or forward that complaint.

