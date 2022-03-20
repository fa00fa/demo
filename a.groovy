node('master'){
    stage('println 99table'){
        println('###########################################################################################');
        println('#                                   printing 99table                                      #');
        println('###########################################################################################');
        sh'''
            echo $JENKINS_HOME
            pwd
            cd workspace
            if [ ! -e demo ];then
                git clone https://github.com/fa00fa/demo.git
            fi
            cd demo
            echo $JENKINS_USER
            python 999table.py
        '''

    }
    stage('get sina blog'){
        println('###########################################################################################');
        println('#                                   get sina blog                                      #');
        println('###########################################################################################');
        sh'''
            python sina_spider.py
        '''
    }
    stage('save file'){
        println('###########################################################################################');
        println('#                                   save file                                             #');
        println('###########################################################################################');
        sh'''
            move ./E-commerce.txt ~/demo
        '''
    }
}