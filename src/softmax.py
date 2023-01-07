import numpy as np
import pandas as pd

def main():
    ROOT = "./res/"
    cache_file = open(f"{ROOT}cache.txt")
    num_of_records = int(cache_file.readline().split(",")[0])
    cache_file.close()

    output_file = open(f"{ROOT}temp.txt")
    output_dict = {}


    values_list = []

    for line in output_file.readlines():
        temp = line.strip().split(",")
        output_dict[(int(temp[1]),int(temp[2]))] = float(temp[3])

    output_file.close()    

    # print(output_dict.keys())
    for i in range(num_of_records):
        values_list.append([])
        for j in range(10):
            values_list[i].append(output_dict[(i,j)])

    classifcations = []
    for i in range(num_of_records):
        e = np.exp(values_list[i])
        classifcations.append(np.argmax(e / e.sum()))
    df = pd.DataFrame({"prediction":classifcations})
    df.to_csv(f"{ROOT}predictions.csv", index=False)

if __name__ == "__main__":
    main()