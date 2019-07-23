def platformImage
node {
    stage('Checkout Code') {
      checkout scm
    }
    stage('Encrypt Code') {
      sh 'pipenv --python 3.6'
      sh 'pipenv install nuitka'
    }
    stage('Compile Code') {
      sh 'pipenv --python 2.7'
      sh 'pipenv install nuitka'
      sh 'python nuitka_compile.py'
    }
    stage('Build Image') {
      docker.withRegistry('http://strideai.azurecr.io','stride-docker-cr') {
          platformImage = docker.build("strideai.azurecr.io/test-image:${env.TAG_NAME}")
      }
    }
    stage('Push Image to Registry') { 
      docker.withRegistry('http://strideai.azurecr.io','stride-docker-cr') {
        platformImage.push()
      }
  }
}
