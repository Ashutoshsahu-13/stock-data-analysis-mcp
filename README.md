# Stock-data-analysis using MCP server and google drive

##Introduction
This project uses the Model Context Protocol (MCP) to provide access to Google Drive for downloading and uploading files. It also enables analysis of stock data and visualization of the data using various plots.

It allows Claude and other AI assistants to retrieve information through the MCP interface.

##Available Tools
This MCP server tool:
analysis_stock_data: Answers stock data queries and generates relevant plots. 

##Setup
Prerequisites
Python 3.10 or higher
uv package manager

###Installation
1.Clone this repository:

git clone https://github.com/stock-data-analysis-mcp/
cd mcp-server

2.If you don't have uv installed, install it:

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
curl -LsSf https://astral.sh/uv/install.ps1 | powershell

3.Install dependencies:

# Create virtual env and activate it
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv add "mcp[cli]" 

4.Set up environment variables:

# Create .env file for your API keys
cp .env.example .env

# Set API key in .env
GEMINI_API_KEY=API_KEY

5.SET GOOGLE DRIVE CLIENT ID 
Create client_secrets.json and set client id 

6.Run the server:

uv run server.py
