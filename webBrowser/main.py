import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.CreateApp()
        self.setBaseSize(1366, 768)

    def CreateApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        #Cria Tab
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab)
        self.tabbar.tabBarClicked.connect(self.SwitchTab)
        self.tabbar.setCurrentIndex(0)

        #Keep track of tabs
        self.tabCount = 0
        self.tabs = []

        #Cria Barra de Endereco
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()
        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)

        # Botao New Tab
        self.addTabButton = QPushButton("+")
        self.addressbar.returnPressed.connect(self.BrowseTo)
        self.addTabButton.clicked.connect(self.addTab)

        self.ToolbarLayout.addWidget(self.addTabButton)

        # Definindo Main View
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)
        self.addTab()
        self.show()

    def CloseTab(self, i):
        self.tabar.removeTab(i)

    def addTab(self):
        i = self.tabCount
        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab" + str(i))

        # Abre o webview
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("https://www.google.com/"))

        # Adiciona o webiew para o layout do tab
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        # Define o top level do tab do [] para o layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        # Adiciona o tab no topo stackedwidget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # Definir o tab em cima da screen
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i, "tab" + str(i))
        self.tabbar.setCurrentIndex(i)

        self.tabCount += 1

    def SwitchTab(self, i):
        tab_data = self.tabbar.tabData(i)
        print("Tab: ", tab_data)
        tab_content = self.findChild(QWidget, tab_data)
        self.container.layout.setCurrentWidget(tab_content)

    def BrowseTo(self):
        text = self.addressbar.text()
        print(text)
        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)
        wv = self.findChild(QWidget, tab).content

        if "http" not in text:
            if "." not in text:
                url = "https://www.google.com/#q=" + text
            else:
                url = "http://" + text
        else:
            url = text
        wv.load(QUrl.fromUserInput(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
