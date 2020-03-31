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
                    python3 ./run_in_parallel.py
                    """
            }
        }
    }
}