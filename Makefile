clean:
	find . -name "*.pyc" -exec rm -rf {} \;

shell:
	ipython

run: clean
	python crawler.py