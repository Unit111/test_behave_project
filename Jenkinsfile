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
        stage('Gather features') {
            steps {
                sh "python3 ./gather_features.py"
            }
        }
        stage('Print features') {
            steps {
                script {
                    def featuresString = readFile(file: 'features')
                    def featuresArray = featuresString.split("\n")
                    for( String value : featuresArray )
                        println(value);
                }
            }
        }
        stage('Run tests') {
            failFast true
            parallel {
                stage('Branch A') {
                    steps {
                        sh "behave -f allure_behave.formatter:AllureFormatter -o reports tests/features/first.feature:1"
                    }
                }
                stage('Branch B') {
                    steps {
                        sh "behave -f allure_behave.formatter:AllureFormatter -o reports tests/features/fourth.feature:1"
                    }
                }
                stage('Branch C') {
                    steps {
                        sh "behave -f allure_behave.formatter:AllureFormatter -o reports tests/features/second.feature:1"
                    }
                }
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