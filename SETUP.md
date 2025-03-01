
# Setup Instructions

## Prerequisites
- Docker installed on your machine.
- The `deepseek-r1:latest` model installed locally.

## Steps
1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/Project_AI.git
    cd Project_AI
    ```

2. **Build the Docker Image**
    ```sh
    docker build -t project_ai .
    ```

3. **Run the Docker Container**
    ```sh
    docker run -d --name project_ai_container -p 5000:5000 project_ai
    ```

4. **Access the Application**
    Open your browser and navigate to `http://localhost:5000` to start using the AI assistant.
