# Citation Fetcher using Semantic Scholar API

This project provides Python scripts to retrieve details of a research paper and its citations from the Semantic Scholar API. The main functionality includes fetching the title, abstract, year, and citation information for papers that cite a specific research paper. Citations are saved into a text file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [File Description](#file-description)
- [API Rate Limits](#api-rate-limits)
- [License](#license)

## Installation

1. **Python**: Ensure you have Python 3.x installed on your system.
2. **Install dependencies**: The only required library for this project is `requests`, which you can install using pip.

    ```bash
    pip install requests
    ```

## Usage

1. **Run the script**: To use this script, simply run the Python file:

    ```bash
    python web_crawl.py
    ```

2. **Input the paper ID**: You will be prompted to enter the paper ID from Semantic Scholar. You can find the paper ID by searching the paper on the [Semantic Scholar website](https://www.semanticscholar.org/) and extracting the ID from the URL of the paper's page.

    Alternatively, the script already contains a hardcoded example paper ID (`2a47759c48bf8d14d2caa54bcc4bd03c1eee6135`).

3. **View results**: The citations will be filtered based on the provided `year_filter` (default is 2023), and the results will be written to a file named `citations_output.txt` in the current directory.

## How It Works

1. **Fetching Paper Details**: The function `get_paper_details(paper_id)` sends an API request to fetch a paper's details such as the title, abstract, and publication year using the Semantic Scholar Paper API.

2. **Fetching Citations**: The `get_citations(paper_id, year_filter)` function retrieves citations of the given paper using the Semantic Scholar Graph API. It fetches citing papers in batches and filters them based on the publication year (`year_filter`). The citation details are written to a text file (`citations_output.txt`).

3. **Pagination Handling**: The script handles pagination by fetching 100 citations at a time and adjusting the `offset` value until no more citations are available.

4. **Output**: The filtered citations (those published after the `year_filter`) are displayed on the console and written to `citations_output.txt`.

## Example Output

The output in the `citations_output.txt` file will look like this:
