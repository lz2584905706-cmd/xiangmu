import os

CONFIG={"base_url":"https://reqres.in","timeout":5}

def get_config(key):
    return CONFIG.get(key)