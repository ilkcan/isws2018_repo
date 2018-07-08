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

def main():
	content = "For though all over Italy traces of the miracle are apparent, Florence was its very home and still can point to the greatest number of its achievements."
	sentences = nltk.sent_tokenize(content)
	print(sentences[0])
	tokenized_sentence = nltk.word_tokenize(sentences[0])
	print(tokenized_sentence)
	tagged_sentence = nltk.pos_tag(tokenized_sentence)
	print(tagged_sentence)
	chunked_sentence = nltk.chunk.ne_chunk(tagged_sentence)
	location_names_sentence = extract_location_names(chunked_sentence)
	location_set = set(location_names_sentence)
	print(location_set)

if __name__ == "__main__":
    main()
