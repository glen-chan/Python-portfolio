import pyttsx3, PyPDF2
from PyPDF2 import PdfReader
import argparse

# create the parser (defining what command line arguments are expected)
parser = argparse.ArgumentParser()

# add an argument called "pdf", to input the name of the .pdf file to read
# add an argument called "mp3", to input the name of the .mp3 file to generate
parser.add_argument("--pdf", help="Enter the name of the PDF file to read")
parser.add_argument("--mp3", help="Enter the name of the MP3 file to generate")  

# parse the command line arguments
args = parser.parse_args()

reader = PdfReader(args.pdf)
speaker = pyttsx3.init()
text_to_read = ''

#print("Number of pages of PDF file: {}".format(len(reader.pages)))

for page_num in range(len(reader.pages)):
    text = reader.pages[page_num].extract_text()
    clean_text =  text.strip().replace('\n',' ')
    text_to_read = text_to_read + clean_text
    
print(text_to_read)
    
output_file = args.mp3

if args.mp3 is None:
    output_file = args.pdf[0: len(args.pdf)-3] + 'mp3'
    print("The generated output file name is: {}".format(output_file))
    
speaker.save_to_file(text_to_read, output_file)
speaker.runAndWait()
 
speaker.stop()