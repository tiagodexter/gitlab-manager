import argparse
import gitlab
import re

def authenticate_gitlab(url, token):
    """Authenticates with GitLab using the provided URL and access token."""
    return gitlab.Gitlab(url, private_token=token)

def get_project_jobs(gl, project_id):
    """Fetches the jobs for a specified project."""
    project = gl.projects.get(project_id)
    return project.jobs.list()

def analyze_job_status(jobs):
    """Analyzes the job status and identifies common issues."""
    issues = []
    for job in jobs:
        if job.status == 'failed':
            issues.append({
                'job_id': job.id,
                'status': job.status,
                'log': fetch_job_log(job),
                'issue_type': 'failed'
            })
        elif job.status == 'success' and is_flaky(job):
            issues.append({
                'job_id': job.id,
                'status': job.status,
                'log': fetch_job_log(job),
                'issue_type': 'flaky_test'
            })
        elif job.duration > 600:  # 600 seconds (10 minutes) threshold for slow builds
            issues.append({
                'job_id': job.id,
                'status': job.status,
                'log': fetch_job_log(job),
                'issue_type': 'slow_build'
            })
    return issues

def fetch_job_log(job):
    """Fetches the log for a specified job."""
    return job.trace()

def is_flaky(job):
    """Checks if a job is marked as flaky based on its name or log."""
    flaky_keywords = ['flaky', 'unstable']
    for keyword in flaky_keywords:
        if re.search(keyword, job.name, re.IGNORECASE) or re.search(keyword, fetch_job_log(job), re.IGNORECASE):
            return True
    return False

def generate_alerts(issues, output_format):
    """Generates alerts in the specified output format."""
    if output_format == 'text':
        for issue in issues:
            print(f"Issue Type: {issue['issue_type']}")
            print(f"Job ID: {issue['job_id']}")
            print(f"Status: {issue['status']}")
            print(f"Log: {issue['log']}")
            print("---")
    elif output_format == 'json':
        alerts = []
        for issue in issues:
            alert = {
                'issue_type': issue['issue_type'],
                'job_id': issue['job_id'],
                'status': issue['status'],
                'log': issue['log']
            }
            alerts.append(alert)
        print(json.dumps(alerts))
    # Add support for other output formats (CSV, etc.) if needed

def main():
    parser = argparse.ArgumentParser(description='GitLab Job Monitoring Tool')
    parser.add_argument('--url', required=True, help='GitLab instance URL')
    parser.add_argument('--token', required=True, help='GitLab access token')
    parser.add_argument('--project', required=True, help='GitLab project ID')
    parser.add_argument('--output', default='text', help='Output format (text/json/csv)')
    args = parser.parse_args()

    gl = authenticate_gitlab(args.url, args.token)
    jobs = get_project_jobs(gl, args.project)
    issues = analyze_job_status(jobs)
    generate_alerts(issues, args.output)

if __name__ == '__main__':
    main()

