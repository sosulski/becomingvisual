import csv as csv
import numpy as np
import matplotlib
from pylab import *
from matplotlib import pyplot as PLT
from operator import itemgetter, attrgetter

#read in and store csv file in numpy recarray object. 
#allows for easy access of columns and rows
 
data = csv2rec('mba3.csv', skiprows=0, delimiter=',')

#getting sorted data for column 4 presalary
presalsort = sorted(data, key=itemgetter(4))
getcount = itemgetter(4)
presalary = map(getcount,presalsort)
#print(presalary)

#getting corresponding schools for sorted column 4 data
getnames =itemgetter(1)
presalnames =map(getnames,presalsort)
#print(presalnames)

#getting corresponding rank for schools for sorted column 4
getrank =itemgetter(0)
rankpresal =map(getrank,presalsort)
print(rankpresal)


#print (presaly)

#sorting average salary
avgsalsort = sorted(data, key=itemgetter(3))
#getting sorted data for column 3 avgsalary
getsalcount = itemgetter(3)
avgsal = map(getsalcount,avgsalsort)
#print(avgsal)

#getting corresponding schools for sorted column 3 data
getsalschoolnames =itemgetter(1)
avgsalschool = map(getsalschoolnames,avgsalsort)
#print(avgsalschool)

#getting corresponding rank for schools for sorted column
getrank_avgsal =itemgetter(0)
rankavgsal =map(getrank_avgsal,avgsalsort)
print(rankavgsal)

#sorting % of grads with jobs
gradjobssort = sorted(data, key=itemgetter(5))
#getting sorted data for column 5 GradJobs
getgradjobs = itemgetter(5)
gradjobs = map(getgradjobs,gradjobssort)
#print(gradjobs)

#getting corresponding schools for sorted column 3 data
getgradjobschoolnames =itemgetter(1)
gradjobsschool = map(getgradjobschoolnames,gradjobssort)
#print(gradjobsschool)

#getting corresponding rank for schools for sorted column 
getrank_jobs =itemgetter(0)
rankjobs =map(getrank_jobs,gradjobssort)
print(rankjobs)
 
#test your work by printing a column from the csv
#data.sort('avgsalary')
#print data['school']
#print data['avgsalary']
#print data ['presalary']
#print data ['gradjobs']

#Create a canvas for plotting multiple graphs

fig = PLT.figure(linewidth=0.0,frameon=True, dpi=80, figsize=(17,8))
fig.canvas.set_window_title('MBA Rankings')
#if you use title you get a frame for the entire canvas/plot 
#title('MBA Rankings. Starting salary or Job percentage?')
#fig.set_figheight(10)
#fig.set_figwidth(20)
fig.patch.set_facecolor('#FFFFFF')
matplotlib.rc('xtick', labelsize=9, color='#000000') # setting font size for x & y
matplotlib.rc('ytick', labelsize=9, color='#000000') 

#barchart horizontal %presalary - working

ax1 = fig.add_subplot(131, frameon=False, axis_bgcolor='#FFFFFF')
#fig.subplots_adjust(hspace=.5)

#remove all those annoying ticks
for a in ax1.yaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

for a in ax1.xaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

val = presalary    # the bar lengths
pos = arange(len(presalary)) +.5    # the bar centers on the y axis
rects = ax1.barh(pos,val, align='center', edgecolor='#CCCCCC', height=.25, color='#CCCCCC')
yticks(pos, (rankpresal))
xlabel('Pre Salary %')

#Plot a solid vertical gridline to highlight the avg position
plt.plot([76,76], [0, 26], 'r', alpha=0.25, lw=2)

##barchart horizontal avgsalary - working
ax2 = fig.add_subplot(132, frameon=False, axis_bgcolor='#FFFFFF')

#remove all those annoying ticks

for a in ax2.yaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

for a in ax2.xaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

#data['avgsalary'] = tuple([float(i) for i in data['avgsalary']])
val1 = avgsal    # the bar lengths
pos1 = arange(len(data)) +.5    # the bar centers on the y axis
rects = ax2.barh(pos1,val1, edgecolor='#CCCCCC', align='center', height=.25, color='#CCCCCC')
yticks(pos1, (rankavgsal))
xlabel('Average Salary')

#Plot a solid vertical gridline to highlight the avg position
plt.plot([113732,113732], [0, 26], 'r', alpha=0.25, lw=2)


##barchart horizontal gradjobs
ax3 = fig.add_subplot(133, frameon=False, axis_bgcolor='#FFFFFF')

#remove all those annoying ticks

for a in ax3.yaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

for a in ax3.xaxis.majorTicks:
  a.tick1On=False
  a.tick2On=False

#data['gradjobs'] = tuple([float(i) for i in data['gradjobs']])
val2 = gradjobs    # the bar lengths
val2.sort()
pos2 = arange(len(data)) +.5    # the bar centers on the y axis

rects = ax3.barh(pos2,val2, align='center', edgecolor='#CCCCCC', height=.25, color='#CCCCCC')
yticks(pos2, (rankjobs))
xlabel('% Graduates with Jobs')

#Plot a solid vertical gridline to highlight the avg position
plt.plot([93,93], [0, 26], 'r', alpha=0.25, lw=2)

PLT.show()
