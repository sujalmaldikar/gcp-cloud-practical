import google.auth
from google.auth.transport.requests import Request
from google.auth import impersonated_credentials
from google.cloud import storage

SERVICE_ACCOUNT = (
    "gcp-storage-app@optimum-phalanx-514316-j3.iam.gserviceaccount.com"
)

source, project = google.auth.default()

credentials = impersonated_credentials.Credentials(
    source_credentials=source._source_credentials,
    target_principal=SERVICE_ACCOUNT,
    target_scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

credentials.refresh(Request())

print("Authentication successful!")
print("Project:", project)
print("Service Account:", credentials.service_account_email)

client = storage.Client(
    project=project,
    credentials=credentials
)

print("Cloud Storage client initialized successfully!")