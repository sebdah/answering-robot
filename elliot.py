#!/usr/bin/env python

"""
Elliot
"""

import os
import sys
import optparse
try:
    import pymongo
except ImportError:
    print 'Module pymongo not found. Install it via e.g. pip install pymongo'
    sys.exit(1)

def main():
    """
    Main method
    """
    parser = optparse.OptionParser( conflict_handler = "resolve",
                                    description = "Elliot manager")

    parser.add_option(  '-h', '--host',
                        action = 'store', type = 'string',
                        dest = 'host', default = '127.0.0.1',
                        help = 'MongoDB hostname')
    parser.add_option(  '-p', '--port',
                        action = 'store', type = 'int',
                        dest = 'port', default = 27017,
                        help = 'MongoDB port number')
    parser.add_option(  '-d', '--database',
                        action = 'store', type = 'string',
                        dest = 'database', default = '',
                        help = 'MongoDB database name')
    parser.add_option(  '--import',
                        action = 'store', type = 'string',
                        dest = 'import_answer', default = '',
                        help = 'Import an answer to MongoDB. Give the path as an argument')
    options, _ = parser.parse_args()

    # Check that the database option was given
    if options.database == '':
        print "Missing option --database"
        parser.print_help()
        sys.exit(1)
    
    # Create the connection to MongoDB
    try:
        mongodb_connection = pymongo.Connection(options.host, options.port)
    except pymongo.errors.ConnectionFailure:
        print "Could not connect to %s:%i" % (options.host, options.port)
        sys.exit(1)
    
    # If import
    if options.import_answer != '':
        import_answer(options.import_answer, mongodb_connection)

def import_answer(answer_markdown, mongodb_connection):
    """
    Import an answer to MongoDB
    """
    # Check that the markdown file exists
    if not os.path.exists(answer_markdown):
        print "File not found: %s" % (answer_markdown)
    
    # Parse the markdown file
    file_handle = open(answer_markdown, 'r')
    
    file_data = file_handle.readlines()
    print file_data[0].replace('\n', '')
    
if __name__ == "__main__":
    main()
    sys.exit(0)
