import matplotlib.pyplot as plt
x_measurements=[]
measurements=[]
fh=open('case5.txt')
for i in fh:
    i=i.split(',')
    x_measurements.append(i[0])
    measurements.append(int(i[1]))

#initial values for both estimate and variance

#consider the error in our measuring device doesn't change
measurment_var=6
#consider th first measurment our prior estimate
#so just for first iteration it wil be the measurment and the estimate
#as we don't a have a model to make an initial estimate
estimate=measurements[0]
estimate_var=4
#KG=estimate_var / (estimate_var + measurment_var)
x=len(measurements)
f_estimates=[]
for i in range(x):
    KG = estimate_var / (estimate_var + measurment_var)
    estimate = estimate + KG * (measurements[i] - estimate)
    f_estimates.append(estimate)
    estimate_var = (1 - KG) * estimate_var
print(len(f_estimates))
print(len(x_measurements))
#print(estimate)
fig1=plt.figure()
axis1=fig1.add_subplot(111)
axis1.scatter(x_measurements, measurements,  color='red', s=1)
axis1.scatter(x_measurements, f_estimates,  color='blue', s=1)

plt.show()