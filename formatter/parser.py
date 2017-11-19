import yaml
from formatter.words import reserved_toplevel, reserved_newline, functions,boundaries
import re


class Extractor(object):
    def __init__(self, sql_path, format_path):
        self.sql_path = sql_path
        self.format_path = format_path
        self.sql_file = self.load(sql_path)
        self.format_file = self.load(format_path)

    def load(self, path):
        with open(path, 'r') as f:
            if re.match(r'^.*\.yaml$', path):
                return yaml.load(f)
            return f.read()

    def save_as_json(self):
        pass

    def save_as_df(self):
        pass

    def save_to_db(self, db_type):
        pass


class Parser(object):
    def prepare(self, data):
        sql = data.split("\n")
        sql = "\n".join(sql)

        return sql

    def create(self, data, regex=None):
        pass

    def concat_words(self, words):
        words = "\n".join(words)
        return words

    def concat_directives(self, directives):
        pass

    def remove_indent(self, word):
        word = word.replace("\t", '')
        return word

    def remove_space(self, word):
        word = word.replace(" ", '')
        return word

    def remove_each_space(self, words):
        words_ = []
        for word in words:
            word = word.replace(" ", "")
            words_.append(word)
        return words_

    def remove_each_newline(self, words):
        return [word for word in words if word]

    def add_indent(self, word):

        pass

    def change_comma_position(self):
        pass

    def add_new_line(self):
        pass

    def run(self):
        pass

    def add_comma(self):
        pass

    def tr_upper_case(self):
        pass

    def add_space(self):
        pass

    def start_newline_by_reserved_words(self, words):
        words_ =[]
        for word in words:
            # add /n if reserved words
            for r_word in reserved_toplevel:
                r = r"[.\s]*({}).*".format(r_word)
                if re.match(r,word.upper()):
                    # todo: r_word.lower() will be bug
                    word = word.replace(r_word.lower(),r_word+"\n")
                    break
            words_.append(word)
        return words_

    def split_name_ref(self, words):
        """split word like ) aaa or ) as aaa"""
        tred_words = []
        for word in words:
            if re.match(r"\s*\)[\s\w]*\w+", word):
                word = word.split(' ')
                tred_words.extend(word)
                continue
            tred_words.append(word)
        return tred_words

    def split_by_newline(self, words):
        """split word like ) aaa or ) as aaa"""
        tred_words = []
        for word in words:
            word = word.split('\n')
            if word == 1:
                tred_words.append(word[0])
            elif word > 1 :
                tred_words.extend(word)
        return tred_words

    def split_name_and_symbol(self, word):
        if re.match(r"\)\s*\w+", word):
            word = word.split(' ')
            return word
        return word

    def whitespace_between_boundary(self,words):
        words_ = []
        for word in words:
            for boundary in boundaries:
                r = r"[./s]*\{}[./s]*".format(boundary)
                is_boundary = re.search(r,word)
                if is_boundary:
                    boundary = is_boundary.group()
                    word = word.replace(boundary,' ' + boundary + ' ')
                    break
            words_.append(word)
        return words_

