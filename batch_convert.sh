#!/bin/bash

pushd $1

mkdir srt
find ./ -name '*.vtt' | sed 's/.vtt//g' | xargs -I {} sh -c "../tosrt.py '{}.vtt' > 'srt/{}.srt'"
