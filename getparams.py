import configparser


def get_url(ini):
    config = configparser.ConfigParser()
    config.read(ini)
    result = str(config['urls']['url'])
    return result