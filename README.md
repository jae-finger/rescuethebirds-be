# rescuethebirds backend

<img src="https://img.shields.io/badge/under%20construction-FF8C00" /> <img src="https://img.shields.io/badge/beta-blue"/>

## Project Overview

Welcome to our FastAPI backend! This repository contains the code for our backend server built using FastAPI, a modern, fast, web framework for building APIs with Python. This backend serves as the foundation for our application, allowing us to handle data processing and interactions.

## Features

- **FastAPI Framework**: Our backend is built using FastAPI, which provides a powerful and intuitive way to create APIs in Python.
- **Endpoint Documentation**: FastAPI automatically generates interactive API documentation. You can access it at `/docs` after running the server.
- **Annotations and Comments**: The code is well-annotated with comments to aid in understanding and maintenance.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.9+
- Pipenv (recommended for managing dependencies)

## Installation

1. Clone this repository: `git clone https://github.com/jae-finger/rescuethebirds`
2. Navigate to the project directory: `cd rescuethebirds`
3. Install dependencies: `pip install -r requirements.txt`

## Configuration

1. Create `.env`.
2. Configure database settings, API keys, and other environment-specific variables.

## Running the Server

Run the following command to start the FastAPI development server:
1. `docker build -t rescuethebirds .`
2. `docker run -d -p 8000:8000 rescuethebirds`

## Basic Backend Flow
The Rescue the Birds! backend is built around assisting our stakeholder, Rich, at the refuge. He wishes to have a website that dumps everything into a google sheet - like the one he has now. So, here's a simplified view of how a user interacts with the frontend, and how it ends up in front of the refuge.
```mermaid

graph LR;
    style randomuser fill:#ffffff, stroke:#000000;
    randomuser([Bird Lover])-->fe[Website];
    subgraph frontend [React Frontend]
    style fe fill:#FFD580, stroke:#000000;
    
    style 1 fill:#CBC3E3, stroke:#000000;
    fe-->7[[Boarding Form]];

    style 2 fill:#CBC3E3, stroke:#000000;
    fe-->6[[Volunteer Form]];

    style 3 fill:#CBC3E3, stroke:#000000;
    fe-->5[[Adoption Form]];
    end
    style fe fill:#FFD580, stroke:#000000;
    fe-.->8[[Donation Form]];
    subgraph comingsoon [Coming Soon]
    8-.->4[[Donation Info]];

    end
    style comingsoon fill:#cccccc, stroke:#000000;
    subgraph backend [Fast API Backend]
    
    
    5-->1[[Adoption Info]];

    style 5 fill:#FFD580, stroke:#000000;
    6-->2[[Volunteer Info]];

    style 6 fill:#FFD580, stroke:#000000;
    7-->3[[Boarding Info]];
    4-.-be;
    style 7 fill:#FFD580, stroke:#000000;

    style 4 fill:#cccccc, stroke:#000000;

    style 8 fill:#cccccc, stroke:#000000;
    
    1-->be;
    style be fill:#CBC3E3, stroke:#000000;
    
    2-->be;
    3-->be;

    be[Docker on GCP]-->googlesheet[(Google Sheet)]
    end
    style be fill:#CBC3E3, stroke:#000000;
    style googlesheet fill:#CBC3E3, stroke:#000000;
    style frontend fill:#FFD580, stroke:#000000;
    style backend fill:#CBC3E3, stroke:#000000;

    googlesheet---stakeholder(["`Rich (*stakeholder*)`"]);


    style stakeholder fill:#ffffff, stroke:#000000;

```
