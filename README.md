# JobSage

JobSage is an AI-powered web application designed to assist users in their job hunt. Leveraging the OpenAI API, JobSage provides resume optimization suggestions, and resume preparation tips to help users land their dream jobs.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

JobSage aims to streamline the job search process by providing tailored assistance through AI-driven insights. Whether you're looking for job openings, need help with your resume, or want to prepare for interviews, JobSage is here to help.

## Technologies Used

- **Frontend**: React
- **Backend**: Go
- **AI**: Python with OpenAI API

## Features

- Personalized job recommendations based on user profiles.
- Resume optimization suggestions to enhance user applications.
- Interview preparation tips and common questions.
- User-friendly interface for an intuitive experience.

## Installation

To set up JobSage locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:AkshathKamath/JobSage.git
   ```
2. ```bash
   cd react-frontend/
   ```
3. ```bash
   npm install
   ```
4. ```bash
   cd ../
   ```
5. ```bash
   cd go-backend/
   ```
6. ```bash
    go mod tidy
   ```
7. ```bash
   cd ../
   ```
8. ```bash
   cd python-gpt-api/
   ```
9. ```bash
   python -m venv venv
   ```
10. ```bash
    source venv/bin/activate
    ```
11. ```bash
    pip install -r requirements.txt
    ```

## Usage

1. ```bash
   cd python-gpt-api/
   python3 app.py
   ```
2. ```bash
   cd go-backend/
   go run ./cmd/api
   ```
3. ```bash
   cd react-frontend/
   npm start
   ```

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or feedback, feel free to reach out:

Your Name - akshathkamathwork@gmail.com
Project Link: https://github.com/AkshathKamath/JobSage
Feel free to reach out if you have any questions or suggestions!
