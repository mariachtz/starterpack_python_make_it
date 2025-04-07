from flask import Flask


# Create a webserver object and keep track of it in the variable server
server = Flask('Generative Art')

# Define an HTTP route /io
@server.route('/io')


# Define the function 'welcome_to_io()' and connect it to the route /io
def welcome_to_io():

    # Return a message 'Welcome to IO!' to the client
    return "Welcome to IO!"

# Start the webserver
server.run('0.0.0.0')