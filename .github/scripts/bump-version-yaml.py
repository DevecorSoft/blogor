import yaml
from yaml import Loader
import sys

if __name__ == '__main__':
    arg_yaml = sys.argv[1]
    version = sys.argv[2]
    with open(arg_yaml, 'r') as f:
        compose = yaml.load(f.read(), Loader)
        tag = compose['services']['blogor']['image'].split(':')
        compose['services']['blogor']['image'] = ':'.join((tag[0], version))
        f.close()
    with open(arg_yaml, 'w') as f:
        f.write(yaml.dump(compose))
        f.close()
