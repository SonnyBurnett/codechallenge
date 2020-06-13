#!/usr/bin/env bash

function pull {
    mkdir -p $1
    cd $1
    git pull
    cd ..
}

while read repo; do
    clone $repo
done <./repos
