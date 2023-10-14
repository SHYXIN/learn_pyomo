"""
Function                    Description
pyomo_preprocess            Perform a preprocessing step before model construction
pyomo_create_model          Construct and return a model object
pyomo_create_modeldata      Construct and return a DataPortal object
pyomo_print_model           Output model object information
pyomo_modify_instance        Modify the model instance
pyomo_print_instance        Output model instance information
pyomo_save_instance         Save the model instance
pyomo_print_results         Print the optimization results
pyomo_save_results          Save the optimization results
pyomo_postprocess           Perform a postprocess step after optimization
"""
def pyomo_print_results(options=None, instance=None, results=None):
    print(results)

# pyomo_preprocess
def pyomo_preprocess(options=None):
    print("Here are the options that were provided")
    if options is not None:
        options.display()

# pyomo_create_model
import sys
from os.path import abspath, dirname

def pyomo_create_model(options=None, model_options=None):
    sys.path.append(abspath(dirname(__file__)))
    abstract6 = __import__('abstract6')
    sys.path.remove(abspath(dirname(__file__)))
    return abstract6.Model

# pyomo_create_modeldata
import pyomo.environ as pyo

def pyomo_create_dataportal(options=None, model=None):
    data = pyo.DataPortal(model=model)
    data.load(filename='abstract6.dat')
    return data

# pyomo_modify_instance
def pyomo_modify_instance(options=None, model=None, instance=None):
    instance.x[1].value = 0.0
    instance.x[1].fixed = True

def pyomo_print_instance(options=None, instance=None):
    if options['runtime']['logging']:
        instance.pprint()

import pickle
def pyomo_save_instance(options=None, instance=None):
    OUTPUT = open('abstract7.pyomo', 'w')
    OUTPUT.write(str(pickle.dumps(instance)))
    OUTPUT.close()

def pyomo_print_results(options=None, instance=None, results=None):
    print(results)

def pyomo_save_results(options=None, instance=None, results=None):
    OUTPUT = open('abstract7.results', 'w')
    OUTPUT.write(str(results))
    OUTPUT.close()

def pyomo_postprocess(options=None, instance=None, results=None):
    instance.solutions.load_from(results, allow_consistent_values_for_fixed_vars=True)
    print("Solutin value " + str(pyo.value(instance.obj)))
