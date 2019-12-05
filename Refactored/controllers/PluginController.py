class PluginController(object):

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab
        self.plugin_tab.newPluginButton.clicked.connect(self.pluginWindow)

    def pluginWindow(self):
        self.plugin_tab.setupUiCreatePlugin(self.plugin_tab.windowPlug)
        self.plugin_tab.windowPlug.show()
