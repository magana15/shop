pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                dir('messaging/messaging_app'){
                    git credentialsId: 'magana15',
                        url: 'https://github.com/magana15/shop'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('messaging/messaging_app'){
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest pytest-html
                '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('messaging/messaging_app'){
                sh '''
                . venv/bin/activate
                pytest --html=report.html --self-contained-html
                '''
                }
            }

        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
