import sys
import nltk
import os

def extract_location_names(tree_node):
	location_names = []
	if hasattr(tree_node, 'label') and tree_node.label:
		if tree_node.label() == 'LOCATION' or tree_node.label() == 'GPE' or  tree_node.label() == 'FACILITY':
			location_names.append(' '.join([child[0] for child in tree_node]))
		else:
			for child in tree_node:
				location_names.extend(extract_location_names(child))

	return location_names

def extract_labels(tree_node):
	labels  = []
	if hasattr(tree_node, 'label') and tree_node.label:
		labels.append(tree_node.label())
		for child in tree_node:
			labels.extend(extract_labels(child))
	return labels

def main(file_name):
	inp_file = open(file_name, 'r')
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
	location_names = []
	for chunked_sentence in chunked_sentences:
		location_names_sentence = extract_location_names(chunked_sentence)
		location_names.extend(location_names_sentence)
	location_set = set(location_names)
	print("\n".join(location_set))


if __name__ == '__main__':
	main(sys.argv[1])
