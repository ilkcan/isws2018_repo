import sys
import nltk
import os

# The function that is used to extract location names from the output of ne_chunk function. 
# The output is a tree and we need to iterate over this tree to find out the location entities.
# The function is recursive meaning that it calls itself as you can see on line 16. The for loop basically calls the function for each child of the current node.
def extract_location_names(tree_node):
	location_names = []
	if hasattr(tree_node, 'label') and tree_node.label:
		if tree_node.label() == 'LOCATION' or tree_node.label() == 'GPE' or  tree_node.label() == 'FACILITY':
			location_names.append(' '.join([child[0].capitalize() for child in tree_node]))
		else:
			for child in tree_node:
				location_names.extend(extract_location_names(child))

	return location_names

# This function is written to check the possible labels in the named entity recognition.
# Currently, it is only used to obtain the list of labels for each input corpus.
def extract_labels(tree_node):
	labels  = []
	if hasattr(tree_node, 'label') and tree_node.label:
		labels.append(tree_node.label())
		for child in tree_node:
			labels.extend(extract_labels(child))
	return labels

# The main function requires an input and an output folder. 
# The input folder contains the input text data.
# The output folder is the folder that the output files will be saved into.
def main(input_folder, output_folder):
	list_of_files = os.listdir(input_folder)
	for file_name in list_of_files:
		print("Processing " + file_name + "...")
		inp_file = open(input_folder + file_name, 'r')
		out_file = open(output_folder + file_name, 'w')
		content = inp_file.read()
		sentences = nltk.sent_tokenize(content)
		tokenized_sentences = []
		for sentence in sentences:
			tokenized_sentences.append(nltk.word_tokenize(sentence))
		tagged_sentences = []
		for tokenized_sentence in tokenized_sentences:
			tagged_sentences.append(nltk.pos_tag(tokenized_sentence))
		chunked_sentences = []
		for tagged_sentence in tagged_sentences:
			chunked_sentences.append(nltk.chunk.ne_chunk(tagged_sentence))
		#print(chunked_sentences)
		location_names = []
		for chunked_sentence in chunked_sentences:
			location_names_sentence = extract_location_names(chunked_sentence)
			location_names.extend(location_names_sentence)
		#print(chunked_sentences)
		location_set = set(location_names)
		labels_list = []
		for chunked_sentence in chunked_sentences:
			labels_list.extend(extract_labels(chunked_sentence))
		labels = set(labels_list)
		print(labels)
		out_file.write("\n".join(location_set))
		out_file.close()
		#print(content)
		print("file_finished")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
