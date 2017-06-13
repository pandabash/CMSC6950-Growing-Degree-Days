#!/usr/bin/Python
import os, sys, stat
import pandas as pd
import numpy as np
import getopt
import shutil
import matplotlib.pyplot as plt

# define the roots
plotpath= (os.getcwd()+'/Plot/')
filepath= (os.getcwd()+'/DataFiles/')

# get the files
def get_allfiles():
	files = os.listdir(filepath)
	return files

# define min_max_plot function to plot the max and min daily temperature for the given cities
def AccGDD_plot(cityName,year,annual):
	if not os.path.exists(plotpath+str(cityName)):
		os.makedirs(plotpath+str(cityName))
	fig = plt.figure(figsize=(12, 6))
	plt.title('Accumulated GDD in '+str(cityName)+' '+str(year))
	plt.ylabel('Accumulated GDD')
	plt.xlabel('Day of Year')
	plt.plot(annual.index.values.tolist(), annual['accGDD'], marker='o',color="red", label = "Accumulated GDD")
	plt.legend(loc='upper left')
	fig.savefig('Plot/accGdd'+str(cityName)+'accGDD'+str(year)+'.png')
        
# define parseData function that read all data from files
def parseData(data,infor):
	cityName = infor[0]
	start = infor[1]
	end = infor[2]
	list_years = list(range(int(start),int(end)+1))
	for year in list_years:
		annual = data[data['Date/Time'].str.contains(str(year))]
		AccGDD_plot(cityName,year,annual)

# define run function which insider of main function
def run():
	files = get_allfiles()
	for element in files:
		Data = pd.read_csv(filepath+element, encoding = 'utf-8',index_col=0)
		placeInfo = element[:-4].split('_')[2:] # city startyear endyear
		parseData(Data,placeInfo)

                
      
# define the main function
if __name__ == '__main__':
	run()

