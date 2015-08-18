#!/bin/bash
echo Generating captions from PDF file "$*"
START=$(date +%s)
pdf2txt.py "$*" > "$*".txt
python parseCaptionsFormText.py "$*".txt > "$*"_captions.txt
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Captions generated, see "$*"_captions.txt, took $DIFF seconds"

