import sys
from surgewarnings import*

if __name__=="__main__":
	#check for command line arguments:
	if len(sys.argv) == 1:
		print("use 'python "+sys.argv[0]+" help' for usage")
	elif len(sys.argv) == 2: 
		if sys.argv[1] == "help":
			print("usage: 'python "+sys.argv[0]+" <.shp file for Barangay> <.shp file for Munipalities/Cities> <municipality/city filter> <fort.14 file> <fort.15 file> <maxele.63 file> <fort.63 file> <output directory> [radiusOffset]'")
		else:
			print("Unknown command: '"+sys.argv[1]+"'")
	else:
		radiusOffset = 1000 #default radius offset

		shape_file = sys.argv[1]
		shape2_file = sys.argv[2]
		filt = sys.argv[3]
		fort_14 = sys.argv[4]
		fort_15 = sys.argv[5]
		maxelev63 = sys.argv[6]	
		fort_63 = sys.argv[7]	
		output_dir = sys.argv[8]	

		earliestSurge=EarliestSurgeLocator(fort_14,fort_15,fort_63,shape2_file,[filt])
		earliestSurge.getEarliestSurge()
		earliestSurge.getBarangayOfEarliestSurge(shape_file,output_dir)

		if len(sys.argv) > 8 : 
			try: 
				radiusOffset = int(sys.argv[6])
			except ValueError:
				print("input valid radiusOffset. Shifting to default radiusOffset 1000")


		warning = Warnings(shape_file,filt,fort_14,maxelev63,radiusOffset)
		warning.generateWarnings()
		warning.writeToFile(output_dir)
		print(datetime.datetime.now())