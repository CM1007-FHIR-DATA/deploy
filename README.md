# HAPI FHIR Deployment with Synthetic Data

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Starting the Server](#starting-the-server)
  - [Importing Synthetic Data](#importing-synthetic-data)
- [Configuration](#configuration)

## Overview

This repository provides a setup for deploying a HAPI FHIR server along with a database and a file server. The file server can be used to import synthetic FHIR data into the HAPI FHIR server.

```mermaid
flowchart LR
    fs(File Server) <-->|Provides synthetic FHIR data files upon request| hf(HAPI FHIR Server)
    hf(HAPI FHIR Server) <-->|Stores FHIR data| db[(PostgreSQL Database)]
```

## Features

- **HAPI FHIR Server**: A fully functional FHIR server using HAPI FHIR jpa-starter.
- **Database**: Pre-configured database to store FHIR data.
- **File Server**: A file server for managing and importing synthetic FHIR data.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Syntetic data or the ability to run a Java program to generate it
- Python 3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CM1007-FHIR-DATA/deploy.git
   ```

2. Navigate to the project directory:
   ```bash
   cd deploy
   ```
3. Start the services using Docker Compose:
   ```bash
   docker-compose up -d
   ```
4. Import synthetic data:
   ```bash
   python bulk_import.py
   ```

## Usage

### Starting the Server

To start the HAPI FHIR server and file server, use the following command:

```bash
docker-compose up -d
```

The FHIR server will be accessible at `http://localhost:8080/fhir`.

### Importing Synthetic Data

1. Place your synthetic FHIR data files in the `fhir-data` directory.
2. Use the python script to post the fhir-data manifest to the hapi servers bulk import path.
   - If you dont have `requests` installed you can run the script from a virtual environment. This can be done by running `python setup_venv.py`.
   - Run the script with `python bulk_import.py`

## Configuration

Configuration options for the HAPI FHIR server, db and file server are located in the `docker-compose.yml` file.
