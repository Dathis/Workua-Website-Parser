from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Make a request to the URL of the web page


def get_data(url, end_page):
    df = pd.DataFrame(columns=["Title", "Salary", "Company", "Experience",
                               "Employment Type", "Is_Hot", "Link"])

    for page_number in range(1, end_page + 1):
        response = requests.get(url.format(page_number))

        if response.status_code == 200:

            # Get the HTML content of the page
            html_content = response.content

            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(html_content, "lxml")

            # Make a pattern to gather all divs where classnames starting with this card card-hover card-visited
            pattern = re.compile("^card card-hover card-visited.*")

            # Finding all divs on a page
            divs = soup.find_all("div", class_=pattern)
            for div in divs:
                """
                Looking a data for this columns:
                title; link; salary; company_name; is_hot; experience; employment_type; 
                """

                title = div.find("h2").find("a").text
                link = "https://www.work.ua" + div.find("h2").find("a").get("href")

                try:
                    salary = div.find("div", class_=None).find("b").text
                    # Remove Unicode from salary
                    salary = salary.replace("\u202f", "").replace("\u2009", "").replace("\xa0", "")
                except AttributeError:
                    salary = None

                company_name = div.find("div", class_="add-top-xs").find("span").find("b").text
                if div.get("class")[-1] == "js-hot-block":
                    is_hot = "HOT"
                else:
                    is_hot = "Simple"
                experience = div.find("p").text.split(".")[1]
                if "Опыт работы" in experience:
                    experience = experience.split("работы")[1]
                else:
                    experience = None

                employment_type = div.find("p").text.split(".")[0].replace(" ", "").replace("\n", "")
                # Add current job to a Frame
                job = pd.DataFrame(
                    {"Title": [title], "Salary": [salary], "Company": [company_name], "Experience": [experience],
                     "Employment Type": [employment_type], "Is_Hot": [is_hot], "Link": [link]})
                df = pd.concat([df, job], ignore_index=True)
        else:
            return "ERROR"
    # Making csv
    df.to_csv("WorkUa.csv", index=False)


def show_data():
    df = pd.read_csv("WorkUa.csv")
    print(df)
    print("Number of rows: " + str(df.count()[0]))


if __name__ == "__main__":
    get_data("https://www.work.ua/ru/jobs-remote/?page={}", 4)
    show_data()
