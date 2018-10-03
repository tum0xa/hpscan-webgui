# hpscan tools

import os
from threading import Thread

class Scanner(Thread):

    def __init__(self, options):
        Thread.__init__(self)
        self.options = options

    def run(self):
        options_string = ''
        options = self.options
        if options:
            for option, value in options.items():
                options_string+=' --' + option + '=' + value
        else:
            print('Scanning with default options!')
        os.system('hp-scan' + options_string)
        print('Scanning is done!')