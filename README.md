Backend Stage One TaskDear Interns,  
Welcome to Stage One.  Objective
Create and host an endpoint using any programming language of your choice.
The endpoint should take two GET request query parameters and return specific information in JSON format.  Requirements
The information required includes:
•	Slack name
•	Current day of the week
•	Current UTC time (with validation of +/-2)
•	Track
•	The GitHub URL of the file being run
•	The GitHub URL of the full source code.
•	A  Status Code of Success
JSON
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
Acceptance Criteria
•	Endpoint Creation: Provide a publicly accessible endpoint.
•	GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.
       E.g.: http://example.com/api?slack_name=example_name&track=backend.
•	Slack Name: The response should include the slack_name passed as a GET request query parameter.
•	Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).
•	Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.
•	Track: The response should display the track of the you signed up for (Backend). This will be based on the track GET parameter passed to the endpoint.
•	GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.
•	GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.
•	Status Code: Return 200 as Integer.
•	JSON Format: The endpoint's response should adhere to the specified JSON format.
•	Testing: Before submission:
•	Ensure the endpoint is accessible.
•	Check the returned JSON against the defined format.
•	Validate the correctness of each data point in the JSON response.
Submission Mode
Please follow these submission guidelines
•	Get into your DM
•	Type /grade <your-api-endpoint-url-with-the-query-parameters>
•	E.g: /grade http://example.com/api?slack_name=example_name&track=backend
•	Check your result
                                                                Very Important.....
•	 Finaly, please use the provided Google Form. Within the form, share the URL of your hosted endpoint, along with the GitHub repository link of the file being run, and where the full source code can be found.
  Before submitting, do a final checkwith the grader bot to ensure that your endpoint is operational and meets the specified requirements. Incomplete or non-functional submissions may affect your evaluation.  Submission Deadline:
•	The deadline for submissions is 12th September 2023, 11:59 PM GMT + 1.
Late submissions will not be entertained .If you encounter any issues or have questions regarding the task or the submission process, please message any backend mentor.Best of luck!
 Google Docs
Backend Stage One Submission (27 kB)
https://forms.gle/zUwsiDyXUJ8pRFmu8
 32  11 10 7

