from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path

app = FastAPI(
    title="Google Takeout Explorer API",
    description="A privacy-focused API for analyzing and processing Google Takeout data",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure data directory exists
data_dir = Path(__file__).parent.parent / "data"
data_dir.mkdir(exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to Google Takeout Explorer API"}


@app.get("/api/v1/data/sources")
async def list_data_sources():
    """List all available data sources from uploaded Google Takeout files"""
    try:
        # Check for zip files in the data directory
        zip_files = list(data_dir.glob("*.zip"))
        
        # Return list of available data sources
        return {
            "sources": [file.stem for file in zip_files],
            "count": len(zip_files)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing data sources: {str(e)}")


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
