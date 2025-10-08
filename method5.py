from scipy.stats import f_oneway

group1 = [20, 23, 23, 25, 21]
group2 = [30, 30, 27, 25, 28]
group3 = [25, 20, 30, 31, 22]

F_statistic, p_value = f_oneway(group1, group2, group3)
print("F-Statistic:", F_statistic, "p-value:", p_value)
