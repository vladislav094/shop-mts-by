pipeline {
  agent any
  stages {
    stage("Clone repository") {
        steps {
        checkout scm
    }
    }

     stage('Build image') {
         steps {
         sh "docker build -t web_test ."
     }
     }

    stage('Execute script') {
        steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            sh "docker run -e RUN_HEADLESS=True --network='host' --name example1 --volume ${WORKSPACE}/allure-results/:/code/allure-results/ --volume selenium-server-allure-reports:/code/allure-reports/ web_test pytest -n3"



    }
    }
    }


     stage('Copy directory from container into workspace') {
         steps {
         sh 'docker cp example1:/code/allure-results/ ${WORKSPACE}/'
     }
     }

    stage('Remove container') {
        steps {
        sh 'docker rm -f example1'
    }
    }

     stage('Remove image') {
         steps {
         sh 'docker rmi web_test -f'
     }
     }


    stage('Allure Report') {
        steps {
            script {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
    }

}
}
}
        }
      }

    }
  }
