pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup venv') {
            steps {
                bat '''
                    py -m venv .venv
                    call .venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate
                    pytest --junitxml=reports\\junit.xml --cov=app --cov-report=xml:reports\\coverage.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
        }
    }
}