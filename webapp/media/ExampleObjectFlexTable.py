import pyjd

from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui import HasAlignment
from pyjamas.ui.Image import Image


class ExampleObjectFlexTable(FlexTable):
    def __init__(self):
        # NOTE: Centering doesnt work in android app with WebView, 
        # but we could "center" the items like this if we wanted to
        #FlexTable.__init__(self, BorderWidth=0, Size=("1%", "100%"))
        FlexTable.__init__(self)
        self.objs = []


    #@param obj: ExampleObject instance
    def addExampleObject(self, obj):
        self.objs.append(obj)

        picRow = 0
        textRow = 1
        column = len(self.objs) - 1  # -1, since we just added this tag

        obj = Image(obj.pic)

        # Add new column to flextable
        self.setWidget(picRow, column, pic)
        self.setText(textRow, column, obj.name)

        # Add css style to textRow
        self.getCellFormatter().addStyleName(textRow, column, 'flexTableItem')
        self.getCellFormatter().addStyleName(textRow, column, 'flexTableItemText')

        # Adjust allignment 
        cellFormatter = self.getFlexCellFormatter()
        cellFormatter.setHorizontalAlignment(picRow, column, HasAlignment.ALIGN_CENTER)
        cellFormatter.setHorizontalAlignment(textRow, column, HasAlignment.ALIGN_CENTER)


    def cleanTable(self):
        while self.getRowCount() != 0:
            self.removeRow(0)
        self.objs = []

