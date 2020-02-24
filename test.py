import nltk
from nltk.corpus import brown
import string
import inflect
import re
import pandas as pd
from pymongo import MongoClient
from termcolor import colored
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

p = inflect.engine()
stop_words = stopwords.words('english')
# print(colored('stopwords from nltk','red'))
# print(stop_words)

angry = []
anticipation = []
disgust = []
fear = []
joy = []
negative = []
positive = []
sadness = []
surprise = []
trust = []

# angry_count = 0
# anticipation_count = 0
# disgust_count = 0
# fear_count = 0
# joy_count = 0
# negative_count = 0
# positive_count = 0
# sadness_count = 0
# surprise_count = 0
# trust_count = 0

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
    word_per = []
    first_person_per = []
    second_person_per = []
    third_person_per = []
    angry_perc = []
    anticipation_perc = []
    disgust_perc = []
    fear_perc= []
    joy_perc= []
    negative_perc= []
    positive_perc= []
    sadness_perc= []
    surprise_perc= []
    trust_perc= []

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
        eng_words = eng_words_only(msg_no_white_space)

        # feature value calculation

        print(colored('number of words ', 'green'))
        total_number_of_words = len(lemmatized_message)
        print(total_number_of_words)
        #
        print(colored('number of english words ', 'green'))
        total_number_of_eng_words = len(eng_words)
        print(total_number_of_eng_words)
        #
        print(colored('first_person_pronoun_count and percentage ', 'green'))
        first_person_pro_count = first_person_pronoun_count(lemmatized_message)
        first_person_pro_percentage = word_percentage(first_person_pro_count, total_number_of_eng_words)
        first_person_per.append(first_person_pro_percentage)
        print(first_person_pro_count)
        print(first_person_pro_percentage)


        print(colored('second_person_pronoun_count and percentage', 'green'))
        second_person_pro_count = second_person_pronoun_count(lemmatized_message)
        second_person_pro_percentage = word_percentage(second_person_pro_count, total_number_of_eng_words)
        second_person_per.append(second_person_pro_percentage)
        print(second_person_pro_count)
        print(second_person_pro_percentage)


        print(colored('third_person_pronoun_count and percentage', 'green'))
        third_person_pro_count = third_person_pronoun_count(lemmatized_message)
        third_person_pro_percentage = word_percentage(third_person_pro_count, total_number_of_eng_words)
        third_person_per.append(third_person_pro_percentage)
        print(third_person_pro_count)
        print(third_person_pro_percentage)

        print(colored('percentage and count of wordlength > 6', 'green'))
        word_than_six = word_length(lemmatized_message)
        word_than_six_perc = word_percentage(word_than_six, total_number_of_words)
        word_per.append(word_than_six_perc)
        print(word_than_six)
        print(word_than_six_perc)

        semantic_perc_dic = semantic_analysis(eng_words, total_number_of_eng_words)
        angry = semantic_perc_dic['angry_perc']
        angry_perc.append(angry)

        anticipation = semantic_perc_dic['anticipation_perc']
        anticipation_perc.append(anticipation)

        disgust = semantic_perc_dic['disgust_perc']
        disgust_perc.append(disgust)

        fear = semantic_perc_dic['fear_perc']
        fear_perc.append(fear)

        joy = semantic_perc_dic['joy_perc']
        joy_perc.append(joy)

        negative = semantic_perc_dic['negative_perc']
        negative_perc.append(negative)

        positive = semantic_perc_dic['positive_perc']
        positive_perc.append(positive)

        sadness = semantic_perc_dic['sadness_perc']
        sadness_perc.append(sadness)

        surprise = semantic_perc_dic['surprise_perc']
        surprise_perc.append(surprise)

        trust = semantic_perc_dic['trust_perc']
        trust_perc.append(trust)



    print(word_per)
    print(first_person_per)
    print(second_person_per)
    print(third_person_per)
    print('--------------------------------------------------------')

    csv_modify(word_per, first_person_per, second_person_per, third_person_per, angry_perc, anticipation_perc, disgust_perc, fear_perc, joy_perc, negative_perc, positive_perc, sadness_perc, surprise_perc, trust_perc)




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


def eng_words_only(text):
    res = re.findall(r"[a-z]*", text)
    without_empty_strings = [string for string in res if string != ""]
    # print(colored('without_empty_strings', 'green'), without_empty_strings)
    return without_empty_strings


def word_percentage(pro_count, total_eng_count):

    try:
        pro_percent = (pro_count / total_eng_count)*100
    except ZeroDivisionError:
        pro_percent = 0

    return pro_percent


def csv_modify(word_len, first_pro, sec_pro, third_pro, angry_perc, anticipation_perc, disgust_perc, fear_perc, joy_perc, negative_perc, positive_perc, sadness_perc, surprise_perc, trust_perc):
    data = pd.read_csv('TotalDataSet.csv')
    data['first_pro_per'] = pd.Series(first_pro)
    data['second_pro_per'] = pd.Series(sec_pro)
    data['third_pro_per'] = pd.Series(third_pro)
    data['word_len_per'] = pd.Series(word_len)
    data['angry_perc'] = pd.Series(angry_perc)
    data['anticipation_perc'] = pd.Series(anticipation_perc)
    data['disgust_perc'] = pd.Series(disgust_perc)
    data['fear_perc'] = pd.Series(fear_perc)
    data['joy_perc'] = pd.Series(joy_perc)
    data['negative_perc'] = pd.Series(negative_perc)
    data['positive_perc'] = pd.Series(positive_perc)
    data['sadness_perc'] = pd.Series(sadness_perc)
    data['surprise_perc'] = pd.Series(surprise_perc)
    data['trust_perc)'] = pd.Series(trust_perc)
    # print(colored('datasetwithpronouns','red'),data)
    # print(data.info())

    data.to_csv(r'J:\UOM\Education\dataset\copies\2020.2.24\modified_with_sentiments_version2.csv', index=False)
    return data


def emotion_corpus():
    data = pd.read_csv('EmotionLexicon.csv')

    for row in data.itertuples():
        if row.anger == 1:
            angry.append(row.Words)

        if row.anticipation == 1:
            anticipation.append(row.Words)

        if row.disgust == 1:
            disgust.append(row.Words)

        if row.fear == 1:
            fear.append(row.Words)

        if row.joy == 1:
            joy.append(row.Words)

        if row.negative == 1:
            negative.append(row.Words)

        if row.positive == 1:
            positive.append(row.Words)

        if row.sadness == 1:
            sadness.append(row.Words)

        if row.surprise == 1:
            surprise.append(row.Words)

        if row.trust == 1:
            trust.append(row.Words)


def semantic_analysis(text, total_eng):

    emotion_corpus()

    angry_count = 0
    anticipation_count = 0
    disgust_count = 0
    fear_count = 0
    joy_count = 0
    negative_count = 0
    positive_count = 0
    sadness_count = 0
    surprise_count = 0
    trust_count = 0

    angr = []
    antici = []
    disgu = []
    fea = []
    jo = []
    neg = []
    pos = []
    sad = []
    surpr = []
    trus = []

    for i in text:

        if i in angry:
            angry_count += 1
            angr.append(i)

        if i in anticipation:
            anticipation_count += 1
            antici.append(i)

        if i in disgust:
            disgust_count += 1
            disgu.append(i)

        if i in fear:
            fear_count += 1
            fea.append(i)

        if i in joy:
            joy_count += 1
            jo.append(i)

        if i in negative:
            negative_count += 1
            neg.append (i)

        if i in positive:
            positive_count += 1
            pos.append(i)

        if i in sadness:
            sadness_count += 1
            sad.append(i)

        if i in surprise:
            surprise_count += 1
            surpr.append(i)

        if i in trust:
            trust_count += 1
            trus.append(i)

    angry_perc = word_percentage(angry_count, total_eng)
    anticipation_perc = word_percentage (anticipation_count, total_eng)
    disgust_perc =  word_percentage (disgust_count, total_eng)
    fear_perc = word_percentage (fear_count, total_eng)
    joy_perc = word_percentage (joy_count, total_eng)
    negative_perc = word_percentage (negative_count, total_eng)
    positive_perc = word_percentage (positive_count, total_eng)
    sadness_perc = word_percentage (sadness_count, total_eng)
    surprise_perc = word_percentage (surprise_count, total_eng)
    trust_perc = word_percentage (trust_count, total_eng)


    semantic_percetages = {
        'angry_perc': word_percentage(angry_count, total_eng),
        'anticipation_perc': word_percentage(anticipation_count, total_eng),
        'disgust_perc': word_percentage(disgust_count, total_eng),
        'fear_perc': word_percentage(fear_count, total_eng),
        'joy_perc':  word_percentage(joy_count, total_eng),
        'negative_perc': word_percentage(negative_count, total_eng),
        'positive_perc': word_percentage(positive_count, total_eng),
        'sadness_perc': word_percentage(sadness_count, total_eng),
        'surprise_perc': word_percentage(surprise_count, total_eng),
        'trust_perc': word_percentage(trust_count, total_eng)
    }

    print(colored('angry_perc', 'green'), angry_perc)
    print(colored('anticipation_perc', 'green'), anticipation_perc)
    print(colored('disgust_perc', 'green'), disgust_perc)
    print(colored('fear_perc', 'green'), fear_perc)
    print(colored('joy_perc', 'green'), joy_perc)
    print(colored('negative_perc', 'green'), negative_perc)
    print(colored('positive_perc', 'green'), positive_perc)
    print(colored('sadness_perc', 'green'), sadness_perc)
    print(colored('surprise_perc', 'green'), surprise_perc)
    print(colored('trust_perc', 'green'), trust_perc)

    return semantic_percetages


    # csv_pre.to_csv(r'J:\UOM\Education\dataset\copies\2020.2.24\modified_with_sentiments.csv', index=False)



if __name__ == "__main__":
    get_db_data()
    get_post_string()
    preprocess_string()
