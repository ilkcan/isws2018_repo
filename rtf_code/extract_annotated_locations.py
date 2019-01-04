# Each location on a separate line 

import sys 
import os

def main(input_folder, output_folder):
    list_of_files = os.listdir(input_folder)
    for file_name in list_of_files:
        print("Processing " + file_name + "...")
        text = "" 
        loc_track = 0 

        with open(input_folder + file_name, 'r') as f:
            for line in f:
                line = line.rstrip("\n")
                line = line.replace("\t", "/")
                if "B-LOCATION" in line:
                    #line = line.rstrip("\n")
                    line = line.replace("/B-LOCATION", "")
                    loc_track = 1 
                 #   sys.stdout.write(line + " ")
                    text = text + line + " "
                if "/O" in line and loc_track == 1: 
                    loc_track = 0  
                #    sys.stdout.write("\n")
                    text = text + "\n"
                if "I-LOCATION" in line:
                    line = line.replace("/I-LOCATION", "")
                 #   sys.stdout.write(line + " ")
                    text = text + line + " "
                else:
                    next 
                    
            print(text)

        # you probably want to write it to a file 
        outputfile = open(output_folder + file_name,"w")
        outputfile.write(text)
        outputfile.close()
        

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])