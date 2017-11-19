from formatter.parser import Parser
import re


class Block(Parser):
    def __init__(self, directive):
        self.directive = directive

    def parse_block(self):
        self.clean_block()
        blocks = self.is_nested()
        blocks = self.adopt_space(blocks)
        print(blocks)

    def adopt_space(self, blocks):
        new_block = []
        len__ = len(blocks)

        if len__ == 1:
            blocks = self.whitespace_between_boundary(blocks)
        elif len__ > 1:
            blocks = [self.whitespace_between_boundary(block) for block in blocks ]
        return blocks

    def clean_block(self):
        directive = self.start_newline_by_reserved_words(self.directive)
        directive = self.split_by_newline(directive)
        directive = self.split_name_ref(directive)
        directive = self.remove_each_space(directive)
        directive = self.remove_each_newline(directive)

        self.directive = directive
        return directive

    def is_nested(self):

        """
        logic :
            start with '('
            found '('  before  ')' means nested

        :return:
            nested list with block
        """
        blocks = []
        for i, word in enumerate(self.directive):
            # scan nest or not based on (
            if word == '(':
                for i_w, w in enumerate(self.directive[i + 1:]):
                    # found ( here , it means nested
                    if w == '(':
                        break
                    # found ) here means not nested
                    if w == ')':
                        i = i + 1
                        blocks.append(self.directive[i:i + i_w])
                        print(blocks)
                        break
        return blocks

    def create_select(self):
        pass

    def create_from(self):
        pass

    def create_func(self, type):
        pass

    def create_join(self):
        pass
