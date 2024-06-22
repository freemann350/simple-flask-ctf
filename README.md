# Simple Flask CTF environment

This repository contains a simple Capture The Flag (CTF) environment using Flask and Docker. The environment provides multiple scenarios for hiding a flag in different ways.

Created as a test bed for one of my repositories, [K8SecLabs](https://https://github.com/freemann350/K8SecLabs).

## Available Scenarios

1. **HTML Comment**: The flag is hidden in an HTML comment.
	-  SCENARIO: 1
2. **JavaScript Console**: The flag is hidden in a JavaScript console log.
	-  SCENARIO: 2
3. **CSS Comment**: The flag is hidden in a CSS comment.
	-  SCENARIO: 3
4. **Hidden Endpoint**: The flag is accessible via a hidden endpoint.
	-  SCENARIO: 4
5. **Encoded Flag**: The flag is Base64 encoded and displayed.
	-  SCENARIO: 5

## Environment Variables

- `FLAG`: The flag to be captured by participants. Default: `CTF35f3224b5a78932f1c0161a932dd310137d38107e4c4da0d26948bd041ff3a92
- `SCENARIO`: The scenario to be used. Default: `1`

## Usage

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository: 
```
git clone <repository_url> cd <repository_directory>
```
2. Build the Docker image:
```sh
docker-compose build
```
4. Run the Docker container:
```sh
docker-compose up
```

### Access the CTF Challenge

Once the container is running, access the web application via `http://localhost:5000/`. The scenario will depend on the value of the `SCENARIO` environment variable.