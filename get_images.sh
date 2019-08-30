while read name; do
    file=$(find gsv_zip_imgs/ -name "$name")
    cp $file ./input_img
done < img_names.txt
    
