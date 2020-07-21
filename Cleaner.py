import os

def clear_cache():
    main_path = os.path.dirname(os.path.realpath(__file__)) 
    cache_path = main_path = "\cache"

    os.remove(cache_path+"\info.cache")
    os.remove(cache_path+"\Display.jpg")
    os.remove(cache_path+"\DisplayBuffer.jpg")

