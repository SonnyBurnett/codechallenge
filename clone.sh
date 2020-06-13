#!/usr/bin/env bash

function clone {
    mkdir -p $1
    cd $1
    git clone $2
    cd ..
}

while read repo; do
    clone $repo
done <./repos
