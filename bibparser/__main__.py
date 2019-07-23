import os
import sys
import fileinput
from typing import List

from cited import Source, Book
from styles import chicago

def parse_txt(txt_filename, style):
    """
        @TODO turn this into a generic parser that takes an Iterator or something
            typehints for vars
    """
    entries = []
    with open(txt_filename) as txt_file:
        for line in txt_file:
            print("Parsing: ", line.rstrip())
            entries.append(style.parse(line.rstrip()))
    return entries
            

def main():
    """
        @TODO add some info about this parser, what you can expect etc
            - style selection
    """
    try:
        input_dir_or_file = sys.argv[1]
    except IndexError as e:
        # @TODO handle errors opening file/filenotfound
        input_dir_or_file = input("Enter the location of your image or text files: ")
    sources_cited = parse_txt(input_dir_or_file, chicago)
    print(sources_cited)

main()