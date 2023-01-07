#!/usr/bin/python
ROOT = "./res/"
def edit_cache():
    global ROOT
    file  = open(f"{ROOT}network_info.txt", "r")
    current_layer_number = int(file.readline())
    file.close()
    
    cache_file = open(f"{ROOT}cache.txt", "r")
    lines = cache_file.readlines()
    # lines = list(map(lambda line: line.strip(),cache_file.readlines()))
    cache_file.close()

    cache_file = open(f"{ROOT}cache.txt", "w")
    temp = lines[0].split(',')
    d = lines[current_layer_number]
    lines[0] = f'{temp[0]},{d}\n'
    cache_file.writelines(lines)
    cache_file.close()


if __name__ == "__main__":
    edit_cache()