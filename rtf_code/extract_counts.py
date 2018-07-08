import sys 

def main(input_file_path, output_folder):
	inp_file = open(input_file_path, 'r')
	country_out_file = open(output_folder + "stats_country.txt", 'w')
	type_out_file = open(output_folder + "stats_type.txt", 'w')
	lines = inp_file.readlines()
	countries = dict()
	location_types = dict()
	for line in lines:
		words = line.split('\t')
		if len(words) == 4:
			country = words[2].strip()
			location_type = words[3].strip()
			if country in countries:
				countries[country] = countries[country] + 1
			else:
				countries[country] = 1
			
			if location_type in location_types:
				location_types[location_type] = location_types[location_type] + 1
			else:
				location_types[location_type] = 1
	for country in countries:
		country_out_file.write(country + "\t" + str(countries[country]) + "\n")
	country_out_file.close()

	for location_type in location_types:
		type_out_file.write(location_type + "\t" + str(location_types[location_type]) + "\n")
	type_out_file.close()
	print (countries)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])