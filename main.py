import pandas as pd
import gin #pylint:disable=import-error
# from pydantic import StrictStr  # pylint: disable=no-name-in-module
# type hinting: https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in


@gin.configurable
def hello_world(name:str, loc:str=gin.REQUIRED):
    print('Hello %s, %s' %(name, loc))
    return


if __name__ == '__main__':

    gin.enter_interactive_mode() 
    gin.parse_config_file('config.gin')

    #no config used -> I can force these values
    hello_world('world', 'around')
    hello_world(17, 13)

    # this uses the config values
    hello_world()