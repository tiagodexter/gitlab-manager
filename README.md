# GitLab Job Monitoring Tool

The GitLab Job Monitoring Tool is a Python-based tool that connects to a GitLab instance using the GitLab API and monitors the status of jobs in a specified GitLab project. It implements pattern recognition for common issues, such as failed jobs, flaky tests, or slow builds, and generates early alerts in a readable format. The tool provides a simple command-line interface for users to interact with.

## Prerequisites

- Python 3.6 or above
- `python-gitlab` package: Install it using `pip install python-gitlab`.

## Installation

1. Clone the repository or download the code files.

2. Install the required Python packages by running the following command:
pip install -r requirements.txt


## Usage

To use the GitLab Job Monitoring Tool, follow these steps:

1. Obtain a GitLab access token with the appropriate permissions to access the desired GitLab instance and project.

2. Open a terminal or command prompt and navigate to the directory where the tool's files are located.

3. Run the tool with the following command:
python gitlab_job_monitor.py --url <gitlab_url> --token <access_token> --project <project_id> [--output <output_format>]

Replace the placeholders with the appropriate values:
- `<gitlab_url>`: The URL of your GitLab instance.
- `<access_token>`: Your GitLab access token.
- `<project_id>`: The ID of the GitLab project you want to monitor.
- `<output_format>` (optional): The desired output format. Choose from text, json, or csv. (Defaults to 'text')

Example command:
python gitlab_job_monitor.py --url https://gitlab.example.com --token <your_token> --project 12345 --output text


4. The tool will connect to the specified GitLab instance, fetch the job statuses for the project, analyze common issues, and generate alerts in the specified output format.

## Output

The tool generates alerts in the specified output format, providing relevant information about identified issues, affected jobs, and specific log entries.

- Text format: Alerts are displayed in the console as text.
- JSON format: Alerts are displayed as a JSON array of objects.
- CSV format: Alerts are saved to a CSV file.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance the tool based on your specific requirements.

If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

Enjoy monitoring your GitLab CI/CD pipelines with the GitLab Job Monitoring Tool!



