# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\options_plugins_download.ui'
#
# Created: Sun Mar 02 09:44:52 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PluginsDownloadPage(object):
    def setupUi(self, PluginsDownloadPage):
        PluginsDownloadPage.setObjectName(_fromUtf8("PluginsDownloadPage"))
        PluginsDownloadPage.resize(609, 474)
        self.vboxlayout = QtGui.QVBoxLayout(PluginsDownloadPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.splitter = QtGui.QSplitter(PluginsDownloadPage)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plugins = QtGui.QTreeWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plugins.sizePolicy().hasHeightForWidth())
        self.plugins.setSizePolicy(sizePolicy)
        self.plugins.setAcceptDrops(True)
        self.plugins.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.plugins.setRootIsDecorated(False)
        self.plugins.setObjectName(_fromUtf8("plugins"))
        self.verticalLayout_2.addWidget(self.plugins)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filter_label = QtGui.QLabel(self.groupBox_2)
        self.filter_label.setObjectName(_fromUtf8("filter_label"))
        self.horizontalLayout.addWidget(self.filter_label)
        self.filter_pattern = QtGui.QLineEdit(self.groupBox_2)
        self.filter_pattern.setText(_fromUtf8(""))
        self.filter_pattern.setObjectName(_fromUtf8("filter_pattern"))
        self.horizontalLayout.addWidget(self.filter_pattern)
        self.filter_plugins = QtGui.QPushButton(self.groupBox_2)
        self.filter_plugins.setObjectName(_fromUtf8("filter_plugins"))
        self.horizontalLayout.addWidget(self.filter_plugins)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.install_plugin = QtGui.QPushButton(self.groupBox_2)
        self.install_plugin.setEnabled(True)
        self.install_plugin.setObjectName(_fromUtf8("install_plugin"))
        self.horizontalLayout_3.addWidget(self.install_plugin)
        self.update_plugin = QtGui.QPushButton(self.groupBox_2)
        self.update_plugin.setObjectName(_fromUtf8("update_plugin"))
        self.horizontalLayout_3.addWidget(self.update_plugin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtGui.QFrame.HLine)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 571, 86))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.details = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy)
        self.details.setMinimumSize(QtCore.QSize(0, 0))
        self.details.setFrameShape(QtGui.QFrame.Box)
        self.details.setLineWidth(0)
        self.details.setText(_fromUtf8(""))
        self.details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.details.setWordWrap(True)
        self.details.setIndent(0)
        self.details.setOpenExternalLinks(True)
        self.details.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.details.setObjectName(_fromUtf8("details"))
        self.verticalLayout.addWidget(self.details)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.vboxlayout1.addWidget(self.scrollArea)
        self.vboxlayout.addWidget(self.splitter)

        self.retranslateUi(PluginsDownloadPage)
        QtCore.QMetaObject.connectSlotsByName(PluginsDownloadPage)

    def retranslateUi(self, PluginsDownloadPage):
        self.groupBox_2.setTitle(_("Plugins"))
        self.plugins.headerItem().setText(0, _("Name"))
        self.plugins.headerItem().setText(1, _("Version"))
        self.plugins.headerItem().setText(2, _("Author"))
        self.plugins.headerItem().setText(3, _("Downloads"))
        self.filter_label.setText(_("Filter Plugins:"))
        self.filter_plugins.setText(_("Filter"))
        self.install_plugin.setText(_("Install"))
        self.update_plugin.setText(_("Update"))
        self.groupBox.setTitle(_("Details"))

