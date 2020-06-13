#!/usr/bin/env bash

function clone {
    git remote add -f $1 $2
    git merge -s ours --no-commit --allow-unrelated-histories $1/master
    git read-tree --prefix=$1/ -u $1/master
    git commit -m "Merge project $1 as our subdirectory"
}

while read repo; do
    clone $repo
done <./repos
