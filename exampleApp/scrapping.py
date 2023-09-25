import requests
from bs4 import BeautifulSoup


def scrapp_jobs():
    jobs_list = []
    page = requests.get("https://realpython.github.io/fake-jobs/")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        job_dict = {
            "title": title_element.text.strip(),
            "company": company_element.text.strip(),
            "location": location_element.text.strip()
        }
        jobs_list.append(job_dict)
    return jobs_list
