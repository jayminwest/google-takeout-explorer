# Google Takeout Explorer

A privacy-focused application for analyzing and visualizing your Google Takeout data.

## Overview

Google Takeout Explorer is a Flask-based web application that helps you gain insights from your Google data exports. The application processes your Google Takeout ZIP files locally, ensuring your data never leaves your machine.

## Features

- **Privacy-First**: All data processing happens locally on your machine
- **Multiple Data Sources**: Analyze Gmail, Location History, and YouTube data
- **Interactive Visualizations**: Explore your data through Plotly visualizations
- **Natural Language Queries**: Ask questions about your data in plain English
- **Secure Processing**: Your data is never sent to external servers

## Installation

### Using Docker (Recommended)

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/google-takeout-explorer.git
   cd google-takeout-explorer
   ```

2. Build and run with Docker Compose:
   ```
   docker-compose up
   ```

3. Open your browser and navigate to http://localhost:5000

### Manual Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/google-takeout-explorer.git
   cd google-takeout-explorer
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r app/requirements.txt
   ```

4. Run the application:
   ```
   python app/app.py
   ```

5. Open your browser and navigate to http://localhost:5000

## Usage

1. Download your Google data from [Google Takeout](https://takeout.google.com/)
2. Select the data you want to analyze (Gmail, Location History, YouTube)
3. Upload the ZIP file to Google Takeout Explorer
4. Explore your data through the interactive visualizations
5. Ask questions about your data using the natural language query interface

## Technical Architecture

The application consists of several components:

- **Flask Web Application**: Handles user interface and file uploads
- **Data Parsers**: Extract and structure data from Google Takeout files
- **Data Analyzers**: Generate insights and visualizations from parsed data
- **Query Interpreter**: Processes natural language queries about your data

## Privacy Considerations

Google Takeout Explorer is designed with privacy in mind:

- All data processing happens locally on your machine
- No data is sent to external servers
- You can delete your processed data at any time
- The application runs in an isolated Docker container

## Troubleshooting

- **File Upload Issues**: Ensure your ZIP file is a valid Google Takeout export
- **Processing Errors**: Check the application logs for detailed error messages
- **Visualization Problems**: Make sure your browser supports JavaScript and WebGL

## License

This project is licensed under the MIT License - see the LICENSE file for details.
