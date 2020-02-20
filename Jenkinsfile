pipeline {
    environment {
        appName = "server"
        registry = "phoexer/bce"
        projectPath = "/jenkins/data/workspace/bce-server"
    }

    agent any


    stages {
        stage('Basic Information') {
            steps {
                sh "echo 'Basic data'"
                sh "pwd"
                sh "ls"
                sh "echo $appName"
                sh "docker-compose -v"
            }
        }
        stage('Build Server Container') {
            steps {
                sh "docker-compose up --build"
            }
        }
        stage('Run Tests') {
            steps {
                sh "docker-compose exec bce-server pytest"
            }
        }
        stage('Garbage Collection') {
            steps {
                sh "docker-compose down"
                sh "docker rm \$(docker ps -a -q)"
                // sh "docker rmi -f \$(docker images -q)"
            }
        }
    }
}
