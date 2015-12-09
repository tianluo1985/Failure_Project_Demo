# -*- coding: utf-8 -*-
import nltk
import re
import sys

import pickle # data saving and loading module
import pprint
import json

from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def main():

	all_text = 'hello world! update'
	all_text = remove_address_info(all_text)
	word_freq = calculate_all_text_freq(all_text)
	print word_freq
	
def calculate_all_text_freq(all_txt):


	all_dict = load_dict('alldict_aftmanu.txt')
	print len(all_dict)
	row_clean_txt = remove_error_words(all_txt)
	row_clean_txt = ' '.join(row_clean_txt)
	row_cell_word = extract_pure_word(row_clean_txt)
	row_cell_stemmed_word = stem_pure_word(row_cell_word)
	row_word_freq =  text_features_word_freq(row_cell_stemmed_word,all_dict)

	return row_word_freq

def remove_error_words(text):


 	all_words = [word for word in text.lower().split()]
	eng_pattern=re.compile(u'^[\s\w\d\?><;:,./\{\}\[\]\-_\+=!@\#\$%^&\*\|\']*$') # All english language code
	
	clean_txt = []

	for word in all_words:
		word = re.findall(eng_pattern,word)
		if len(word):
			clean_txt.extend(word)
		else:
			clean_txt.extend(' ')
	# print clean_txt
	#print len(clean_text)
	
	return clean_txt

def remove_address_info(cell_txt):

	if 'ship' in cell_txt:
		ship_indx = cell_txt.index('ship')	
		cell_txt = cell_txt[0:ship_indx]


	return cell_txt


def load_dict(filename):
	
	with open(filename,'r') as file_object:
		all_dict = json.load(file_object)
		file_object.close()
	return all_dict


def extract_pure_word(document):


	texts_tokenized = [word.lower() for word in word_tokenize(document)]

	start_pattern = re.compile(u'^[\?><;:,./\{\}\[\]\-_\+=!@\#\$%^&\*\|\']') 
	end_pattern = re.compile(u'[\?><;:,./\{\}\[\]\-_\+=!@\#\$%^&\*\|\']$') 

	i = -1
	for word in texts_tokenized:
		i = i + 1
		for ntimes in range(40):
			word = start_pattern.sub('',word)
			word = end_pattern.sub('',word)
		texts_tokenized[i] = word

	texts_tokenized = [word for word in texts_tokenized if not 'date' in word]
	texts_tokenized = [word for word in texts_tokenized if not ':' in word]
	texts_tokenized = [word for word in texts_tokenized if not word==''] 

	english_stopwords = ["a", "about", "above", "across", "after", "afterwards", "again", "against", "all", "almost", 
				"alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount", 
				"an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as", 
				"at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", 
				"behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", 
				"by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", 
				"do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", 
				"empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", 
				"few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", 
				"found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", 
				"he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", 
				"himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", 
				"is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", 
				"may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", 
				"must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", 
				"nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", 
				"one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", 
				"own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", 
				"seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", 
				"some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", 
				"take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", 
				"thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", 
				"though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", 
				"towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", 
				"we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", 
				"whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", 
				"whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", 
				"yourself", "yourselves", "the"]
	english_stopwords.extend([',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '<', '>','=','#','%','$','\'','\"','\'\''])
	english_stopwords.extend(['hello','look','notes','details','cisco','until','problem','description','statement',
							'service','request','however','date','year','yesterday', 'yestreday', 'yi', 'yilmaz', 
							'ym', 'yolu', 'yuregir','zhe', 'zhen', 'zhi', 'zhonghu', 'zhuang', 'zi'])
	# print english_stopwords
	words_filtered_stopwords = [word for word in texts_tokenized if not word in english_stopwords]

	# print words_filtered_stopwords[1:100]
	return words_filtered_stopwords
	

def stem_pure_word(all_words):
	st = LancasterStemmer()
	texts_stemmed = [st.stem(word) for word in all_words]

	return texts_stemmed

def text_features_word_freq(cell_word,col_dict):
	
	word_freq = []

	for word in col_dict:
		if word in cell_word:
			word_freq.append(cell_word.count(word))
		else:
			word_freq.append(0)

	return word_freq

if __name__ == '__main__':
	main()
