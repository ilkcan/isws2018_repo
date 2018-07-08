import geocoder
import sys
import os

def main(input_folder, output_folder):
	list_of_files = os.listdir(input_folder)
	for file_name in list_of_files:
		print("Processing " + file_name + "...")
		inp_file = open(input_folder + file_name, 'r')
		location_names = inp_file.readlines()
		out_file = open(output_folder + file_name, 'w')
		for location_name in location_names:
			try:
				geonames_entities = geocoder.geonames(location_name, name_equals=location_name, continentCode='EU', key='42s_isws2', maxRows=1)
				if (len(geonames_entities) > 0):
					geonames_entity = geonames_entities[0]
					curr_row = []
					curr_row.append(location_name.strip())
					curr_row.append(str(geonames_entity.geonames_id))
					if geonames_entity.country:
						curr_row.append(geonames_entity.country)
					if geonames_entity.description:
						curr_row.append(geonames_entity.description)
					out_file.write("\t".join(curr_row) + "\n")
			except (UnicodeEncodeError, UnicodeDecodeError): 
				print("An exception occurred...")
		out_file.close()
		

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
