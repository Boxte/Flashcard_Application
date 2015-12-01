#hello
import sys
from PyQt5.QtGui import *
 
# We instantiate a QApplication passing the arguments of the script to it:
a = Qt.QApplication(sys.argv)
 
# Add a basic widget to this application:
# The first argument is the text we want this QWidget to show, the second
# one is the parent widget. Since Our "hello" is the only thing we use (the 
# so-called "MainWidget", it does not have a parent.
hello = Qt.QLabel("Hello, World")
 
# ... and that it should be shown.
hello.show()
 
# Now we can start it.
a.exec_()