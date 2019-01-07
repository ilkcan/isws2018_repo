import geocoder
import sys
import os

def main(annotated_file, linking_output, difference_file):
	ann_file = open(annotated_file, 'r')
	locations = ann_file.readlines()
	locations_unique = set([x.strip() for x in locations])
	ann_file.close()
	
	linking_out_file = open(linking_output, 'r')
	linked_location_names = set()
	linked_locations = linking_out_file.readlines()
	linking_out_file.close()
	for linked_location in linked_locations:
		linked_location_names.add(linked_location.split("\t")[0])
	
	unlinked_locations = locations_unique.difference(linked_location_names)
	

	diff_file = open(difference_file, 'w')
	for location_name in unlinked_locations:
		diff_file.write(location_name + "\n")
	diff_file.close()
		

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
