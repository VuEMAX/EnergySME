
import matplotlib.pyplot as plt
import collections
from collections import defaultdict
datad= defaultdict(lambda : None)


line1=[]


#read file and store in line1; line1 is of length 5 and contains date, month, year, startdate, power in this order

with open('data1.csv') as o:
	for line3 in o:
		if 'Local' not in line3 and 'A+' in line3:
			line=line3.split(';')
			a=line[2].split('/')
			line2=[]
			for i in a:
				line2.append(i)
			line2.append(line[3])
			line2.append(line[5])
			line1.append(line2)		



x=[]
y=[]
cost=0

'''

####NEW NEW NEW
#per day basis; x axis is time and y axis is power consumption

for i in line1:
	if '19' in  i[2] and 'Jul' in i[1] and '03' in i[0]:
		datad[ i[3]]=i[4]
		
			
od = collections.OrderedDict(sorted(datad.items()))
#print od

for u,v in od.items():
	x.append(u)
	y.append(v)

print len(x), len(y)

plt.title(" Power Consumption Cycle in a Day") 
plt.plot(x, y, marker="*") 
plt.show()


####NEW NEW NEW
#per day basis; x axis is time in an hour and y axis is power consumption


for i in line1:
	if '19' in  i[2] and 'Jul' in i[1] and '03' in i[0]:
		datad[ i[3]]=i[4]
		
			
od = collections.OrderedDict(sorted(datad.items()))
#print od

datad1= defaultdict(lambda : None)
num=0
for u,v in od.items():
	datad1[num]=v
	num=num+1

num2=0
cost=0.0
num3=0
for num1 in range(0,96):
	if num2 < 3:  #u can change this 3 to more if you want to club more data points together, like when this is 3: then 0,1,2,3 points are clubbed together
		cost=cost+float(datad1[num1])
		#num3=num3+num1
		num2=num2+1
	else:
		c=float(cost/4)
		#n=float(num3/4)
		x.append(num3)
		y.append(c)
		num2=0
		cost=0.0
		num3=num3+1

print len(x), len(y)

plt.title(" Power Consumption Hourly Cycle in a Day") 
plt.plot(x, y, marker="*") 
plt.show()


####NEW NEW NEW
#per month basis; x axis is month  and y axis is avg power consumption of the month


mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

datam1= defaultdict(lambda : None)

m1=0
for mon1 in mon:
	m1=m1+1
	cost=0
	c=0
	for i in line1:
		if mon1 in i[1] and '18' in i[2]: #year is in i[2], can be any, here i have taken 19. Or,  remove this if you want to check for month irrespective of year
			cost=cost+float(i[4])
	c=cost/(96*31)
	x.append(m1)
	y.append(c)
		
print len(x), len(y)

plt.title("  Average Power Consumption Monthly Wise") 
plt.plot(x, y, marker="*") 
plt.show()
			
		



####NEW NEW NEW
# daily consumption for a month; x axis is day  and y axis is avg power consumption daily


#mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

datam1= defaultdict(list)


for i in line1:
	if 'Jul' in i[1] and '19' in i[2]: #year is in i[2], can be any, here i have taken 19. mon in i[1]
		datam1[ i[0]].append(i[4])
		
datam2 = collections.OrderedDict(sorted(datam1.items()))
for d in datam2:
	cost=0
	c=0
	for t in datam2[d]:
		cost=cost+float(t)
	c=float(cost/96)
	y.append(c)
	x.append(d)
	

print len(x), len(y)

plt.title("  Average Power Consumption Daily Wise for July 2019") 
plt.plot(x, y, marker="*") 
plt.show()


'''
####NEW NEW NEW
# daily consumption for a month; x axis is day  and y axis is total power consumption daily


#mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

datam1= defaultdict(list)


for i in line1:
	if 'Jul' in i[1] and '19' in i[2]: #year is in i[2], can be any, here i have taken 19. mon in i[1]
		datam1[ i[0]].append(i[4])
		
datam2 = collections.OrderedDict(sorted(datam1.items()))
for d in datam2:
	cost=0
	c=0
	for t in datam2[d]:
		cost=cost+float(t)
	#c=float(cost/96)
	y.append(cost)
	x.append(d)
	

print len(x), len(y)

plt.title(" Total Power Consumption Daily Wise for July 2019") 
plt.plot(x, y, marker="*") 
plt.show()

'''
compare month year wise  : ex : 4lines for 4 mnths daily average
compare year wise with month avg power : ex : 4lines for 4 mnths yearly wise calculated over daily
avg of the year for a month , x axis is month (histogram and average)
date or month wise forecast





m1=0
for mon1 in mon:
	m1=m1+1
	cost=0
	c=0
	for i in line1:
		if 'Jul' in i[1] and '19' in i[2]: #year is in i[2], can be any, here i have taken 19. mon in i[1]
			cost=cost+float(i[4])
	c=cost/(96*31)
	x.append(m1)
	y.append(c)
		
print len(x), len(y)

plt.title(" Average Power Consumption Daily Wise") 
plt.plot(x, y, marker="*") 
plt.show()
		




year=['17','18','19']
for i in line1:
 	for yr in year:
 		print yr
 		cost=0
		if  'Jul' in i[1] and yr in  i[2]:
			datad[ i[3]]=i[4]
			cost=cost+float(i[4])
		c1=(cost/float(96*31))
		print c1,yr
		x.append(yr)
		y.append(c1)
			
od = collections.OrderedDict(sorted(datad.items()))
#print od


for u,v in od.items():
	x.append(u)
	y.append(v)

#print x
#print y

#plt.scatter(x, y)
#plt.show()

plt.title("Time with Power Consumption") 
plt.plot(x, y, marker="*") 
'''


