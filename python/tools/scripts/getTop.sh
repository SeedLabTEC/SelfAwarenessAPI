#!/bin/bash
#Constants for the data construction
separator=":"
extension=".txt"
file="./results/"$1$extension
prefixPer="%MEM"
prefixBytes="RSS"
suffixBytes="K"
now="date"
top="top.txt"
#echo "Saving memory of Process: $1"
#Function that get the memory usage percentage
checkMemPer(){
   memoryPer=$(ps -p $1 -o %mem)
   memoryPer=$(echo $memoryPer | sed -e s/^$prefixPer//)
}
#Function that get the memory usage bytes
checkMemBytes(){
   memoryBytes=$(ps -p $1 -o rss)
   memoryBytes=$(echo $memoryBytes | sed -e s/^$prefixBytes//)
}
#Function that concatenate all the information
checkMem(){
    checkMemPer $1
    checkMemBytes $1
    result=$1$separator$memoryBytes$separator$memoryPer$separator$($now)
    echo "$result">>"$file"
}
refactor(){
   tail -n 13 "$top" > "$top.tmp" && mv "$top.tmp" "$top"
}
checkTop(){
   memoryPer=$(top -b -d 5 | head -n 20 )
   #memoryPer=$(echo $memoryPer | sed -e s/^$prefixPer//)
   echo "$memoryPer">"$top"
   
}
#checkMem $1
checkTop
refactor



