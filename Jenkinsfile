def platformImage
node {
    stage('Checkout Code') {
      checkout scm
    }
    stage('Encrypt Code') {
      sh 'tox'
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
