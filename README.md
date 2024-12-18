# Wikipedia Concept Data Crawler 🕷️📚

This project is a Python-based web crawler that extracts and processes concept data from Wikipedia articles. It focuses on fetching information like article descriptions, categories, and related links for a deeper understanding of various Wikipedia topics.

## Features ✨

- **Wikipedia Article Extraction** 📖: Crawls through Wikipedia articles to extract data related to concepts.
- **Category Parsing** 🔍: Extracts relevant categories linked to the article.
- **Link Extraction** 🔗: Identifies and extracts related links to other Wikipedia articles.

## Requirements 🔧

Before you begin, ensure you have the following Python libraries installed:

- `requests` — To send HTTP requests and fetch Wikipedia pages.
- `beautifulsoup4` — For parsing HTML content from Wikipedia pages.


You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 pandas sqlite3
```
How to Use 🚀
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/wikipedia-concept-crawler.git

```
Navigate to the project directory:
```bash

cd wikipedia-concept-crawler
```
Run the main script (webcrawler.py):


# Data Output 📊
Links 🔗: A list of related Wikipedia article links.
