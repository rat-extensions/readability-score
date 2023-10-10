# readability-score


Description: A Python tool that extracts the main text content of a web document and analyzes its readability.
Input data: URL or/ Search Query.
Output data: for a URL: the output is the detected language, and the readability score is calculated with different formulae and average reading time. For search query: the output is a list of the first 10 Google search results with the option to either analyze a specific result or all of them.
Installation: install dependencies mentioned in Readme.txt. and then Run app.py.
Notes: Supported Languages (EN, DE, AR).

make sure Python is installed if not: https://www.python.org

before running the tool the following dependencies need to be installed:

https://github.com/adbar/trafilatura

$ pip install trafilatura # pip3 where applicable

https://pypi.org/project/urllib3/

$ pip install urllib3


https://github.com/psf/requests

$ python -m pip install requests

https://github.com/psf/requests-html

$ pipenv install requests-html

https://pypi.org/project/textstat/

$ pip install textstat

https://pypi.org/project/emoji/

$ pip install emoji


https://github.com/Mimino666/langdetect

$ pip install langdetect

to run it

$ /bin/python3 app.py
