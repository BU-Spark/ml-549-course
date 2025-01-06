#!/bin/bash

# Render all .qmd files to HTML and Reveal.js
for file in *.qmd; do
  if [ -f "$file" ]; then
    quarto render "$file" --to revealjs --output-dir _revealjs
  fi
done

# Render all .ipynb files to HTML and Reveal.js
for file in *.ipynb; do
  if [ -f "$file" ]; then
    quarto render "$file" --to revealjs --output-dir _revealjs
  fi
done

# revealjs slideshow
#quarto render --to revealjs --output-dir _revealjs
