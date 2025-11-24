def word_count(file_contents):
        word_array = file_contents.split()
        return len(word_array)

def letter_count(file_contents):
	letter_dict = {}
	letters = file_contents.lower()
	for letter in letters:
		if letter not in letter_dict:
			letter_dict[letter] = 1
		else:
			letter_dict[letter] += 1
	return(letter_dict)

def sort_on(items):
	return items["num"]

def sorter(unsorted_dict):
	formatted_list = []
	for letter_dict in unsorted_dict:
		if letter_dict not in formatted_list:
			formatted_list.append({"char":letter_dict,"num":unsorted_dict[letter_dict]})
		else:
			raise Exception("cannot add to list")
	formatted_list.sort(reverse=True, key=sort_on)
	return(formatted_list)
