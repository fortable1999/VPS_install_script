# resize all jpg files in current directory
find . -name '*.jpg'  -exec convert -resize 30% {} {}.small.jpg \;
