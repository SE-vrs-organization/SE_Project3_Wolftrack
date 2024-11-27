Group 32
Shubham Kakirde, Vinal Bagaria, Rakshita Tantry


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14188177.svg)](https://doi.org/10.5281/zenodo.14188177)
[![GitHub Release](https://img.shields.io/badge/release-v1.0.1.1-blue)](https://github.com/SE-vrs-organization/SE_Project3_Wolftrack)
[![Pytest](https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/actions/workflows/python-build.yml/badge.svg)](https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/actions/workflows/python-build.yml)
[![GitHub license](https://img.shields.io/github/license/SE-vrs-organization/SE_Project3_Wolftrack)](https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/blob/main/License.md)
<a href="https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/SE-vrs-organization/SE_Project3_Wolftrack"></a>
<a href="https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/SE-vrs-organization/SE_Project3_Wolftrack">
<a href="https://github.com/SE-vrs-organization/SE_Project3_Wolftrack/pulls"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/SE-vrs-organization/SE_Project3_Wolftrack">

---

<p align="center">
  <a href="#movie_camera-checkout-our-video">Checkout our video</a>
  ::
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#computer-technology-used">Technology Used</a>
  ::
  <a href="#bulb-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#golf-future-roadmap">Future Roadmap</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  ::
  <a href="#Acknowledgement">Acknowledgement</a>
  ::
  <a href="#email-support">Support</a>
  
</p>

---

:movie_camera: Checkout our video
---

[[https://youtu.be/lyx93075Xkw]](https://www.youtube.com/watch?v=ijOOYHe2Ywc)


---
:rocket: Installation
---

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

:computer: Technology Used
---
- Flask
- SQLite
- Python
- HTML & CSS

:bulb: About WolfTrack 7.0
---

Wolftrack7.0 is an online platform for the easy and efficient organization in your pursuit of internships and full-time job opportunities. This platform allows you to expedite your application process and track every step of your career path. It provides features to help manage job applications, deadlines and important documents (resumes). WolfTrack7.0 is your ticket to success, guiding you through the twisting paths of employment prospects with ease. This platform was created with the intention of helping anyone looking for a job or an internship. It may be a college student in any year, a working professional looking to switch or even someone trying to go into an industry for the first time. It appeals to a diverse audience, and its basic yet strong features make it beneficial to everyone.

:bulb: Use Case
---
1. College Students
  - Scenario: Manage multiple internship applications with varying deadlines.
  - Features:
      - Job tracking, resume reviews, and interview preparation resources.
      - Notifications for upcoming deadlines.
3. Recent Graduates
  - Scenario: Find entry-level positions and build a network.
  - Features:
  - Job recommendations and networking opportunities through events.
  - Bookmark and organize potential roles.
4. Working Professionals
  - Scenario: Transition to new roles or industries.
  - Features:
    - Salary insights for negotiation.
    - Resume parsing to highlight transferable skills.
5. Career Changers
  - Scenario: Identify required skills for new industries.
  - Features:
    - Skill gap analysis and role-specific job suggestions.
    - Resume template customization.
7. Recruiters & Admins
  - Scenario: Review resumes and manage recruitment events.
  - Features:
      - Admin dashboard for centralized resume review.
      - Event organization and feedback tools.

:golf: Phase 7 developments
---
## :sparkles: Enhancements  

### **1. Events Management**  
- **Objective**: Simplify event organization and tracking for students and professionals.  
- **Details**:  
  - Users can seamlessly add new events, including career fairs, webinars, and networking opportunities, to their dashboard.  
  - Real-time updates keep users informed about upcoming events, ensuring they never miss critical opportunities.  
  - **Impact**:  
    Helps users stay organized and actively engage in events that can significantly boost their career prospects.  

---

### **2. Professional Resume Review**  
- **Objective**: Assist users in creating standout resumes tailored to industry standards.  
- **Details**:  
  - Users can upload their resumes to receive professional feedback from platform admins.  
  - Reviews focus on enhancing resume formatting, structure, and content relevance to align with job market expectations.  
  - **Impact**:  
    Significantly improves the quality of user resumes, making them more competitive in the job market.

---

### **3. Admin Comments on Resumes**  
- **Objective**: Provide personalized resume feedback directly from platform admins to students.  
- **Details**:  
  - Admins can review submitted resumes and add detailed, actionable comments tailored to each user.  
  - Feedback is visible to students in their dashboard, allowing them to make revisions promptly.  
  - **Impact**:  
    Offers students a direct avenue to improve their resumes with expert guidance, enhancing their confidence and job application success.

---

### **4. Bookmark Jobs**  
- **Objective**: Enable users to efficiently manage and organize job opportunities for future applications.  
- **Details**:  
  - Users can save jobs of interest directly from the platform, categorizing them based on preferences like role, location, or company.  
  - Bookmarked jobs are displayed in an easily accessible list, allowing users to revisit them without needing to search again.  
  - **Impact**:  
    Streamlines the job application process, making it easier for users to focus on roles that match their goals and preferences.


:golf: Future Roadmap
---

### **1. SMS Notifications**  
- **Objective**: Enhance user engagement and reliability of the platform by delivering real-time reminders through SMS.  
- **Details**:  
  - Integrate SMS services (e.g., Twilio, Plivo) to send personalized reminders.  
  - Allow users to register their phone numbers to receive notifications.  
  - Provide reminders for:  
    - Upcoming application deadlines.  
    - Scheduled interview dates.  
    - Event registrations or job postings.  

---

### **2. Networking Opportunities**  
- **Objective**: Facilitate meaningful connections between job seekers and industry professionals, alumni, or mentors.  
- **Details**:  
  - Create a dedicated networking dashboard where users can:  
    - Search for mentors based on industry, role, or location.  
    - Send connection requests and engage in mentorship.  
    - Access shared resources, such as tips, documents, or webinars.  
  - Enable recruiters to scout talent directly through the platform.  
  - **Advanced Features**:  
    - Schedule virtual coffee chats or Q&A sessions with mentors.  
    - Showcase success stories from users who benefited from networking on the platform.  

---

### **3. Job Recommendations**  
- **Objective**: Provide users with intelligent job suggestions tailored to their preferences, enhancing the discovery of relevant opportunities.  
- **Details**:  
  - Implement **Recommendation Algorithms**:  
    - **Content-Based Filtering**: Match jobs based on user-uploaded resumes and preferences (e.g., skills, industry).  
    - **Collaborative Filtering**: Suggest jobs based on the interests of users with similar profiles.  
    - **Hybrid Models**: Combine content-based and collaborative methods for more accurate recommendations.  
  - Allow users to refine recommendations by:  
    - Specifying preferred locations, roles, or industries.  
    - Excluding unwanted job types (e.g., internships for full-time job seekers).  


---

### **4. Interview Prep Resources**  
- **Objective**: Equip users with the tools and resources needed for successful interview preparation, tailored to specific roles.  
- **Details**:  
  - Add a comprehensive **Interview Prep Tab** with:  
    - **Behavioral Questions**: Common questions and sample answers for topics like teamwork, leadership, and conflict resolution.  
    - **Video Tutorials**: Access to curated videos on improving interview skills, body language, and communication.  
  - Enable users to track their progress with a checklist of interview preparation steps.  
  - Provide downloadable guides, templates, and recommended reading material.  

---

:sparkles: Contributors
---

1. Shubham Kakride (skakird@ncsu.edu)
2. Rakshita Tantry (rtantry@ncsu.edu)
3. Vinal Bagaria (vbagari@ncsu.edu)



## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of Maintaining a good Software Engineering project. We would also like to thank the teaching assistants for their support throughout the project.
We would also like to extend our gratitude to previous group : https://github.com/RAV-Organization/SE_Project1_Wolftrack


:email: Support
---
For any queries and help, please reach out to us at : simlyclipse43@gmail.com

