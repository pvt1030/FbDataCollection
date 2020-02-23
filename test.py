import nltk
from nltk.corpus import brown
import string
import inflect
import re
from pymongo import MongoClient
from termcolor import colored
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from langdetect import detect



p = inflect.engine()
stop_words = stopwords.words('english')
# print(colored('stopwords from nltk','red'))
# print(stop_words)


def get_db_data():
    connection = MongoClient('localhost', 27017)
    db = connection.user2
    data = db.IdAndPosts2019
    data_set = data.find()
    return data_set


def get_post_string():
    data_list = get_db_data()
    record_list = []
    for record in data_list:
        id_dict = record['id']
        name_dict = record['name']
        posts = record['posts']

        messages = []
        for y in posts:
            if 'message' in y:
                messages.append(y['message'])
            if 'description' in y:
                messages.append(y['description'])
        # print(messages)
        message_string = " ".join(messages)
        # print(message_string)

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "post_messages": message_string,   # join array elements into single string
        }


        record_list.append(retrieved_data)

        # sending to db
        # profile = retrieved_data
        # print(type(profile))
        # client = MongoClient('mongodb://localhost:27017')
        # db = client.user2  # new database user2created
        # users = db.postString  # featureSelection collection created
        # result = users.insert_one(profile)

    return record_list


def preprocess_string():
    retrieved_data = get_post_string()

    for record in retrieved_data:
        id = record['id']

        name = record['name']
        print(name)
        message_text = record['post_messages']

        # pre- processing
        message_lowercase = text_lowercase(message_text)
        msg_num_str = convert_number(message_lowercase)
        msg_no_punctuation = remove_punctuation(msg_num_str)
        msg_no_white_space = remove_whitespace(msg_no_punctuation)
        lemmatized_message = lemmatize_word(msg_no_white_space)
        print(lemmatized_message)

        # feature value calculation

        print(colored('number of words ', 'green'))
        total_number_of_words = len(lemmatized_message)
        print(total_number_of_words)

        print(colored('first_person_pronoun_count ', 'green'))
        first_person_pro_count = first_person_pronoun_count(lemmatized_message)
        print(first_person_pro_count)

        print(colored('second_person_pronoun_count', 'green'))
        second_person_pro_count = second_person_pronoun_count(lemmatized_message)
        print(second_person_pro_count)

        print(colored('third_person_pronoun_count', 'green'))
        third_person_pro_count = third_person_pronoun_count(lemmatized_message)
        print(third_person_pro_count)

        print(colored('wordlength > 6', 'green'))
        word_than_six = word_length(lemmatized_message)
        print(word_than_six)

        # print(colored('English_words', 'green'))
        # english_words = lang_detect(lemmatized_message)
        # print(english_words)


def text_lowercase(text):
    return text.lower()


# convert number into words
def convert_number(text):
    # split string into list of words
    temp_str = text.split()
    # initialise empty list
    new_string = []

    for word in temp_str:
        # if word is a digit, convert the digit
        # to numbers and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)

            # append the word as it is
        else:
            new_string.append(word)

            # join the words of new_string to form a string
    temp_str = ' '.join(new_string)
    return temp_str


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def remove_whitespace(text):
    return " ".join(text.split())


lemmatizer = WordNetLemmatizer()


# lemmatize string
def lemmatize_word(text):
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
    return lemmas


def first_person_pronoun_count(text):
    count = 0
    first_person_pronouns = ['i', 'me', 'my', 'mine', 'myself','im']
    for i in text:
        if i in first_person_pronouns:
            count += 1
    return count


def second_person_pronoun_count(text):
    count = 0
    second_person_pronouns = ['you', 'your', 'yours','yourself']

    for i in text:
        if i in second_person_pronouns:
            count += 1
    return count


def third_person_pronoun_count(text):
    count = 0
    third_person_pronouns = ['he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself']

    for i in text:
        if i in third_person_pronouns:
            count += 1
    return count


def word_length(text):
    count = 0
    for i in text:
        if len(i) > 6:
            count += 1
    return count


# def lang_detect(text):
#     english_words = []
#     for i in text:
#         lan = detect(i)
#         if lan is 'en':
#             english_words.append(i)
#
#     return english_words





if __name__ == "__main__":
    get_db_data()
    get_post_string()
    preprocess_string()