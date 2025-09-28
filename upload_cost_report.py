from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Your Slack Bot Token (⚠️ don’t hardcode in production, use env vars!)
slack_token = "OAuth_slack_token"
client = WebClient(token=slack_token)

try:
    # upload the file using files_upload_v2
    response = client.files_upload_v2(
        channel="channel_id",             # ✅ singular "channel"
        file="file_to_upload",            # file to upload
        title="name of your file",           # shows as file title
        initial_comment="AWS Cost Report"  # message with file
    )
    print("File uploaded successfully:", response)
except SlackApiError as e:
    print(f"Error uploading file: {e.response['error']}")
