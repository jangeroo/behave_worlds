# OVERVIEW
This project is an exploration of a Python implementation of the Worlds concept from Cucumber.

The feature file describes a single scenario of withdrawing cash from an ATM, based on the examples from The Cucumber Book.

The scenario has been implemented in three worlds:
1. Default (this is essentially the domain model)
2. API (REST-ish)
3. GUI (Web/Selenium-ish)

# EXECUTION
Run the scenario in the default world with: 

    bash
    $ behave --no-capture -o /dev/null

**Note:**
- `--no-capture` allows the print statements to be printed to stdout
- `-o /dev/null` suppresses the standard Behave output to make the print statements more readable. This is optional

The other two worlds are accessed by passing a `--stage` parameter:

    bash
    $ behave --no-capture -o /dev/null --stage=api
    $ behave --no-capture -o /dev/null --stage=gui

# EXPLANATION
Ideally, a single set of feature files would be implemented using a single set of step definitions, acting as a translation layer that simply references a domain model. This domain model would then implemented for each of the various worlds. Behave's [test stages|https://behave.readthedocs.io/en/latest/new_and_noteworthy_v1.2.5.html#test-stages] are implemented in such a way that requires multiple sets of step definitions, one for each "stage", or world. To work around this, the default steps serve as the single set of step definitions, and the step files for each of the other worlds simply import these. The world-specific implementions of the domain objects are injected at runtime into Behave's Context object in the `[world_]environment.py` files.

(**Note:** Neither the API nor GUI worlds have a 'real' implementation. Each method in these worlds prints a text description of how the step would be executed in that world, and then just calls the default world method in order to allow the execution to pass.)

