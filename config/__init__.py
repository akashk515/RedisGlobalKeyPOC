import yaml


def load_config():
    # Load the YAML config file
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config
