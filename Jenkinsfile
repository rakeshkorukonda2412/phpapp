pipeline {
    agent {
        docker { image 'node:7-alpine' }
    }
    stages {
        stage('Build'){
          steps{
            docker.withRegistry('http://34.69.111.201:8082', 'jfrog-admin-cred') {
              echo 'building application'
              def customImage = docker.build("34.69.111.201:8082/cloudapprepo/myapache:${env.BUILD_ID}")
              customImage.push()
            }
          }
        }
        stage('pull'){
          steps{
            docker.withRegistry('http://34.69.111.201:8082', 'jfrog-admin-cred') {
              docker.image("34.69.111.201:8082/cloudapprepo/myapache:${env.BUILD_ID}").pull()
            }
          }
        }
        stage('Deploy'){
          steps{
            echo 'Deploy application'
            sh """docker container run -dit --name=test-app${env.BUILD_ID} -p 88${env.BUILD_ID}:80 34.69.111.201:8082/cloudapprepo/myapache:${env.BUILD_ID}"""
          }
        }
        stage('Test') {
            steps {
                echo 'testing application'
                sh """curl http://localhost:88${env.BUILD_ID}"""
            }
        }
    }
}
