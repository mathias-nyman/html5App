import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.ui import HasAlignment
from pyjamas import Window
from pyjamas import DOM

from ClockCanvas import ClockCanvas
from ExampleObject import ExampleObject
from ExampleObjectFlexTable import ExampleObjectFlexTable


class DefaultView(HorizontalPanel, ClickHandler):
    def __init__(self, remote):
        HorizontalPanel.__init__(self, BorderWidth=1,
                                       HorizontalAlignment=HasAlignment.ALIGN_LEFT,
                                       VerticalAlignment=HasAlignment.ALIGN_MIDDLE,
                                       Width="100%",
                                       Height="100%")

        # Catch all clicks to the entire panel
        ClickHandler.__init__(self)
        self.addClickListener(getattr(self, "screenClicked"))

        # A flex table for the example objects
        self.exampleObjectFlexTable = ExampleObjectFlexTable()

        # The JSON proxy service
        self.remote = remote

        # Create an Audio element, which can be played ( .play() )
        self.audioElement = DOM.createElement('audio')
        DOM.setAttribute(self.audioElement, 'src', 'sound/sonaralm.wav');

        # An analog clock demonstrating canvas usage
        self.clockCanvas = ClockCanvas('images/chrome_clock_and_numbers.png')

        # Assemble self
        self.add(self.clockCanvas)
        self.add(self.exampleObjectFlexTable)


    def playSound(self):
        self.audioElement.play()


    def stopSound(self):
        self.audioElement.pause()
        self.audioElement.currentTime=0


    def screenClicked(self, sender=None):
        self.stopSound()


    def onRemoteError(self, code, message, request_info):
        Window.alert('DefaultView: Unrecognized JSONRPC method.')


    # Will be called when we get a successfull response from the remote for the JSON query
    def onRemoteResponse(self, response, request_info):

        method = request_info.method
        if method == 'getExampleObjects':
            self.exampleObjectFlex.cleanTable()
            for obj in response:
                self.exampleObjectFlexTable.addExampleObject(ExampleObject(obj, response[obj]))
        elif method == 'saveExampleObject':
            pass
        elif method == 'removeExampleObject':
            if not response:
                Window.alert('DefaultView: removeExampleObject returned False.')
            pass
        elif method == 'getAllPics':
            pass
        else:
            Window.alert('DefaultView: Unrecognized JSONRPC method.')

