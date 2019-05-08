# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
# import matplotlib.pyplot as plt
import ast
#from home import JobSearch

def get_info(job_desc, resume):
	blacklist=[]
	blackarray=[]
	resume33=[]
	jobdescription = []

	jd = job_desc#(JobSearch.execute("Product Management Full Time Los Angeles Indeed")[0])["jobDescription"].split(" ")

	############################################################################################
	#THIS IS THE BLACK LIST
	with open('home/scripts/jobhunterblacklist.txt', encoding="latin-1") as file1:
		for line in file1:
			line = line.strip().split(" ") #or some other preprocessing
			blacklist.append(line) #storing everything in memory!
		for k in blacklist:
			blackarray += k

	blacklistu=[x.lower() for x in blackarray]

	################################################################################################
	#THIS WILL BE RESUME
	line33 = resume.strip().split(" ") #or some other preprocessing
	resume33.append(line33) #storing everything in memory!

	mergelist33= []
	for k in resume33:
		mergelist33 += k

	newmerge33=[x.lower() for x in mergelist33]

	#########################################################################################################################

	for line in jd:
		# line = line.strip().split(" ") #or some other preprocessing
		jobdescription.append(line) #storing everything in memory!

	mergelist1= []
	for k in jobdescription:
		mergelist1 += k

	newmerge1=[x.lower() for x in mergelist1]


	#################################################################################################################

	#count= 1000
	count= 1
	#index1=100
	index1=1
	#index2=0
	index2=0
	#count33= 1000
	count33= 1
	#index33=100
	index33=1



	#only adding if job description newmerge1   are not in the black list which is mega merge IS BLACK LIST
	#NEWMERGE1 IS JB
	for i in blacklistu[:]:
		newmerge1[:] = [x for x in newmerge1 if x != i]


	#newmerge33 is the resume
	for i in blacklistu[:]:
		newmerge33[:] = [x for x in newmerge33 if x != i]




	###############################################################################################

	#calculating number of hits
	total = len(jd)
	hit = 0
	for t in newmerge33:
		if t in jd:
			hit+=1




	#######################################################
	###########################################################################
	#this is for the graphical plot
	percent = hit/float(total)
	percent = percent *100



	#objects = ('100% match','job1', 'job2', 'job3', 'job4', 'job5', 'job6')
	objects = ('100% match', "JOBLOL", 'job2', 'job3', 'job4', 'job5', 'job6')
	y_pos = np.arange(len(objects))
	performance = [100,percent,7,70,85,88,90]

	return percent