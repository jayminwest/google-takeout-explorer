# Google Takeout Explorer API

A privacy-focused API for analyzing and processing your Google Takeout data.

## Overview

Google Takeout Explorer API is a FastAPI-based service that helps you process and gain insights from your Google data exports. The API processes your Google Takeout ZIP files locally, ensuring your data never leaves your machine.

## Features

- **Privacy-First**: All data processing happens locally on your machine
- **Multiple Data Sources**: Process Gmail, Location History, YouTube and other Google Takeout data
- **Data Conversion**: Convert Google Takeout data into more usable file formats
- **Data Analysis Pipeline**: Extract insights and patterns from your data
- **RESTful API**: Access your processed data through a well-documented API
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

3. The API will be available at http://localhost:8000
4. API documentation will be available at http://localhost:8000/docs

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
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

5. The API will be available at http://localhost:8000
6. API documentation will be available at http://localhost:8000/docs

## Usage

1. Download your Google data from [Google Takeout](https://takeout.google.com/)
2. Place your Google Takeout ZIP files in the `data/` directory
3. The API will automatically process these files and convert them to usable formats
4. Access the processed data and analysis through the API endpoints

## Technical Architecture

The application consists of several components:

- **FastAPI Backend**: Provides RESTful API endpoints for data access
- **Data Processors**: Extract and convert data from Google Takeout files
- **Data Analysis Pipeline**: Processes and analyzes the converted data
- **Storage Layer**: Manages processed data in optimized formats

## API Endpoints

- `/api/v1/data/sources`: List all available data sources
- `/api/v1/data/{source}/summary`: Get summary statistics for a specific data source
- `/api/v1/data/{source}/records`: Get detailed records from a specific data source
- `/api/v1/analysis/{analysis_type}`: Run specific analysis on your data

## Privacy Considerations

Google Takeout Explorer API is designed with privacy in mind:

- All data processing happens locally on your machine
- No data is sent to external servers
- You can delete your processed data at any time
- The application runs in an isolated Docker container

## Troubleshooting

- **File Processing Issues**: Ensure your ZIP files are valid Google Takeout exports
- **API Errors**: Check the application logs for detailed error messages
- **Performance Issues**: Consider increasing Docker resource limits for large datasets

## Future Development

This API is the first step toward a full-stack application. Future versions will include:
- A web-based frontend for visualizing the data
- Interactive dashboards for exploring insights
- Natural language query capabilities
- Additional data sources and analysis methods

## License

This project is licensed under the MIT License - see the LICENSE file for details.
