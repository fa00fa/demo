node('Built-In Node'){
    stage('println 99table'){
        println('###########################################################################################');
        println('#                                   printing 99table                                      #');
        println('###########################################################################################');
        sh'''
            cd $jenkins_home
            git clone https://github.com/fa00fa/demo.git
            cd demo
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
}