pipeline {
    agent any

    environment {
        VENV = ".venv"
        PYLAUNCHER = "C:\\Users\\kamil.raczkowski\\AppData\\Local\\Programs\\Python\\Launcher\\py.exe"
        PYVER = "3"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Diagnostics') {
            steps {
                bat '''
                    echo PYLAUNCHER=%PYLAUNCHER%
                    "%PYLAUNCHER%" --version
                    "%PYLAUNCHER%" -%PYVER% -c "import sys; print(sys.version); print(sys.executable)"
                '''
            }
        }

        stage('Setup venv') {
            steps {
                bat '''
                    "%PYLAUNCHER%" -%PYVER% -m venv %VENV%
                    %VENV%\\Scripts\\python.exe -m pip install --upgrade pip
                    %VENV%\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                    %VENV%\\Scripts\\pytest.exe --junitxml=reports\\junit.xml --cov=app --cov-report=xml:reports\\coverage.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
        }
    }
}