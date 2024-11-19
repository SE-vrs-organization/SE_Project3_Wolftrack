Group 32
Shubham Kakirde, Vinal Bagaria, Rakshita Tantry

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10211531.svg)](https://doi.org/10.5281/zenodo.14014887)
[![GitHub Release](https://img.shields.io/badge/release-v1.0.1.1-blue)](https://github.com/SE-vrs-organization/slash-backend)
[![Black Python](https://github.com/SE-vrs-organization/slash-backend/actions/workflows/blackformatting.yaml/badge.svg)](https://github.com/SE-vrs-organization/slash-backend/actions/workflows/blackformatting.yaml)
[![GitHub license](https://img.shields.io/github/license/SE-vrs-organization/slash-backend)](https://github.com/SE-vrs-organization/slash-backend/blob/main/License.md)
<a href="https://github.com/SE-vrs-organization/slash-backend/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/SE-vrs-organization/slash-backend"></a>
<a href="https://github.com/SE-vrs-organization/slash-backend/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/SE-vrs-organization/slash-backend">
<a href="https://github.com/SE-vrs-organization/slash-backend/pulls"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/SE-vrs-organization/slash-backend">

## Getting Started & Installation:

- ### Prerequisite:

  - Download [Python3.x](https://www.python.org/downloads/).

- ### Installation:

  E.g If you downloaded `Python 3.8.7` above, then

  **Steps to setup virtual environment**

  - Create a virtual environment:

    `python3.8 -m venv test_env`

  - Activate the virtual environment:

    `source test_env/bin/activate`

  - Build the virtual environment:(must be present in project root directory)

    `pip install -r requirements.txt`

- ### Run Instructions

  **To run/test the site locally:**

  - Clone

  - Navigate to project directory.

  - Run `python main.py` or `python3 main.py` <br> <br>
    If there is a certificate error coming up for nltk stopwords download: <br>

    - search for "Install Certificates.command" in finder and open it. Its a script that will install required Certificates. <br>
    - Run the above command again.

  - Site will be hosted at:
    `http://127.0.0.1:5000/`

## Roadmap

### About WolfTrack 6.0:

Wolftrack6.0 is an online platform for the easy and efficient organization in your pursuit of internships and full-time job opportunities. This platform allows you to expedite your application process and track every step of your career path. It provides features to help manage job applications, deadlines and important documents (resumes). WolfTrack6.0 is your ticket to success, guiding you through the twisting paths of employment prospects with ease. This platform was created with the intention of helping anyone looking for a job or an internship. It may be a college student in any year, a working professional looking to switch or even someone trying to go into an industry for the first time. It appeals to a diverse audience, and its basic yet strong features make it beneficial to everyone.

### About WolfTrack 5.0:

1. Centralized Job Application Management
   It centralizes all job application information, including deadlines, statuses, and documents, into a single, user-friendly dashboard. This eliminates the need to rely on various tools such as spreadsheets, email threads and notebooks. This makes the process more organized and less stressful.

2. Built-in Deadline Alerts
   Previously, users risked missing important deadlines without a reminder system to tell them of application dates and deadlines. With built-in alert mechanisms, it ensures users never miss application deadlines, providing peace of mind and reducing the chances of missing opportunities.

3. Streamlined Resume Upload and Download
   Some job applications may require different versions of resumes and managing as well as sharing them with potential employers could be difficult and hard to track. WolfTrack 5.0 allows users to upload, download, and store multiple versions of their resume seamlessly. This ensures that resumes are easily accessible and up-to-date.

4. Comprehensive CRUD Operations for Applications
   WolfTrack 5.0 offers full CRUD (Create, Read, Update, Delete) functionality, allowing users to easily add new applications, update statuses, and remove old or irrelevant entries. This elimates the need to manually manage applications with no structured way to edit, update, or delete job application records.

5. Enhanced User Experience with Filter by Status Feature
   The "Filter by Status" feature allows users to view applications based on their progress (e.g., applied, in process, offer received). This makes it much easier to focus on priority tasks and manage multiple applications efficiently.

### Future Scope

1. Web Scrapping for recommended jobs

- Utilize Python libraries like BeautifulSoup and Selenium to scrape job postings from websites like LinkedIn, Indeed, Glassdoor, etc.

2. Send reminders through SMS notification.

- Include an option of providing contact number to receive SMS notifications based on interview dates and job deadlines.

3. Interview preparation resources tab.

- Include a detailed tab for interview preparation resources including behavioural questions and questions tailored to specific roles.

4. Salary insights and comparisons.

- Use visualization libraries to show salaries for different roles based on factors like locations, job roles, years of experience.

5. Resume template editor.

- Provides users with an option to directly edit and make changes in their resume on the website.
