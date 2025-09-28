sudo apt update

nodejs nvm installation for linux:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 22

install aws cost cli:
npm install -g aws-cost-cli

install aws cli linux:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install

configuring iam:
aws configure

usage commands:
aws-cost
aws-cost --text 
