node {
    stage('Test') {
      checkout scm
      echo "In Branch ${env.BRANCH_NAME}"
      sh "git fetch"
      sh "git checkout origin/${env.CHANGE_TARGET}"
      sh "git merge -m "test merge" origin/${env.BRANCH_NAME}"        
    }
}
