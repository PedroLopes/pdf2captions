echo $1
pdf2txt.py $1 > $1.txt
python parseCaptionsFormText.py $1.txt > $1_captions.txt
