import pyjd

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.JSONService import JSONProxy
from pyjamas import Window

from DefaultView import DefaultView

class ExampleApp:
    def onModuleLoad(self):
        '''
        This is the main entry point method.
        '''

        # Setup JSON RPC
        self.remote = DataService()

        self.defaultView = DefaultView(self.remote)
        RootPanel().add(self.defaultView)

        # TODO: could demonstrate removing and adding smth else also
        #RootPanel().remove(self.exampleView)


# Set up the JSONProxy service and specify the function calls
class DataService(JSONProxy):
    methods = ['getExampleObjects', 
               'saveExampleObject', 
               'removeExampleObject',
               'getAllPics']
    
    def __init__(self):
        JSONProxy.__init__(self, 'services/', DataService.methods)


# Default Pyjamas stuff
if __name__ == '__main__':
    pyjd.setup('./ExampleApp.html')
    app = ExampleApp()
    app.onModuleLoad()
    pyjd.run()

