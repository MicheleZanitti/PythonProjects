class Book:
    def __init__(self, filename):
        self.filename = filename
        self.title = None
        self.author = None
        self.year = None
        self.language = None
        self.text = None
        # open the file and parse in the constructor
        with open(filename, 'r', encoding='utf-8') as f:
            self.parse_file(f)
    
    
    
    def parse_file(self, thisfile):
        # extract the attributes from the text and store in the right variables
        
        title = ''
        author = ''
        year = 0
        language = ''
        text = ''

        # step 1: get the header and separate header from text
        text = thisfile.read()
        header_end = text.index('***')
        header = text[:header_end]
        text = text[header_end:]

        # step 2: get the metadata
        # we can split the header based on new lines (\n), so to get a list of strings
        header_lines = header.split('\n')
        for line in header_lines:
            if line.find('Title: ') >= 0:
                # we have a title
                line = line.strip()
                title = line[7:] # len('Title: ') is 7
                #print(title)
            if line.find('Author:') >= 0:
                line = line.strip()
                author = line[8:]
                #print(author)
            if line.find('Language:') >= 0:
                line = line.strip()
                language = line[len('Language: '):]
                #print(language)
            if line.find('Release Date: ') >= 0:
                line = line.strip()
                year = line[len('Release Date: '):]
                #print(year)
                year_words = year.split(' ')
                #print(year_words)
                year = year_words[2]
                #print(year)
        
        # update the object attributes
        self.title = title
        self.author = author
        self.year = year
        self.language = language
        self.text = text
        
        
        
    # 3. return the average word length for a book
    def avg_word_length(self):
        # we split the text based on whitespace, then find the length of all words and return the average
        all_words = self.text.split(' ') # rudimentary split
        all_words_lengths = []
        for w in all_words:
            all_words_lengths.append(len(w))
        return sum(all_words_lengths)/len(all_words_lengths)

    
    
    # 4. return the average sentence length, in char
    def avg_sentence_length(self):
        # we split the text based on dots, then find the length of all sentences and return the average
        all_sent = self.text.split('.')
        all_sent_lengths = []
        for w in all_sent:
            all_sent_lengths.append(len(w))
        return sum(all_sent_lengths)/len(all_sent_lengths)

    
    
    # 5. return the average paragraph length, in char
    def avg_paragraph_length(self):
        # we split the text based on dots followed by newlines, then find the length of all paragraphs and return the average
        all_par = self.text.split('.\n')
        all_par_lengths = []
        for w in all_par:
            all_par_lengths.append(len(w))
        return sum(all_par_lengths)/len(all_par_lengths)

    
    
    # 6 Count the frequency of all the letters and return a dictionary of word : word_count pairs.
    # remember that the upper case letters are not the same as lower case letter, so we must set everything in lowercase (or uppercase)
    def word_count_dict(self):
        # we split the text based on whitespace and create an empty dictionary using dict().
        words = self.text.lower().split(' ') # we can concatenate methods like this.
        words_dict = dict()

        for word in words:
            if word in words_dict.keys():
                words_dict[word] = words_dict[word] + 1 # we update the count
            else: # the word is not in the dictionary, so we need to create the pair and set its count at 1
                words_dict[word] = 1
        return words_dict