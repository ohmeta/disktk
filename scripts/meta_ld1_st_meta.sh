#TIME=$(date "+%y-%m-%d-%H-%M-%S")
TIME=$(date "+%y-%m-%d-%H")

mkdir -p $TIME

fd -d 1 -t d \
    -E share -E SHR \
    . \
    /ldfssz1/ST_META \
    -x echo fd -j 8 -d 10 . --owner :ST_META {} | \
    awk -F'/' -v time=$TIME '{print $0 " > " time "/" $NF ".list"}' > scan_st_meta.sh.$TIME

chmod u+x scan_st_meta.sh.$TIME

cat scan_st_meta.sh.$TIME
