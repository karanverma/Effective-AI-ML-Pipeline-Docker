# Effective AI/ML Pipeline with Docker

This repository provides a comprehensive guide to building and scaling AI/ML pipelines using Docker. The project includes practical examples and instructions for creating a Dockerized Recommender System API with LocalStack, showcasing the use of various technologies and tools.

## Tech Stack

![Tech Stack](https://github.com/karanverma/Effective-AI-ML-Pipeline-Docker/blob/main/Und-2024-09-14-114851.png)

- **Frontend:** React.js, Material UI
- **Backend:** Node.js, Express
- **Database:** MongoDB
- **Object Storage:** LocalStack (emulating AWS S3)

## Project Structure

This project contains the following components:

- **/backend** - Contains the Node.js application that handles server-side logic and interacts with MongoDB and LocalStack. Includes configuration for S3 uploads.
- **/frontend** - Contains the React.js application for the user interface that communicates with the backend API.

## Development Setup

### Prerequisites

- Docker
- Docker Compose
- AWS CLI
- Node.js and npm
- Python and pip (for awscli-local)

### Installation and Setup

1. **Install awscli-local tool**

    ```bash
    pip install awscli-local
    ```

2. **Clone the Repository**

    ```bash
    git clone https://github.com/karanverma/Effective-AI-ML-Pipeline-Docker.git
    cd Effective-AI-ML-Pipeline-Docker
    ```

3. **Navigate to Project Directory**

    ```bash
    cd Effective-AI-ML-Pipeline-Docker
    ```

### Running the Application

#### Run Locally

1. **Start LocalStack and MongoDB**

    ```bash
    docker compose -f compose-native.yml up -d --build
    ```

2. **Verify LocalStack**

    Access LocalStack at `http://localhost:4566` to confirm it's running.

3. **Add a Sample S3 Bucket**

    ```bash
    awslocal s3 mb s3://mysamplebucket
    ```

4. **Start the Backend**

    Navigate to the backend directory:

    ```bash
    cd backend/
    npm install
    ```

    Start the backend server:

    ```bash
    node index.js
    ```

5. **Start the Frontend**

    Open a new terminal, navigate to the frontend directory, and run:

    ```bash
    cd frontend/
    npm install
    npm run dev
    ```

    Access the frontend at `http://localhost:5173/`.

#### Running with Docker Compose

1. **Start All Services**

    ```bash
    docker compose -f compose.yml up -d --build
    ```

2. **Check Logs**

    Check LocalStack and MongoDB container logs to verify:

    ```bash
    docker logs <localstack-container-id>
    docker logs <mongodb-container-id>
    ```

### Usage

1. **Add a Task and Upload an Image**

   Use the frontend to add tasks and upload images. The images will be stored in the S3 bucket simulated by LocalStack.

2. **Check Application Logs**

   Monitor logs to ensure everything is working as expected.

### Stopping the Services

1. **Stop Services**

    ```bash
    docker compose -f compose-native.yml down
    ```

2. **Remove Containers**

    ```bash
    docker compose -f compose.yml down
    ```

## Contributing

Feel free to open issues, submit pull requests, and contribute to this project. For more information, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Karan Verma](https://github.com/karanverma).

