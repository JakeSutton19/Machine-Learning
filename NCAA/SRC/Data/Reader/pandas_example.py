import numpy
import pandas as pd
import os


class search:
	#pull all the csv files into seperate pandas dataframes
	#the instructions have a typo, name for tester.csv is actually "testers.csv" 
	tstCSV = pd.read_csv("testers.csv")
	dvcCSV = pd.read_csv("devices.csv")
	bugsCSV = pd.read_csv("bugs.csv") 
	tstdCSV = pd.read_csv("tester_device.csv")
	#merge the testers dataframe with the bugs dataframe
	merge1 = pd.merge(bugsCSV, tstCSV, on=['testerId'], how='inner')
	merge1.head()
	#concatenate first and last names to new fullName column
	merge1['fullName'] = merge1['firstName'].str.cat(merge1['lastName'],sep=" ")
	#merge that one above with the devices dataframe
	merge2 = pd.merge(merge1, dvcCSV, on=['deviceId'], how='inner')
	merge2.head()


	def __init__(self):
		#prompt for the search criteria
		self.country1 = [str(x) for x in input("enter countries seperated by commas: ").split(",")]
		#do the same for devices, starting with filtered country dataframe
		self.devices1 = [str(x) for x in input("enter device descriptions, seperated by commas: ").split(",")]
	def doSearch(self):
		merge2 = search.merge2
		#if input is "ALL" then just leave current dataframe intact
		#else, filter the dataframe for the input countries
		if self.country1[0] == "ALL":
			ctry = merge2
		else:
			ctry = merge2.loc[merge2['country'].isin(self.country1)]

		if self.devices1[0] == "ALL":
			dvcs = ctry
		else:
			dvcs = ctry.loc[ctry['description'].isin(self.devices1)]
		#get value counts from most to least, by number of times a testerId appears in the dataframe
		#and print to console
		pb = dvcs['fullName'].value_counts()
		print("Users Name/Experience:")
		print(pb)

if __name__ == '__main__':
	#initiate class
	searchy = search()
	#initiate search
	searchy.doSearch()