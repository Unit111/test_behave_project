pipeline {
    agent {label "masterNode"}
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
                    def tests = [:]
                    def featuresArray = readFile(file: 'features').split("\n")
                    Arrays.asList(featuresArray).each { feature ->
                        featureName = feature.replace(":1", "").split("/")
                        featureName = featureName[featureName.length - 1]
                        tests[featureName] = {
                            stage(featureName) {
                                    sh "behave -f allure_behave.formatter:AllureFormatter -o reports " + feature
                            }
                        }
                    }
                    parallel tests
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