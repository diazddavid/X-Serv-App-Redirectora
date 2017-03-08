#!/usr/bin/python3

import webapp

class redirect(webapp.webApp):
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        import random

        nextDirection = str(random.randrange(100000000000))
        return("303 See Other", "<html><head><meta http-equiv="'refresh'
                                " content="'1'";url=" + nextDirection + "'></head></html>")

if __name__ == "__main__":
    testRedirect = redirect("localhost", 1234)
