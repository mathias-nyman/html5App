import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.ui import HasAlignment
from pyjamas import Window
from pyjamas import DOM

from ClockCanvas import ClockCanvas
from ExampleObject import ExampleObject
from ExampleObjectFlexTable import ExampleObjectFlexTable


class DefaultView(HorizontalPanel, ClickHandler):
    def __init__(self, remote):
        HorizontalPanel.__init__(self, BorderWidth=0,
                                       HorizontalAlignment=HasAlignment.ALIGN_LEFT,
                                       VerticalAlignment=HasAlignment.ALIGN_TOP)

        # Catch all clicks to the entire panel
        ClickHandler.__init__(self)
        self.addClickListener(getattr(self, "screenClicked"))

        # A panel to hold the main content
        self.middlePanel = VerticalPanel(BorderWidth=0,
                                         HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                                         VerticalAlignment=HasAlignment.ALIGN_TOP)

        # Some text
        self.heading = Label('An example html5App')
        self.shortExplanation = Label("""
On the right you see a HTML5 Canvas which updates syncronously.
Beneath is an example of communicating between the client and server
using JSON.
""")

        # The text box and button to Add some stuff with JSON
        self.textToAdd = TextBox()
        self.addTextButton = Button('Click me!', self.addText)

        # A flex table for the example objects
        self.exampleObjectFlexTable = ExampleObjectFlexTable()

        # The JSON proxy service
        self.remote = remote

        # Create an Audio element, which can be played ( .play() )
        self.audioElement = DOM.createElement('audio')
        DOM.setAttribute(self.audioElement, 'src', 'sound/sonaralm.wav');

        # An analog clock demonstrating canvas usage
        self.clockCanvas = ClockCanvas('images/chrome_clock_and_numbers.png')

        # Assemble middlePanel
        self.middlePanel.add(self.heading)
        self.middlePanel.add(self.shortExplanation)
        self.middlePanel.add(self.exampleObjectFlexTable)
        self.middlePanel.add(self.textToAdd)
        self.middlePanel.add(self.addTextButton)

        # Assemble self
        self.add(self.clockCanvas)
        self.add(self.middlePanel)
        self.remote.getExampleObjects(self)

        # Listen for keyboard events in the input box
        self_addText = self.addText
        class TextToAdd_KeyboardHandler():
            def onKeyPress(self, sender, keycode, modifiers):
                if keycode == KEY_ENTER:
                    self_addText()
            def onKeyDown(self, sender, keycode, modifiers): return
            def onKeyUp(self, sender, keycode, modifiers): return
        self.textToAdd.addKeyboardListener(TextToAdd_KeyboardHandler())


    def addText(self, sender=None):
        text = self.textToAdd.getText()
        if text is not None:
            self.saveExampleObject(self, text.trim())
 

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
            self.exampleObjectFlexTable.cleanTable()
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

