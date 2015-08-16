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

with open(target_file) as f:
    for line in f:
        #print line
        line_words = line.split()
        if (DEBUG): print(debug_string+"".join(line_words))
        if (waiting_for_caption_to_end and len(line_words) >= 1):
            if (DEBUG): print(debug_string+"upper")
            caption_lines.append(line.replace("\n",""))
            if (line_words[len(line_words)-1].endswith(' ') == True):
                if (line_words[len(line_words)-2].endswith('.') == False):
                    waiting_for_caption_to_end = False
                    print(output_string+" ".join(caption_lines).replace("\n","").replace("- ","").replace("  "," "))
                    caption_lines = []
                    if (OUTPUT): print(output_string) #and print a new line
            elif (line_words[len(line_words)-1].endswith('.') == True):
                    waiting_for_caption_to_end=False
                    print(output_string+" ".join(caption_lines).replace("\n","").replace("- ","").replace("  "," "))
                    caption_lines = []
                    if (OUTPUT): print(output_string) #and print a new line
        elif (len(line_words)>=2):
            if (DEBUG): print(debug_string+"lower")
            figure = (line_words[0]).lower() #only first word of each sentence should be "Figure"
            figure_number = line_words[1].lower()
            if (figure in figure_labels and figure_number.endswith(':')):
                    if (OUTPUT): print(output_string+figure+" "+figure_number[:-1])
                    for word in line_words[2:]:
                        caption.append(word)
                    caption_lines.append(" ".join(caption))
                    if (line_words[len(line_words)-1].endswith(' ') == True):
                        if (line_words[len(line_words)-2].endswith('.') == False):
                            waiting_for_caption_to_end = True
                    elif (line_words[len(line_words)-1].endswith('.') == False):
                        waiting_for_caption_to_end = True
                    elif (OUTPUT): 
                        print(output_string+" ".join(caption_lines).replace("\n",""))
                        print(output_string)
                    caption = []
