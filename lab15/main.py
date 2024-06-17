def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

def filter_emails(data):
    emails = data.split()
    def is_valid_email(email):
        return email.count('@') == 1
    valid_emails = filter(is_valid_email, emails)
    return list(valid_emails)

def extract_keywords(data, num):
    words = data.split()
    def is_valid_word(word):
        return len(word) > 4
    valid_word = filter(is_valid_word, words)
    return list(valid_word)

import re

def process_text(texts):
    def clean_text(text):
        cleaned = re.sub(r'[^\w\s]', '', text).strip().lower()
        return cleaned

    text_list = texts.split(',')

    cleaned_texts = map(clean_text, text_list)

    filtered_texts = filter(lambda x: len(x) > 1, cleaned_texts)

    return list(filtered_texts)

def normalize_data(numbers):
    num_list = list(map(float, numbers.split(',')))
    
    max_value = max(num_list)
    
    normalized_numbers = list(map(lambda x: round(x / max_value, 3), num_list))
    
    return normalized_numbers

def concatenate_strings(data, separator):
    parts = data.split(separator)
    
    concatenated = ''.join(parts)
    
    return concatenated

def sum_numeric_strings(numbers):
    total_sum = 0
    
    number_list = numbers.split(',')
    
    for num_str in number_list:
        try:
            num = int(num_str.strip())  
            total_sum += num  
        except ValueError:
            pass  
    
    return total_sum

def filter_numbers(numbers, threshold):
    filtered_numbers = []
    
    number_list = numbers.split()

    for num_str in number_list:
        try:
            num = float(num_str)
            if num > threshold:
                filtered_numbers.append(num)
        except ValueError:
            pass 
    
    return filtered_numbers

def map_to_squares(numbers):
    number_list = numbers.split(',')

    squared_numbers = [int(num.strip()) ** 2 for num in number_list]
    
    return squared_numbers

def reverse_strings(words):
    word_list = words.split(',')
    
    reversed_words = [word[::-1] for word in word_list]
    
    return reversed_words


