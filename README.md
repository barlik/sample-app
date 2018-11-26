MyApp micro service
===================

A sample micro service returning static "Hello world" message.

Building and provisioning
-------------------------

Micro service runs as a Docker container created and deployed from inside Vagrant machine.

To build and run the micro service run:

    git clone https://github.com/barlik/sample-app
    cd sample-app

    vagrant up

Running
-------

After a successful build and deployment, the micro service will be available to use on `http://192.168.100.2:80` (IP address configured in Vagrantfile). You can test the micro service by running:

    curl http://192.168.100.2/


Executing automated tests
-------------------------

Tests make use of [testinfra](https://testinfra.readthedocs.io/en/latest/index.html) testing framework.

To install testinfra run:

    pip install --user testinfra

To run tests against deployed docker container:

    ./run-tests


TODO
----

- install and run testinfra from Vagrant VM
