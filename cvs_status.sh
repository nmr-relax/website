#!/bin/sh

cvs st | grep -P "^[?F]" | grep -v "Up-to-date"
