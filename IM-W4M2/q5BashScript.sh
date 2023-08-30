#!/bin/bash
file='q5Data.txt'
declaredNumber=153
#FILE READ, 
#COMPARE, IF DATA>153 , save greaterThan153.txt, else save lessthen153.txt
while read -r line; do
  if [[ $line -gt $declaredNumber ]]
   then
      echo $line >> "greterThan153.txt"
  else
      echo $line >> "lessThan153.txt"  
  fi

done < $file
