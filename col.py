from module.listener import Listener
import optparse


parser = optparse.OptionParser()
parser.add_option("-p","--port",dest="port",help="port number to listening requests")
(userIn, arg) = parser.parse_args()


if userIn.port:
    Listener(userIn.port)
else:
    print("Give Any port to listen requests -> -p ")

