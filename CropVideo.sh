#!/bin/sh
ffmpeg -i $1 -r 1/1 $filename%03d.png
for file in *.png; do convert -gravity East -crop 50%x100% $file $file; done

