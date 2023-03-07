#!/bin/bash

test() {
    case "$1" in
        patch*) echo "patch" ;;
        feature*) echo "minor" ;;
        release*) echo "major" ;;
        *) echo "none" ;;
    esac
}

test2(){
    IFS='.' read -ra version <<< "$(echo 0.0.0)"
    case "$1" in
        patch) version[2]=$((version[2]+1)) ;;
        minor) version[1]=$((version[1]+1)); version[2]=0 ;;
        major) version[0]=$((version[0]+1)); version[1]=0; version[2]=0 ;;
    esac
    VERSION="${version[0]}.${version[1]}.${version[2]}"
    echo "$VERSION"
}

test "feature22"
test "release/a"
test "patch.bb"
test "release-valery"
test "boom"

# test2 "minor"
