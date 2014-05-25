# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2007 Lukáš Lalinský
# Copyright (C) 2009 Carlin Mangar
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import os.path
import sys
import json
from PyQt4 import QtCore, QtGui
from picard import config
from picard.const import USER_PLUGIN_DIR
from picard.util import encode_filename, webbrowser2
from picard.ui.options import OptionsPage, register_options_page
from picard.ui.ui_options_plugins_download import Ui_PluginsDownloadPage


def cmp_plugins(a, b):
    return cmp(a.name, b.name)


class PluginsDownloadPage(OptionsPage):

    NAME = "plugins_dl"
    TITLE = N_("Download Plugins")
    PARENT = None
    SORT_ORDER = 70
    ACTIVE = True

    options = [
        config.ListOption("setting", "enabled_plugins", []),
    ]

    def __init__(self, parent=None):
        super(PluginsDownloadPage, self).__init__(parent)
        self.ui = Ui_PluginsDownloadPage()
        self.ui.setupUi(self)
        self.items = {}
        # self.ui.plugins.itemSelectionChanged.connect(self.change_details)
        self.ui.plugins.setSortingEnabled(True)
        self.ui.plugins.mimeTypes = self.mimeTypes
        if sys.platform == "win32":
            self.loader = "file:///%s"
        else:
            self.loader = "file://%s"
        self.ui.install_plugin.clicked.connect(self.install_plugin)
        self.ui.update_plugin.clicked.connect(self.update_plugin)
        self.ui.filter_plugins.clicked.connect(self.filter_plugins)
        # self.tagger.pluginmanager.plugin_installed.connect(self.plugin_installed)

    def load(self):
        import random
        random.seed()

        # This file will be downloaded
        downloaded_json = json.load(open('../picard-plugins/Plugins.json'))

        firstitem = None
        for plugin in downloaded_json['plugins']:
            item = QtGui.QTreeWidgetItem(self.ui.plugins)
            item.setText(0, plugin['title'])
            item.setCheckState(0, QtCore.Qt.Unchecked)
            item.setText(1, str(round(random.random(), 2)))
            item.setText(2, plugin['author'])
            item.setText(3, str(random.randint(305, 813)))
            if not firstitem:
                firstitem = item

        self.ui.plugins.setCurrentItem(firstitem)

        self.ui.plugins.header().resizeSections(QtGui.QHeaderView.ResizeToContents)

    def plugin_installed(self, plugin):
        if not plugin.compatible:
            msgbox = QtGui.QMessageBox(self)
            msgbox.setText(u"The plugin ‘%s’ is not compatible with this version of Picard." % plugin.name)
            msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgbox.setDefaultButton(QtGui.QMessageBox.Ok)
            msgbox.exec_()
            return
        for i, p in self.items.items():
            if plugin.module_name == p.module_name:
                enabled = i.checkState(0) == QtCore.Qt.Checked
                self.add_plugin_item(plugin, enabled=enabled, item=i)
                break
        else:
            self.add_plugin_item(plugin)

    def add_plugin_item(self, plugin, enabled=False, item=None):
        if item is None:
            item = QtGui.QTreeWidgetItem(self.ui.plugins)
        item.setText(0, plugin.name)
        if enabled:
            item.setCheckState(0, QtCore.Qt.Checked)
        else:
            item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setText(1, plugin.version)
        item.setText(2, plugin.author)
        self.ui.plugins.header().resizeSections(QtGui.QHeaderView.ResizeToContents)
        self.items[item] = plugin
        return item

    def save(self):
        enabled_plugins = []
        for item, plugin in self.items.iteritems():
            if item.checkState(0) == QtCore.Qt.Checked:
                enabled_plugins.append(plugin.module_name)
        config.setting["enabled_plugins"] = enabled_plugins

    def change_details(self):
        plugin = self.items[self.ui.plugins.selectedItems()[0]]
        text = []
        name = plugin.name
        descr = plugin.description
        if descr:
            text.append(descr + "<br/>")
            text.append('______________________________')
        if name:
            text.append("<b>" + _("Name") + "</b>: " + name)
        author = plugin.author
        if author:
            text.append("<b>" + _("Author") + "</b>: " + author)
        text.append("<b>" + _("File") + "</b>: " + plugin.file[len(plugin.dir)+1:])
        self.ui.details.setText("<p>%s</p>" % "<br/>\n".join(text))

    def install_plugin(self, path):
        pass

    def filter_plugins(self):
        pass

    def update_plugin(self):
        pass

    def open_plugin_site(self):
        webbrowser2.goto('plugins')

    def mimeTypes(self):
        return ["text/uri-list"]


register_options_page(PluginsDownloadPage)
