#!/bin/bash

test() {
    case "$1" in
        patch*) echo "patch" ;;
        feature*) echo "minor" ;;
        release*) echo "major" ;;
        *) echo "none" ;;
    esac
}

test "feature22"
test "release/a"
test "patch.bb"
test "release-valery"
test "boom"
