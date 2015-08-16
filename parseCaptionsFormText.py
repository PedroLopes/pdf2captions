import sys
import re

#Note: this parser is failing for the edge case in which one of the middle lines in a caption ends exactly at the period. All other cases (tested) work. 

target_file = sys.argv[1]
figure_labels = ["figure", "fig"]
caption = []
OUTPUT = True
DEBUG = False
debug_string = "DEBUG:"
output_string = ""
waiting_for_caption_to_end = False
caption_lines = []
captions_captured = []
figure_number = ""

with open(target_file) as f:
    for line in f:
        #print line
        line_words = line.split()
        if (DEBUG): print(debug_string+"".join(line_words))
        if (waiting_for_caption_to_end and len(line_words) >= 1):
            if (DEBUG): print(debug_string+"upper")
            caption_lines.append(line.replace("\n",""))
            if (line_words[len(line_words)-1].endswith('.') == True):
                    caption_text = " ".join(caption_lines).replace("\n","").replace("- ","").replace("  "," ")
                    pair = [figure_number,caption_text]
                    captions_captured.append(pair)
                    waiting_for_caption_to_end=False
                    #print(output_string+" ".join(caption_lines).replace("\n","").replace("- ","").replace("  "," "))
                    caption_lines = []
                    #if (OUTPUT): print(output_string) #and print a new line
        elif (len(line_words)>=2):
            if (DEBUG): print(debug_string+"lower")
            figure = (line_words[0]).lower() #only first word of each sentence should be "Figure"
            figure_number = line_words[1].lower()
            if (figure in figure_labels and figure_number.endswith(':')):
                    #if (OUTPUT): print(output_string+figure+" "+figure_number[:-1])
                    figure_number = output_string+figure+" "+figure_number[:-1]
                    for word in line_words[2:]:
                        caption.append(word)
                    caption_lines.append(" ".join(caption))
                    if (line_words[len(line_words)-1].endswith('.') == False):
                        waiting_for_caption_to_end = True
                    elif (OUTPUT): 
                        caption_text = output_string+" ".join(caption_lines).replace("\n","")
                        #print(output_string+" ".join(caption_lines).replace("\n",""))
                        pair = [figure_number,caption_text]
                        captions_captured.append(pair)
                        #print(output_string)
                    caption = []

#lame determining of figure count on the paper
max_number = 0
for pair in captions_captured:
    number = int(pair[0].replace("figure ", ""))
    if number > max_number:
        max_number = number
if (DEBUG): print max_number
iterator = 1

#print in order
while (iterator <= max_number):
    for pair in captions_captured:
        if (int(pair[0].replace("figure ", "")) == iterator):
            print(pair[0])
            print(pair[1])
            print("")
    iterator+=1
