pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "adityavshinde/memeops"
        DOCKER_CREDENTIALS_ID = "dockerhub-creds"
        KUBE_CONFIG = credentials('kubeconfig')
        ANSIBLE_VAULT_PASSWORD = credentials('ansible-vault-pass')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/adityavshinde/MemeOpsFinal.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker run --rm $DOCKER_IMAGE pytest tests/'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory.yml deploy.yml --vault-password-file vault_pass.txt'
                }
            }
        }

        stage('Monitoring and Logging') {
            steps {
                script {
                    sh 'kubectl logs -l app=memeops | tee memeops.log'
                    sh 'echo "$(date): Logs fetched" >> elk.log'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
