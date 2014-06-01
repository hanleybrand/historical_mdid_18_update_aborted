shopt -s nullglob


for f in *.html
do
	fn=$(basename "$f")
	ext="${fn##*.}"
	fjn="${fn%.*}"
	echo "converting  $f to $fjn.rst"
    pandoc -s -r html -t rst "$f" -o "$fjn.rst"
done
