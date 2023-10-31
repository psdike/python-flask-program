pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/psdike/python-flask-program.git'

                sh "ls"
            }
            }

        stage('Build')  {
          steps {
               
                sh "sudo apt update"
                sh "sudo apt install python3-pip -y"
                sh "pip3 install -r requirements.txt"
                
            }
        }
         stage('Deploy')  {
          steps {
                
                sh "nohup python3 main.py &"
                
            }
        }
    }
    post{
        success{
        sh 'echo check on port 8000'
        }
    }
}
