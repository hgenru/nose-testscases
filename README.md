nose-testscases
===============

Install
------

    $ python setup.py install

Usage
------
    $ nosetests --tests-case=case1
    $ nosetests --tests-case=case1,case2
    # The order has a value of
    $ nosetests --tests-case=case2,case1
    # You can pass the tests directly,
    # then they will run first, and then the specified cases
    $ nosetests --tests-case=case1 test4.py
