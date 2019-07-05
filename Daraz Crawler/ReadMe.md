#  Crawler Using Requests-html library
## This Crawler is specifialyy designed for the Daraz.pk [e-commerce site].

## Prerequesits
> python 3.6 [latest version]

### Download the required libraries using following pip command.
```
pip install requests-html
pip install csv
```
# How to Use this script?
This script will be used by passing single command line argument. Following line will show how to use the script.
## Syntax:
> python script_name.py "Search_Query"
## Example:
> python "Daraz Crawler Using HTMLResponse.py" "samsung j5"

# What Script Will Do?
* requests the html response with the required credentilas.
* scrap the html code using requests_html lib.
* scrap the product name, price , old price, and discount.
* __display__ the results on __console__ and __save__ the data in __csv file__ with query_text on the current working directory.

## Why requests_html ? Why not BeautifulSoup

I used requests_html library because it has more advance features than beautifulsoup.
It has the ability to parse the java script code to reqired html, and the beautiful soup library has not this feature.

---

### Resouce where I have learned it.
[Official Site: www.Coreyms.com](https://coreyms.com/)

[![Youtube Video Link](http://img.youtube.com/vi/a6fIbtFB46g/0.jpg)](http://www.youtube.com/watch?v=a6fIbtFB46g)
