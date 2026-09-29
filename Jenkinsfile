pipeline {
    agent any
    
    stages {
        stage('Build and Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                python3 -m pytest
                '''
            }
        }
        stage('Deploy to Server') {
            steps {
                sh '''
                docker build -t bus-app .
                docker stop bus-schedule || true
                docker rm bus-schedule || true
                docker run -d -p 5000:5000 --name bus-schedule bus-app
                '''
            }
        }
    }
}