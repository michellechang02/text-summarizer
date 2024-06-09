import nltk            
import sys   
from nltk.corpus import stopwords   
import string         
from nltk.tokenize import word_tokenize, sent_tokenize 
from heapq import nlargest
import re


def summarize_text(input_text: str) -> str:
    print("GOTHERE11")
    # stop_words and punctuation to ignore
    stop_words = set(stopwords.words("english"))      
    punctuation = string.punctuation + '\n'

    # all the words that are tokenized
    words = word_tokenize(input_text)

    
    #create a frequency table
    freq_table = dict()                 
    for word in words:               
        word = word.lower()                 
        if word in stop_words or word in punctuation:                 
            continue                  
        if word in freq_table:    #increase frequency by 1                  
            freq_table[word] += 1            
        else:          #add to the frequency table
            freq_table[word] = 1  
    
    #find the maximum value
    max_frequent = max(freq_table.values())

    for word in freq_table.keys():
        freq_table[word] = freq_table.get(word)/max_frequent
    
    #tokenize the sentences 
    sentences = sent_tokenize(input_text)
    print("GOTHERE22")
    print(freq_table)


    sentence_weight = dict()
    for sentence in sentences:
        word_count_no_stopwords = 0

        for word_weight in freq_table:
            if word_weight in sentence.lower():
                word_count_no_stopwords += 1
                if sentence in sentence_weight:
                    sentence_weight[sentence] += freq_table[word_weight]
                else:
                    sentence_weight[sentence] = freq_table[word_weight]
    
    print(sentence_weight)

    select_length = int(len(sentence_weight) * 0.3)

    summary = nlargest(select_length, sentence_weight, key=sentence_weight.get)
    final_summary = [word for word in summary]
    
    # Filter out non-alphabetic characters except periods and join with spaces
    filtered_summary = [re.sub(r'[^\w\s.]', '', word) for word in final_summary if re.sub(r'[^\w\s.]', '', word)]

    # Remove any extra spaces and join the filtered words
    summary = " ".join(filtered_summary).strip()

    # Ensure no multiple spaces in the result
    summary = re.sub(r'\s+', ' ', summary)

    return summary


          