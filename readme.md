📊 AWS Cost Monitoring & Slack Notifications

*This project automates AWS cost reporting and sends daily updates to a Slack channel using:

*AWS CLI + Cost Explorer

*aws-cost-cli

*Slack SDK (Python)

*Cron job for automation

*Easily monitor AWS service usage and keep your team informed directly in Slack.

🚀 Features

*Get AWS cost reports with a single command.

*Send cost details directly to a Slack channel.

*Automate daily cost reporting using cron jobs.

*Export AWS cost data in text & file format.

*IAM policy restricted to only ce:GetCostAndUsage and iam:ListAccountAliases for security.

🛠️ Prerequisites

*Linux system (Ubuntu/Debian recommended)

*Node.js & NVM

*AWS CLI v2

*Slack Workspace & Bot Token

*IAM User with Cost Explorer access

⚙️ Installation & Setup

1. Update system
      
    sudo apt update

2. Install Node.js (via NVM)

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    . "$HOME/.nvm/nvm.sh"
    nvm install 22

3. Install AWS Cost CLI

   npm install -g aws-cost-cli

4. Install AWS CLI

   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   sudo apt install unzip
   unzip awscliv2.zip
   sudo ./aws/install

5. Configure AWS

   aws configure

IAM Policy (policy.json):
    
    {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "iam:ListAccountAliases",
        "ce:GetCostAndUsage"
      ],
      "Resource": "*"
    }
  ]
}



🤖 Slack Setup

1)Go to app.slack.com → Create a new workspace (if not already).

2)Create a private channel for cost reports.

3)Go to Slack API Apps → Create a new app from scratch.

4)In OAuth & Permissions, add:

    chat:write

    chat:write.public

    files:write

5)Install the app → Copy the OAuth Bot Token.

6)Go to your Slack channel → Copy the Channel ID.

7)Invite the bot to the channel:
    /invite @your-app-name


📤 Uploading AWS Cost Report to Slack

1. Generate cost report

    aws-cost --text > file_to_upload

2. Python script (upload_cost_report.py)

   from slack_sdk import WebClient
   from slack_sdk.errors import SlackApiError

   slack_token = "YOUR_OAUTH_SLACK_TOKEN"
   client = WebClient(token=slack_token)

   try:
      response = client.files_upload_v2(
          channel="YOUR_CHANNEL_ID",
          file="file_to_upload",
          title="AWS Cost Report",
          initial_comment="Here is the latest AWS Cost Report 📊"
      )
      print("File uploaded successfully:", response)
   except SlackApiError as e:
      print(f"Error uploading file: {e.response['error']}")

  Run:
     python3 upload_cost_report.py

⏰ Automating with Cron

    Edit crontab:

        crontab -e

    Add job (runs every day at 9 AM):

        0 9 * * * /usr/bin/python3 /path/to/upload_cost_report.py >> /path/to/slack_cron.log 2>&1

📌 Usage

   Get cost report:

      aws-cost

   Text format:

      aws-cost --text

   Send directly to Slack:

      aws-cost --slack-token <your_token> --slack-channel <channel_id>


