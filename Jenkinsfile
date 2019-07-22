def platformImage
node {
    stage('Checkout Code') {
      checkout scm
      sh 'ls'
      sh 'git clone git@github.com:premsompura/premsompura.github.io.git'
      sh 'ls'
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
