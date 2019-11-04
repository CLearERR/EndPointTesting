import configparser


def get_url(ini):
    config = configparser.ConfigParser()
    config.read(ini)
    result = str(config['urls']['url'])
    return result

def get_conf(ini):
    config = configparser.ConfigParser()
    config.read(ini)
    return config
