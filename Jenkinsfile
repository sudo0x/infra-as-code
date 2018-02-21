node {
    stage('Test') {
      checkout scm
      docker.image('stridesdk:PR-88').inside('-u root') {
        sh "ls /usr/src/app"
      }
    }
}
