import spotlight
import sys
import os

def main(input_folder, output_folder):
	list_of_files = os.listdir(input_folder)
	for file_name in list_of_files:
		print("Processing " + file_name + "...")
		inp_file = open(input_folder + file_name, 'r')
		location_names = inp_file.readlines()
		location_names_unique = set([x.strip() for x in location_names])
		out_file = open(output_folder + file_name, 'w')
		print(len(location_names_unique))
		for location_name in location_names_unique:
			try:
				only_place_filter = {
					'policy': "whitelist",
					'types': "DBpedia:Place",
					'coreferenceResolution': False
				}

				dbpedia_output = spotlight.annotate("http://api.dbpedia-spotlight.org/en/annotate", 
					location_name.strip(),
					filters=only_place_filter)
				curr_row = []
				curr_row.append(location_name)
				curr_row.append(dbpedia_output[0]['URI'])
				curr_row.append(str(dbpedia_output[0]['similarityScore']))
				out_file.write("\t".join(curr_row) + "\n")
			except: 
				continue
		out_file.close()
		

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])