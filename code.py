import csv
import pandas as bear
import plotly.figure_factory as ff
import statistics as stats

df = bear.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

'''
def height(height_list):
    height_mean = stats.mean(height_list)
    height_median = stats.median(height_list)
    height_mode = stats.mode(height_list)
    height_stdev = stats.stdev(height_list)

    print("--------------------")

    print(f"Mean, Median, Mode, Stdev of Height is {height_mean}, {height_median}, {height_mode}, & {height_stdev} respectively.")

    height_first_stdev_start, height_first_stdev_end = height_mean-height_stdev, height_mean+height_stdev
    height_second_stdev_start, height_second_stdev_end = height_mean-(2*height_stdev), height_mean+(2*height_stdev)
    height_third_stdev_start, height_third_stdev_end = height_mean-(3*height_stdev), height_mean+(3*height_stdev)

    height_list_data_within_1_stdev = [result for result in height_list if result > height_first_stdev_start and result < height_first_stdev_end]
    height_list_data_within_2_stdev = [result for result in height_list if result > height_second_stdev_start and result < height_second_stdev_end]
    height_list_data_within_3_stdev = [result for result in height_list if result > height_third_stdev_start and result < height_third_stdev_end]

    print("--------------------")

    print("{}% of data for height lies within the 1st standard deviation".format(len(height_list_data_within_1_stdev)*100.0/len(height_list)))
    print("{}% of data for height lies within the 2nd standard deviation".format(len(height_list_data_within_2_stdev)*100.0/len(height_list)))
    print("{}% of data for height lies within the 3rd standard deviation".format(len(height_list_data_within_3_stdev)*100.0/len(height_list)))

    print("--------------------")
'''
#elif ():
weight_mean = stats.mean(weight_list)
weight_median = stats.median(weight_list)
weight_mode = stats.mode(weight_list)
weight_stdev = stats.stdev(weight_list)

print("--------------------")

print(f"Mean, Median, Mode, Stdev of Weight is {weight_mean}, {weight_median}, {weight_mode}, & {weight_stdev} respectively.")

weight_first_stdev_start, weight_first_stdev_end = weight_mean-weight_stdev, weight_mean+weight_stdev
weight_second_stdev_start, weight_second_stdev_end = weight_mean-(2*weight_stdev), weight_mean+(2*weight_stdev)
weight_third_stdev_start, weight_third_stdev_end = weight_mean-(3*weight_stdev), weight_mean+(3*weight_stdev)

weight_list_data_within_1_stdev = [result for result in weight_list if result > weight_first_stdev_start and result < weight_first_stdev_end]
weight_list_data_within_2_stdev = [result for result in weight_list if result > weight_second_stdev_start and result < weight_second_stdev_end]
weight_list_data_within_3_stdev = [result for result in weight_list if result > weight_third_stdev_start and result < weight_third_stdev_end]

print("--------------------")

print("{}% of data for weight lies within the 1st standard deviation".format(len(weight_list_data_within_1_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within the 2nd standard deviation".format(len(weight_list_data_within_2_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within the 3rd standard deviation".format(len(weight_list_data_within_3_stdev)*100.0/len(weight_list)))

print("--------------------")