from maxkmlgenerator import*

if __name__=="__main__":
	#check for command line arguments:
	if len(sys.argv) == 1:
		print("use 'python "+sys.argv[0]+" help' for usage")
	elif len(sys.argv) == 2: 
		if sys.argv[1] == "help":
			print("usage: 'python "+sys.argv[0]+" <fort.14 file> <maxele.63 file> <typhoon name> <event id> <maxsurge id> <output directory> <.shp file> <province filters>'")
		else:
			print("Unknown command: '"+sys.argv[1]+"'")
	else:
		try:
			fort14 = sys.argv[1]
			maxelev63 = sys.argv[2]
			typhoonName = sys.argv[3]
			eventId = sys.argv[4]
			MaxSurgeId = sys.argv[5]
			outputDir = sys.argv[6]
			shapeFile = sys.argv[7]
			filt = []
			for i in range(8,len(sys.argv)):
				filt.append(sys.argv[i])
		except	IndexError:
			print("Complete the command line argument to proceed")

		else:
			if filt != []:
				generator=MaxKmlGenerator(fort14,maxelev63,typhoonName,eventId,MaxSurgeId,outputDir,shapeFile,filt)
				generator.writeToKml()
			else:
				print("Please indicate filters")