import gin
import random
import typer

# allows typer commands
app = typer.Typer()

# configurables for gin
@gin.configurable()
def function(name, food, price=gin.REQUIRED):
    '''print favorite food'''
    print('%s likes %s, if cheaper than %s.' %(name, food, round(price, 2)))
    return

# make existing function configurable
gin.external_configurable(random.uniform)

# example to outline gin-config functionalities
@app.command('config')
def gin_config_example():

    gin.parse_config_file('config.gin')

    # root scope
    function()

    # sub-scope
    with gin.config_scope('ana'): function()
    with gin.config_scope('wessel'): function()

# example to outline typer functionalities
@app.command('typer')
def typer_example(scope:str, showroot:bool = True):

    gin.parse_config_file('config.gin')

    # root scope
    if showroot:
        function()
  
    # sub-scope
    with gin.config_scope(scope): function()



def cli() -> None:
    """Helper function to start cli via poetry scripts."""
    app()

if __name__ == '__main__':
    app()



