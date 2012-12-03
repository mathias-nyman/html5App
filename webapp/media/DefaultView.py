import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui import HasAlignment
from pyjamas import Window
from pyjamas import DOM

from ClockCanvas import ClockCanvas
from ExampleObject import ExampleObject
from ExampleTable import ExampleTable


class DefaultView(HorizontalPanel):
    def __init__(self, remote):
        HorizontalPanel.__init__(self, BorderWidth=0,
                                       HorizontalAlignment=HasAlignment.ALIGN_LEFT,
                                       VerticalAlignment=HasAlignment.ALIGN_TOP)

        # A panel to hold the main content
        self.middlePanel = VerticalPanel(BorderWidth=0,
                                         HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                                         VerticalAlignment=HasAlignment.ALIGN_TOP)

        # Some text
        self.heading = Label('An example html5App')
        self.shortExplanation = Label("""
On the right you see a HTML5 Canvas which updates syncronously.
Beneath is an example of communicating between the client and server
using JSON RPC.
""")

        # The text box and button to Add some stuff with JSON
        self.getObjectsButton = Button('Get Example objects!', self.getObjects)

        # A flex table for the example objects
        self.exampleTable = ExampleTable()

        # The JSON proxy service
        self.remote = remote

        # An analog clock demonstrating canvas usage
        self.clockCanvas = ClockCanvas('images/chrome_clock_and_numbers.png')

        # Assemble middlePanel
        self.middlePanel.add(self.heading)
        self.middlePanel.add(self.shortExplanation)
        self.middlePanel.add(self.getObjectsButton)
        self.middlePanel.add(self.exampleTable)

        # Assemble self
        self.add(self.clockCanvas)
        self.add(self.middlePanel)


    def getObjects(self, sender=None):
        self.remote.getExampleObjects(self)


    def onRemoteError(self, code, message, request_info):
        Window.alert('DefaultView: JSONRPC error.')


    # Will be called when we get a successfull response from the remote for the JSON query
    def onRemoteResponse(self, response, request_info):

        method = request_info.method
        if method == 'getExampleObjects':
            self.exampleTable.clear()
            for obj in response:
                self.exampleTable.add(ExampleObject(obj, response[obj]))
        else:
            Window.alert('DefaultView: Unrecognized JSONRPC method. method= %s' % method)

