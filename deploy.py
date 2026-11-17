
import os
import subprocess
import sys


def run_command(command):
    """Execute a shell command and stop if it fails."""
    print(f"\nExecuting: {' '.join(command)}")

    result = subprocess.run(command, text=True)

    if result.returncode != 0:
        print("ERROR: Command failed.")
        sys.exit(result.returncode)

    return result


def main():
    project_id = os.getenv("GCP_PROJECT_ID")
    region = os.getenv("GCP_REGION", "asia-south1")
    service_name = os.getenv("SERVICE_NAME", "gcp-cloud-practical")

    if not project_id:
        print("ERROR: GCP_PROJECT_ID is not set.")
        sys.exit(1)

    print("Starting Cloud Run deployment automation...")
    print(f"Project: {project_id}")
    print(f"Region: {region}")
    print(f"Service: {service_name}")

    run_command(["gcloud", "config", "set", "project", project_id])

    run_command([
        "gcloud", "run", "services", "describe", service_name,
        "--region", region,
        "--project", project_id
    ])

    print("\nCloud Run service verification completed.")


if __name__ == "__main__":
    main()
