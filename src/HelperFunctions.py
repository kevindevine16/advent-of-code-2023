from IPython import get_ipython

def convert_to_py(prefix:str): 
    get_ipython().system(f'jupyter nbconvert --to script {prefix}.ipynb --output {prefix}_raw')
