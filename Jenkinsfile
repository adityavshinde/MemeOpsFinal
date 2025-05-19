pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "adityavshinde/memeops"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'git@github.com:adityavshinde/MemeOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Login to DockerHub & Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHubCred', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push adityavshinde/memeops
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes cluster...'
                sh 'kubectl apply -f k8s/memeops-deployment.yaml'
                sh 'kubectl apply -f k8s/memeops-service.yaml'
                sh 'kubectl apply -f k8s/memeops-hpa.yaml'
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }

        stage('(Optional) Deploy via Ansible') {
            steps {
                sh '''
                    ansible-playbook ansible-deploy/deploy.yml -i ansible-deploy/hosts
                '''
            }
        }
    }

    post {
        always {
            // Clean up old Docker container if it exists
            sh 'docker rm -f memeops-app || true'
        }
    }
}

