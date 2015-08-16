# pdf2captions
Outputs a list of captions from a target pdf, done for UIST 2015 accessibility options. 

This was made for UIST/CHI templates and might work with others however there are very strict (perhaps lame) assumptions:

1. a caption starts with "Figure" followed by whitespace and a number (digits) and a ":" and some text.

2. The caption ends IMPERATIVELY on a period ("."). If not, it will continue until a period is found.

# how to run
Put the pdf in the local directory. 

Then type:

./run.sh <pdfname.pdf>

It will output a file called <pdfname.pdf_captions.txt> with all your captions.

# how to install
Please install pdfminer first. (for instance: easy_install pdfminer)
