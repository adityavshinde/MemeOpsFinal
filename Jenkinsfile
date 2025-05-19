pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
<<<<<<< HEAD
                // Clone the dev branch from the repository
=======
                // Corrected the git syntax
>>>>>>> 9b6fb07 (Integrate CI/CD with Jenkins)
                git branch: 'dev', url: 'https://github.com/adityavshinde/MemeOps.git'
            }
        }
        stage('Install Dependencies') {
            steps {
<<<<<<< HEAD
                // Navigate to the project directory and install dependencies
                sh '''
                cd ${WORKSPACE}
                echo "Working directory: $(pwd)"
                which python || echo "Python not found!"
                which pip || echo "Pip not found!"
                
                # Check if requirements.txt exists and install packages
                if [ -f requirements.txt ]; then
                    pip install --user -r requirements.txt
                else
                    echo "requirements.txt not found!"
                    exit 1
                fi
=======
                // Ensure that Python and pip are available
                sh '''
                which python || echo "Python not found!"
                which pip || echo "Pip not found!"
                pip install -r requirements.txt
>>>>>>> 9b6fb07 (Integrate CI/CD with Jenkins)
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh '''
<<<<<<< HEAD
                cd ${WORKSPACE}
                if [ -f requirements.txt ]; then
                    pip install --user -r requirements.txt
                fi
                pytest || echo "No tests found!"
=======
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                pytest
>>>>>>> 9b6fb07 (Integrate CI/CD with Jenkins)
                '''
            }
        }
        stage('Build') {
            steps {
                // Run the application
                sh '''
<<<<<<< HEAD
                cd ${WORKSPACE}
=======
>>>>>>> 9b6fb07 (Integrate CI/CD with Jenkins)
                if [ -f app.py ]; then
                    python app.py
                else
                    echo "app.py not found!"
                    exit 1
                fi
                '''
            }
        }
    }
    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed!'
        }
    }
}
