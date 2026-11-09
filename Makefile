# Build every lesson PDF:  make        Build one:  make lesson01/lesson01_arrays.pdf
# Needs XeLaTeX and the Inter + DejaVu Sans Mono fonts. Shared style lives in style/dsa-style.sty.
TEX := $(wildcard lesson*/*.tex complexity/*.tex)
PDF := $(TEX:.tex=.pdf)

all: $(PDF)

%.pdf: %.tex style/dsa-style.sty $(wildcard lesson*/code/* complexity/code/*)
	cd $(dir $<) && for i in 1 2 3; do \
	  TEXINPUTS=../style//: xelatex -interaction=nonstopmode $(notdir $<) >/dev/null; done
	@cd $(dir $<) && ! grep -E "^!|Overfull" $(notdir $(<:.tex=.log)) || (echo "LaTeX problems above"; exit 1)
	@cd $(dir $<) && rm -f *.aux *.log *.out *.toc *.bkm

clean:
	rm -f lesson*/*.aux lesson*/*.log lesson*/*.out lesson*/*.toc lesson*/*.bkm complexity/*.aux complexity/*.log complexity/*.out complexity/*.toc complexity/*.bkm

.PHONY: all clean
