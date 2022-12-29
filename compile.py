"""
use this script to compile the html file to a c++ header file, encoded as a list of bytes
"""

import gzip
import os
import sys


if os.path.exists("html.h"):
    os.remove("html.h")

if len(sys.argv) != 2:
    print("Please enter the path to the html file")
    exit(-1)

input_path = sys.argv[1]

if not os.path.exists(input_path):
    print("Input file does not exist!")
    exit(-1)

with open(input_path, "rb") as input_file:
    data = input_file.read()
    out = gzip.compress(data)
    text = out.hex(" ")

    with open("html.h", "w+") as output_txt:
        entries = text.split(" ")
        size = len(entries)

        output_txt.write("#ifndef HTML_H\n")
        output_txt.write("#define HTML_H\n\n")
        output_txt.write("#include <Arduino.h>\n\n")
        output_txt.write(f"#define html_size {size}\n\n")
        output_txt.write("static const uint8_t index_html[] PROGMEM = {")

        for i, val in enumerate(entries):
            buffer = ""
            if i % 50 == 0:
                buffer += "\n"
            buffer += "0x" + val
            if i < size:
                buffer += ","
            output_txt.write(buffer)

        output_txt.write("\n};\n\n")
        output_txt.write("#endif")

