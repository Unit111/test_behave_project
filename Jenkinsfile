pipeline {
    agent any
    stages {
        stage('Install requirements') {
            steps {
                sh  """
                    pip3 install -r requirements.txt
                    """
            }
        }
        stage('Run tests') {
            steps {
                sh  """
                    behave -f allure_behave.formatter:AllureFormatter -o reports tests/features/first.feature:1
                    """
            }
        }
        stage('Reports') {
            steps {
                script {
                        allure([
                                includeProperties: false,
                                jdk: '',
                                properties: [],
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: 'reports']]
                        ])
                }
            }
        }
    }
}