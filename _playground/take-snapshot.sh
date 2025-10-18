#!/bin/bash

if [ -f .tutorial.metadata ]; then
  . .tutorial.metadata
  echo "$tutorial_name"
else
  if [ "$1" == "" ]; then
    echo "usage: $0 <tutorial-name>"
    exit
  else
    tutorial_name="$1"
    echo "tutorial_name=$1" > .tutorial.metadata
  fi
fi

sample_folder="../../tutorials/tutorial-generated-examples/$tutorial_name"
rm -rf $sample_folder
mkdir -p $sample_folder

if [ -d "$sample_folder" ]; then
  echo $sample_folder
  cp -r . "$sample_folder"
  cd $sample_folder
  mv .git .git.save
  cd -
  echo "snapshot taken"
fi