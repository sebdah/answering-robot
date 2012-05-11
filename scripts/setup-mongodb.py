#!/usr/bin/env python

"""
Install all requirements in MongoDB
"""

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
                                    description = "Install Elliot MongoDB")
    
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
    options, _ = parser.parse_args()
    
    # Check that the database option was given
    if options.database == '':
        print "Missing option --database"
        parser.print_help()
        sys.exit(1)
    
    # Create the connection
    try:
        con = pymongo.Connection(options.host, options.port)
    except pymongo.errors.ConnectionFailure:
        print "Could not connect to %s:%i" % (options.host, options.port)
        sys.exit(1)
    
    # Create the database
    database = con[options.database]
    
    # Create collection - answers
    if 'answers' not in database.collection_names():
        database.create_collection('answers')
    collection = database['answers']
    collection.ensure_index('a', unique = True)
    
    # Create collection - keywords
    if 'keywords' not in database.collection_names():
        database.create_collection('keywords')
    collection = database['keywords']
    collection.ensure_index('k', unique = True)

    print "Database %s created" % (options.database)

if __name__ == "__main__":
    main()
    sys.exit(0)
