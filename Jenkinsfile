node {
    stage('Test') {
      if (env.CHANGE_TARGET == 'master') {
        checkout scm
        echo "In Branch ${env.BRANCH_NAME}"
        sh "printenv"
      }
      else {
         echo "In Branch ${env.BRANCH_NAME}"
      }
    }
}
