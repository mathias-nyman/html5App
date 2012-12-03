import pyjd

from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui import HasAlignment
from pyjamas.ui.Image import Image
from pyjamas import Window

from ExampleObject import ExampleObject

class ExampleTable(FlexTable):
    def __init__(self):
        FlexTable.__init__(self)
        self.objs = []


    # @param obj: ExampleObject instance
    def add(self, obj):
        assert isinstance(obj, ExampleObject)
        self.objs.append(obj)

        nameRow = 0
        valueRow = 1
        column = len(self.objs) - 1  # -1, since we just added this tag

        # Add new column to flextable
        self.setText(nameRow, column, obj.name)
        self.setText(valueRow, column, obj.value)

        # Add css style to textRow
        self.getCellFormatter().addStyleName(valueRow, column, 'blackOnRed')
        self.getCellFormatter().addStyleName(nameRow, column, 'blackOnGreen')

        # Adjust allignment
        cellFormatter = self.getFlexCellFormatter()
        cellFormatter.setHorizontalAlignment(valueRow, column, HasAlignment.ALIGN_CENTER)
        cellFormatter.setHorizontalAlignment(nameRow, column, HasAlignment.ALIGN_CENTER)


    def clear(self):
        while self.getRowCount() != 0:
            self.removeRow(0)
        self.objs = []

