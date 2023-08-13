## Farmers Market Finder
The app hosts the ability to pull in data from the USDA via a Google Sheets CSV file and return the farmers markets in the specified area.

## Setup
No local set up required, web hosted via onrender.com.

```sh
conda create -n farmers python=3.10

conda activate farmers
```

```sh
pip install -r requirements.txt
```

## Usage

Running the web app on Mac OS:

```sh
FLASK_APP=web_app flask run
```

## Testing
Tests can be run via pytest to verify that the returned data accepts both upper and lower case strings of state id info.

```sh
pytest
```

## Deployment Guide

See [Deployment Guide](/DEPLOYING.md)
