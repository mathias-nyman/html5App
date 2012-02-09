import pyjd

from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.Timer import Timer
from pyjamas.ui import HasAlignment

import datetime

from ClockCanvas import ClockCanvas
from TextVars import TextVars


class StandByView(HorizontalPanel, ClickHandler):
    def __init__(self, oviValpas):
        HorizontalPanel.__init__(self, BorderWidth=1,
                                       HorizontalAlignment=HasAlignment.ALIGN_LEFT,
                                       VerticalAlignment=HasAlignment.ALIGN_TOP,
                                       Width="100%",
                                       Height="94%")
        ClickHandler.__init__(self)
        
        self.oviValpas = oviValpas
        self.addClickListener(getattr(self, "screenClicked"))

        self.createStandByView()

        self.isActive = True
        self.onTimer()


    def reset(self):
        self.middleLabel.setText(TextVars.allIsFine)


    def screenClicked(self, sender=None):
        self.oviValpas.valpasWatcher.stopSound()


    def createStandByView(self):
        
        # Initialize member variables
        self.middlePanel = VerticalPanel( BorderWidth=0,
                                          HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                                          VerticalAlignment=HasAlignment.ALIGN_MIDDLE,
                                          Width="100%",
                                          Height="100%")
        self.leftPanel = VerticalPanel( BorderWidth=0,
                                        HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                                        VerticalAlignment=HasAlignment.ALIGN_TOP,
                                        Width="100%",
                                        Height="100%")

        self.leftHeaderButton = Button('OviValpas', self.oviValpas.toTagAdminInterface)
        self.middleLabel = Label(TextVars.allIsFine)
        self.weekDayLabel = Label('')
        self.dateLabel = Label('')
        self.timeLabel = Label('')

        # Clock canvas widget
        self.clockCanvas = ClockCanvas('images/chrome_clock_and_numbers.png')

        # Assemble Middle panel
        self.middleLabel.setStyleName('standByViewMainText')
        self.middlePanel.add(self.middleLabel)

        # Assemble Left panel
        self.leftHeaderButton.setStyleName('leftHeaderButton')
        self.leftPanel.add(self.leftHeaderButton)
        self.leftPanel.add(self.clockCanvas)
        self.leftPanel.add(self.weekDayLabel)
        self.leftPanel.add(self.dateLabel)
        self.leftPanel.add(self.timeLabel)
        self.leftPanel.setCellHorizontalAlignment(self.clockCanvas, HasAlignment.ALIGN_CENTER)
        self.leftPanel.setCellVerticalAlignment(self.clockCanvas, HasAlignment.ALIGN_TOP)

        
        # Assemble the Main Holder panel
        self.add(self.leftPanel)
        self.add(self.middlePanel)
        self.setCellWidth(self.leftPanel, "1%")


    def updateTextTime(self):
        now = datetime.datetime.now()
        dayNumber = now.weekday()

        if   dayNumber == 0: weekday = TextVars.Weekday.monday
        elif dayNumber == 1: weekday = TextVars.Weekday.tuesday
        elif dayNumber == 2: weekday = TextVars.Weekday.wednesday
        elif dayNumber == 3: weekday = TextVars.Weekday.thursday
        elif dayNumber == 4: weekday = TextVars.Weekday.friday
        elif dayNumber == 5: weekday = TextVars.Weekday.saturday
        elif dayNumber == 6: weekday = TextVars.Weekday.sunday

        self.weekDayLabel.setText(weekday)
        self.dateLabel.setText("%d.%d.%d" % (now.day, now.month, now.year))

        minute = str(now.minute)
        hour = str(now.hour)
        if now.minute <= 9:
            minute = '0' + minute
        if now.hour <= 9:
            hour = '0' + hour
        self.timeLabel.setText("%s:%s" % (hour, minute))


    def onTimer(self, sender=None):
        if not self.isActive:
            return
        
        Timer(1000, self)
        self.updateTextTime()
        
