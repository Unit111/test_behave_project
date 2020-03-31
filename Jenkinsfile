pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                sh './venv/bin/behave run_in_parallel'
            }
        }
    }
}