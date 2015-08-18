echo "$*"
pdf2txt.py "$*" > "$*".txt
python parseCaptionsFormText.py "$*".txt > "$*"_captions.txt
