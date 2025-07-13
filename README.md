# Deloitte Australia Technology Job Simulation on Forage - July 2025

 Task -1  Completed a job simulation involving development and coding

 Task -2  Wrote a proposal for creating a dashboard

# Task -1

 
## Goal:
Write a Python program that converts machine telemetry data from two different formats into a single, unified format suitable for displaying on a dashboard.


This is useful for integrating systems where data sources vary, but you need one consistent format to feed into monitoring tools or dashboards.


## ✅ Example Use Case

Imagine you're building a dashboard for a company like Daikibo that monitors machines across multiple factories:

Some older systems export data in ISO format.

Some newer ones use epoch timestamps.

The dashboard backend needs one consistent format to work reliably.

Your Task 1 solution is the data normalization layer that prepares this data — a common requirement in real-world software engineering and system integration.


## 🧪 Testing

The script includes unittest tests that:

Load example JSON files

Run them through your conversion logic

Compare the result to the expected output in data-result.json

If all tests pass: ✅ it means your logic works correctly.

## Skills Acquired

In Task 1, I demonstrated practical skills in handling and transforming structured data using Python. This involved reading and normalizing telemetry data provided in two different JSON formats, each using different field naming conventions and timestamp formats (ISO 8601 vs. epoch milliseconds). I implemented logic to automatically detect the format of each incoming data record and convert it into a unified structure suitable for use in a real-time dashboard application. A key aspect of this task was the conversion of ISO timestamps into epoch milliseconds using Python’s dateutil library, which is critical in systems that rely on consistent time-series data. I structured the code into modular functions, ensuring reusability and clarity, and validated the entire process using unit testing (unittest), reflecting attention to reliability and correctness. This task highlights core backend development skills, including data integration, time format handling, schema normalization, and test-driven development.



## Sample workspace of my work in this job simulation


<img width="1914" height="971" alt="Screenshot 2025-07-13 112349" src="https://github.com/user-attachments/assets/af582940-3d2a-461c-ac62-0ec00b535072" />


 # Task-2

 In Task 2, I authored a formal software development proposal for an internal dashboard solution intended for Daikibo’s machine telemetry monitoring system. The document outlines the architecture and delivery plan for a secure, intranet-based dashboard that displays real-time and historical health status of 9 machines across 4 factories. The solution includes collapsible and expandable views at both the factory and device level, and integrates with the company’s internal authentication server to support Single Sign-On (SSO) using existing enterprise credentials. The proposal clearly defines the project scope, covering key functionalities such as real-time telemetry visualization, authenticated access, responsive UI design, and structured device data handling. It also includes a detailed estimate of total development effort (140 man-hours), broken down into design, development, testing, and deployment phases. A milestone-based timeline and post-deployment support strategy were also documented, ensuring maintainability and long-term usability. This task reflects strong skills in requirements analysis, solution planning, stakeholder communication, and technical documentation — all essential in client-facing software engineering roles.

 

