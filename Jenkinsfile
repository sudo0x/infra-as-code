node {
    stage('Checkout Code') {
      checkout scm
    }
    stage('Build Image') {
      docker.withRegistry('strideai.azurecr.io','stride-docker-cr') {
          def platformImage = docker.build("strideai.azurecr.io/test-image:${env.TAG_NAME}")
      }
    }
    stage('Push Image to Registry') { 
        platformImage.push()
    }
}
