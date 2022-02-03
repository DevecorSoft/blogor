import yaml
from yaml import Loader
import sys

if __name__ == '__main__':
    arg_yaml = sys.argv[1]
    with open(arg_yaml, 'r') as f:
        compose = yaml.load(f.read(), Loader)
        print(compose.get('services').get('blogor').get('image').split(':')[-1])
        f.close()
