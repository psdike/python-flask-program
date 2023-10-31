pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Get some code from a GitHub repository
                sh "git clone https://github.com/psdike/python-flask-program.git"
                sh "cd python-flask-program" 
                sh "ls"
            }
            }

        stage('Build')  {
          steps {
               
                sh "sudo apt update"
                sh "sudo apt install python3-pip -y"
                sh "pwd"
              sh "ls -a"
                sh "sudo pip3 install -r requirements.txt"
                
            }
        }
         stage('Deploy')  {
          steps {
                
                sh "nohup sudo python3 main.py &"
                
            }
        }
    }
    post{
        success{
        sh 'echo check on port 8000'
        }
    }
}
