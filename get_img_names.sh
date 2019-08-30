for filename in gsv_label_charlie/*.xml; do
    file="$(basename "$filename" .xml)"
    tag=".jpg"
    name=$file$tag
    echo "$name" >> img_names.txt
done

for filename in gsv_label_andrew/*.xml; do
    file="$(basename "$filename" .xml)"
    tag=".jpg"
    name=$file$tag
    echo "$name" >> img_names.txt
done

for filename in gsv_label_prince/*.xml; do
    file="$(basename "$filename" .xml)"
    tag=".jpg"
    name=$file$tag
    echo "$name" >> img_names.txt
done



