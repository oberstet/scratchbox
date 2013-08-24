from twisted.application.service import ServiceMaker

__all__ = ['serviceMaker']


serviceMaker = ServiceMaker('foobar',
                            'foobar.main',
                            'Foobar Service',
                            'foobar')
