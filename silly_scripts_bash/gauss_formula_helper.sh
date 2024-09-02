#!/bin/bash

echo "This is a Gauss' formula helper.  This program will illuminate the thinking behind how to add up the first n integers."
echo "We seek to help the user understand the formula 1 + 2 + 3 + ... + n = n*(n+1)/2."
echo "Enter an integer."

read input
  if [[ $input ]] && [ $input -eq $input 2>/dev/null ] && [ $input -ge 0 ]
  then
     echo "$input is a positive integer"
  else
     echo "$input is not a positive integer or not defined"
     echo "Error!"
     exit
  fi

expr $input + $input

for i in $(seq 1 $input);
do
    echo $i
done
