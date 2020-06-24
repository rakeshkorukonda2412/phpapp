pipeline {
    agent {
        docker { image 'node:7-alpine' }
    }
    stages {
        stage('Build'){
          steps{
            echo 'building application'
          }
        }
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
        stage('Deploy'){
          steps{
            echo 'Deploy application'
          }
        }
    }
}
