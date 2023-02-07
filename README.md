# Work.ua Parser

This code is a simple script that parses job data from the Work.ua website and stores it in a csv file. 

## Requirements
- BeautifulSoup
- Requests
- Re
- Pandas

## How it works
- The scrape_data function takes two arguments:
  * url: The URL of the web page to be parsed.
  * end_page: The number of pages to be parsed.
- The function then makes a request to the URL of the web page, and if the response is successful (status code 200), it parses the HTML content of the page using BeautifulSoup.

- The function then finds all the job listings on the page, and for each job, it gathers information about the job title, salary, company name, experience required, employment type, and whether the job is hot or not.

- The gathered information is then added to a pandas DataFrame, which is finally stored in a csv file named "WorkUa.csv".

- The display_data function then reads the csv file and displays its contents in the terminal, along with the number of rows in the DataFrame.

## Usage
- Clone the repository to your local machine.

- Open the terminal and navigate to the project directory.

- Run the script by executing the following command:

```python main.py```
* This will parse the data from the Work.ua website and store it in a csv file, which can be further processed for analysis or used for other purposes.
