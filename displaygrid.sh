#!/bin/bash

function main()
{
	python3 scripts/generate_grids.py $1
	python3 scripts/display.py view/grid.html
}

main $@
