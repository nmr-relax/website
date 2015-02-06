#! /usr/bin/env python

"""Script for changing the headers of the epydoc documentation.

This will recursively walk through the directory supplied as an argument, find all *.html files, read the contents in the <head> tag, preserve the <title> tag, and replace the rest of the header with a custom header.
"""

# Python module imports.
from os import getcwd, sep, system, walk
from re import search
import sys


# Blacklisted files to not change.
BLACKLIST = [
    'frames.html',
    'index.html',
    'redirect.html'
]

# The contents for the HEAD tag, excluding the title tag.
HEAD_CONTENTS = [
    "",
    "  <!--Epydoc setup-->",
    "  <link rel=\"stylesheet\" href=\"epydoc.css\" type=\"text/css\" />",
    "  <script type=\"text/javascript\" src=\"epydoc.js\"></script>",
    "",
    "  <!--Mobile device support-->",
    "  <meta name=viewport content=\"width=device-width, initial-scale=1\">",
    "",
    "  <!--Google analytics JS-->",
    "  <script type=\"text/javascript\">",
    "",
    "    var _gaq = _gaq || [];",
    "    _gaq.push(['_setAccount', 'UA-30096326-1']);",
    "    _gaq.push(['_setDomainName', 'nmr-relax.com']);",
    "    _gaq.push(['_trackPageview']);",
    "",
    "    (function() {",
    "      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;",
    "      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';",
    "      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);",
    "    })();",
    "",
    "  </script>",
]

# The expected head tag contents.
EXPECTED = [
    "<head>",
    None,
    "  <link rel=\"stylesheet\" href=\"epydoc.css\" type=\"text/css\" />",
    "  <script type=\"text/javascript\" src=\"epydoc.js\"></script>",
    "</head>",
]


class Rehead:
    def __init__(self):
        """Change all HTML headers."""

        # Walk through the current dir.
        for root, dirs, files in walk(sys.argv[1]):
            # Loop over the files.
            for file in files:
                # Only work with HTML files.
                if not search(".html$", file):
                    continue
        
                # Skip blacklisted files.
                if file in BLACKLIST:
                    continue

                # Full path to the file.
                full_path = root + sep + file

                # Extract the title.
                title = self.extract_title(full_path)

                # Process the head tag.
                self.change_head(full_path, title=title)


    def change_head(self, file_name, title=None):
        """Read the HTML file to extract the head tag, then recreate the file."""

        # Open the file for writing.
        file = open(file_name, 'w')

        # Walk over the file contents, replacing the header.
        index = 0
        while 1:
            # No more lines.
            if index >= len(self.file_lines):
                break

            # In the head tag.
            if search("<head>", self.file_lines[index]):
                # Write out the head tag and add the title.
                file.write("<head>\n")
                file.write(title)
                file.write("\n")

                # Add the rest of the head contents.
                for line in HEAD_CONTENTS:
                    file.write("%s\n" % line)

                # Go to the end of the head tag.
                while not search("</head>", self.file_lines[index]):
                    index += 1

            # Write out the line.
            file.write(self.file_lines[index])

            # Increment the line number.
            index += 1


    def extract_title(self, file_name):
        """Read the HTML file to extract and return the title tag."""

        # Read the file contents.
        file = open(file_name)
        self.file_lines = file.readlines()
        file.close()

        # Extract the title.
        in_head = False
        index = 0
        pre_modified = False
        analytics = False
        for line in self.file_lines:
            # In the head tag.
            if search("<head>", line):
                in_head = True

            # Check the head contents, to be sure.
            if in_head:
                # Already modified.
                if index == 2 and line[:-1] == "":
                    pre_modified = True

                # Google analytics insertion.
                if index == 4 and line[:-1] == "  <!--Google analytics JS-->":
                    analytics = True

                # Check the line, skipping the title tag.
                if not pre_modified and not analytics and EXPECTED[index] != None and EXPECTED[index] != line[:-1]:
                    print("%s: Unexpected head tag encountered, quitting." % file_name)
                    print("    Encountered line:  \"%s\"" % line[:-1])
                    print("    Expected line:  \"%s\"" % EXPECTED[index])
                    sys.exit()

                # Increment the line index.
                index += 1

            # Out of the head tag.
            if search("</head>", line):
                break

            # Store the title.
            if search("<title>", line):
                title = line[:-1]

        # Return the title.
        return title


if __name__ == "__main__":
    # Check the arguments.
    if len(sys.argv) != 2:
        print("Usage:  rehead.py dir")
        sys.exit()

    # Execute the code.
    Rehead()
