import cProfile
import re


cProfile.run('re.compile("for|bar")', 'restats')
