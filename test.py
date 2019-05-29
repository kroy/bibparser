from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

lang = "eng"
img_path = 'test_images/rise-and-kill-first/rise-and-kill-first_2.jpg'

txt = tool.image_to_string(
    Image.open(img_path),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# txt is a Python string
print(txt)

word_boxes = tool.image_to_string(
    Image.open(img_path),
    lang=lang,
    builder=pyocr.builders.WordBoxBuilder()
)
# list of box objects. For each box object:
#   box.content is the word in the box
#   box.position is its position on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

line_and_word_boxes = tool.image_to_string(
    Image.open(img_path), lang=lang,
    builder=pyocr.builders.LineBoxBuilder()
)

for line in line_and_word_boxes:
    print(line.position, line.content)

if tool.can_detect_orientation():
    try:
        orientation = tool.detect_orientation(
            Image.open(img_path),
            lang=lang
        )
        print("Orientation: {}".format(orientation))
    except pyocr.PyocrException as exc:
        print("Orientation detection failed: {}".format(exc))
# list of line objects. For each line object:
#   line.word_boxes is a list of word boxes (the individual words in the line)
#   line.content is the whole text of the line
#   line.position is the position of the whole line on the page (in pixels)
#
# Each word box object has an attribute 'confidence' giving the confidence
# score provided by the OCR tool. Confidence score depends entirely on
# the OCR tool. Only supported with Tesseract and Libtesseract (always 0
# with Cuneiform).
#
# Beware that some OCR tools (Tesseract for instance) may return boxes
# with an empty content.

# Digits - Only Tesseract (not 'libtesseract' yet !)
#digits = tool.image_to_string(
#    Image.open('test-digits.png'),
#    lang=lang,
#    builder=pyocr.tesseract.DigitBuilder()
#)
# digits is a python string


