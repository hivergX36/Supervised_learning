from  Regression import regression 

Reg = regression()
file_name = "data.txt"
Reg.parse_data(file_name)
print(Reg.Labels)
print(Reg.Predictor)
Reg.regression_coefficient_least_square()