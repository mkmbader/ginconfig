import gin
import random

@gin.configurable()
def function(name = gin.REQUIRED, food = gin.REQUIRED, price = gin.REQUIRED):
    '''print favorite food'''
    print('%s likes %s, if cheaper than %s euro.' %(name, food, round(price,2)))
    return


gin.external_configurable(random.uniform)

if __name__ == '__main__':
    gin.parse_config_file('config.gin')

    with gin.config_scope('maria'): function()
    with gin.config_scope('ana'): function()
