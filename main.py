import pandas as pd
import gin



def hello_world(text:str):
    print(text)
    return


if __name__ == '__main__':

    gin.parse_config_file('config.gin')

    #no config
    hello_world('hello')
    hello_world(17)