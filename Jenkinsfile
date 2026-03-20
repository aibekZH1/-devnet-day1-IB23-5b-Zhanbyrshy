pipeline {
    agent any
    stages {
        stage('Check Env') {
            steps {
                echo 'Checking versions...'
                sh 'python3 --version'
                sh 'docker --version'
            }
        }
        stage('Build & Test') {
            steps {
                echo 'Testing Flask App syntax...'
                // Проверяем код на ошибки без запуска сервера
                sh 'python3 -m py_compile app.py'
                echo 'Build successful!'
            }
        }
    }
}
