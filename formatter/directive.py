from formatter.parser import Extractor
from formatter.parser import Parser
from formatter.block import Block
from formatter.words import reserved_toplevel, reserved_newline, functions
import re


class Directive(Parser):
    def __init__(self,format):
        self.data = ""
        self.id = 0
        self.format = format

    # def create(self):
    #     pass

    re_with_directive_withou_with = re.compile(r"\,\s?\w+as[\s\w\(\,\`\.]+.*\)")

    def is_within_select(self):
        pass

    def create_with(self):
        # extract with directive
        r = re.compile(r"(with[\s\w\(\)\,\`\.\=]+)\,\w+\s*\w*\s*\(")
        directive = re.findall(r, self.data)[0]
        directive = list(map(lambda s: self.remove_indent(s.split('\n')[0]), directive.split('\n')))

        self._find_blocks(directive)

        # todo : replace new blocks
        # todo : reshape words within directive tip layer



        # return self.concat_words(directive)
    def _find_blocks(self,directive):
        if '(' or ')' in directive:
            directive.pop(0)
            directive.pop()
            block = Block(directive)
            block.parse_block()


    def __repr__(self):
        return """%s""" % self.id

