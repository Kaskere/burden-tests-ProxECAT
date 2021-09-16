import os

if __name__ == '__main__':
    files = os.listdir("./")
    for file in files:
        if file.endswith('fragment.vcf'): #'vep_sample.vcf'
            new_file_name = os.path.splitext(file)[0] + '_1609variants'
            output = open(new_file_name + ".vcf", "w")

            with open(file, 'rt') as f:
                data = f.readlines()
                Count = 0
                for line in data:
                    if line[0] == "#":
                        output.write(line)
                    if line.__contains__('synonymous_variant'): 
                        output.write(line)
                        Count += 1
            output.close()
            f.close()
            os.rename(new_file_name + ".vcf", new_file_name + "_syn" + str(Count) + ".vcf")
