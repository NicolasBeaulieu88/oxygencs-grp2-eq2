# LOG-680 : Template for Oxygen-CS

This Python application continuously monitors a sensor hub and manages HVAC (Heating, Ventilation, and Air Conditioning) system actions based on received sensor data.

It leverages `signalrcore` to maintain a real-time connection to the sensor hub and utilizes `requests` to send GET requests to a remote HVAC control endpoint.

This application uses `pipenv`, a tool that aims to bring the best of all packaging worlds to the Python world.

## Requierements

- Python 3.8+
- pipenv

## Getting Started

1. Clone the repository :

```
git clone https://github.com/MarioGith/log680.git
cd log680
```

2. Install the project's dependencies :

```
pipenv install
```

## Setup

To run the app on your machine, you need to setup the following variables in your environment:

- HOST: The host of the sensor hub and HVAC system.
- TOKEN: The token for authenticating requests.
- T_MAX: The maximum allowed temperature.
- T_MIN: The minimum allowed temperature.
- DATABASE_URL: The database connection URL.
- DATABASE_NAME: The name of the database that will be used
- DATABASE_USER: The user that will connect to the database
- DATABASE_PASSWORD: the password for the provided user of the database

## Running the Program

After setup, you can start the program with the following command:

```
pipenv run start
```

## Docker

You can use the provided dockerfile to create a runnable image of this application.

## Logging

The application logs important events such as connection open/close and error events to help in troubleshooting.

## Testing

this application uses unitest with the unittest python library. you can run these tests with the following command:
```
python -m unittest discover
```

## License

MIT

## Contact

For more information, please feel free to contact the repository owner.
