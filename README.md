# Weather API

An API that gets the minimum, maximum, average and median temperature for a given city and period of time.

## Introduction

An API that gets the minimum, maximum, average and median temperature for a given city and period of time.

## Prerequisites

Before you continue, ensure you have met the following requirements:

- You have installed [Python 3.0 or later](https://www.python.org/)
- You have installed the latest version of [virtualenv](https://pypi.org/project/virtualenv/) Python library.
- You are using a Linux or Mac OS or Windows machine.

## Usage

1. Get the source code onto your dev machine workspace:

   `git clone https://github.com/pmutua/weather-api.git`

2. Navigae to the folder:

   `cd weather-api`

3. Create a virtual environment

   ```# Linux/MacOS:
       python3 -m virtualenv env

       # Windows:
       python -m virtualenv env
   ```

4. Start the virtual environment

   ```# Linux/MacOS
       source env/bin/activate

       # Windows
       .\env\Scripts\activate
   ```

5. Install dependencies

   **Linux:**

   `pip install -r requirements/dev.txt`

   **Windows:**

   `pip install requirements\dev.txt`

6. Set up environment variables
   Create a file called `.env` in the directory where `manage.py` is located.

   The `.env` should have the following variables then add neccessary values:

   ```bash
       DEBUG=True
       SECRET_KEY=<AddSecretKey>
       DATABASE_URL=<AddDataBaseUrl>
       ALLOWED_HOSTS=<AddAllowedHostsHere>
       WEATHER_API_KEY=<AddWeatherAPIKeyHere>
       WEATHER_API_BASE_URL=http://api.weatherapi.com/v1
   ```

   You can get the Weather API key at [Weather API](https://www.weatherapi.com/docs/)

7. Create migrations and apply migrations.

   ```bash
      python manage.py makemigrations
      python manage.py migrate
   ```

8. Start the app locally

   `python manage.py runserver`

## Using the API

The API currently has one endpoint that allows the user to get the minimum, maximum, average and median temperature for a given city and period of time.

### Making a Request

Url format: `/api/locations/<add city name here>/?days=<add number of days here>`

**Example**
`GET /api/locations/london/?days=1`

| Parameter   | Type      | Description             |
| :---------- | :-------- | :---------------------- |
| `city` | `string`  | **Required**. city name |
| `days`      | `integer` | **Required**. days      |

### Response

The endpoint returns a JSON response in the following format:

```javascript
{
    "success": true,
    "msg": "success",
    "data": {
        "maximum": 18.6,
        "minimum": 11.0,
        "average": 13.593055555555555,
        "median": 12.95
    },
    "status": 200
}
```

The `msg` attribute contains a message commonly used to indicate errors or success that the resource was retrieved.

The `success` attribute describes if the request was successful or not.

The `status` attribute describes status code.

The `data` attribute contains JSON data.

## Status Codes

The API returns the following status codes in its API:

| Status Code | Description   |
| :---------- | :------------ |
| 200         | `OK`          |
| 400         | `BAD REQUEST` |
