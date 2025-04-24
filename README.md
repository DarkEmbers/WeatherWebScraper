# Weather Forecast Web Scraper

This Python script scrapes a 10-day weather forecast from [weather.com](https://weather.com) using `requests` and `BeautifulSoup`. It collects daily temperature highs, weather conditions, and precipitation chances, then prints the results in a readable format.

## Features

- Extracts 10-day forecast data including:
  - Day of the week
  - High temperature
  - Weather conditions
  - Chance of rain
- Uses `BeautifulSoup` for HTML parsing
- Quick and lightweight script suitable for command-line use or as a backend utility

## Getting Started

### Prerequisites

Install the required Python libraries:

```bash
pip install requests beautifulsoup4
```