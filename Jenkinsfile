
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = 'ateebakmal/linear-regression-api-lab-6:v1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set +x
                        printf '%s' "$DOCKERHUB_TOKEN" |
                            docker login \
                                --username "$DOCKERHUB_USERNAME" \
                                --password-stdin

                        docker push "$IMAGE_NAME"
                        docker logout
                    '''
                }
            }
        }


        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                    whoami
                    which docker
                    docker --version
                    docker compose version
                    docker compose down || true
                    docker compose pull
                    docker compose up -d --remove-orphans
                    docker compose ps
                '''
            }
        }

    }
}
