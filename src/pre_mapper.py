#!/usr/bin/python3
ROOT = "./res/"
def get_configs():
    with open(f"{ROOT}network_info.txt", "r+") as file:
        current_layer_number = int(file.readline()) + 1
        number_of_layers = int(file.readline())
        file.seek(0)

        if(current_layer_number > number_of_layers):
            return
        else:
            file.writelines([f"{current_layer_number}\n", f"{number_of_layers}\n"])
            edit_input(current_layer_number)

        return 1 if current_layer_number != number_of_layers else 0



def edit_input(layer_number):
    weights_file = open(f"{ROOT}w{layer_number}.txt", "r")
    weights = weights_file.readlines()
    weights_file.close()
    data_file = open(f"{ROOT}temp.txt", "r")
    data = data_file.readlines()

    with open(f"{ROOT}input.txt", "w") as input_file:
        input_file.writelines(data)

    with open(f"{ROOT}input.txt", "a") as input_file:
        input_file.writelines(weights)

if __name__ == "__main__":
    print(get_configs())