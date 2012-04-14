from twisted.application.service import ServiceMaker

serviceMaker = ServiceMaker('sslecho',
                            'sslecho',
                            'sslecho Twistd Plugin',
                            'sslecho')
