class POIController(object):

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab
        self.poi_tab.newPOIButton.clicked.connect(self.poiWindow)

    def poiWindow(self):
        self.poi_tab.setupUiPOI(self.poi_tab.windowPOI)
        self.poi_tab.windowPOI.show()