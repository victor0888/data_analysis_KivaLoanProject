from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

df = pd.read_csv(r'Medical\\DataCleaning\\DataTransformation\\KivaLoanProject\\kiva_data.csv')
print(df.head(25))

# Creates the figure
f, ax = plt.subplots(figsize=(15, 10))

# Plot the data
sns.barplot(data=df, x="country", y = "loan_amount")

# Use part of the code above to format the y-axis ticks below this line
sns.barplot(data=df, x="country", y="loan_amount", hue="gender")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.show()
plt.clf()
# On average, do female or male recipients receive larger loans from Kiva? 
# On average, male recepient receive larger loans from Kiva.
# Which country has the least disparity in loan amounts awarded by gender?
# It looks like El Salvador appears have the smallest disparity in loan amounts (by gender).
# Based on the data, what kind of recommendations can you make to Kiva about the loans they give?
# Kiva should work to decrease the gap between gender loan.
# What actions could be taken to implement the recommendations you've made?
# Some actions could be:

# Kiva could hold workshops focused on women-led projects (to see more women-led project)
# Kiva could require that an equal amount of loans be given to male and female-driven projects

# Set color palette
sns.set_palette("Accent")

# Set style
sns.set_style("darkgrid")

# Create figure and axes (no need to use the previous syntax, as the y-label ticks aren't going to be formatted)
plt.figure(figsize=(25, 15))

# Add a title
ax.set_title("Loan Amounts")

# Use Seaborn to create the bar plot
sns.barplot(data=df, x="country", y="loan_amount", hue="gender")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.show()
plt.clf()
# Box Plots With Kiva Data
plt.figure(figsize=(16, 10))
sns.boxplot(data=df,x="country",y="loan_amount")
plt.show()
plt.clf()
# Which country's box has the widest distribution?
# Kenya
# In which country would you be most likely to receive the largest loan amount?
# Cambodia


# Box Plot by Activity
plt.figure(figsize=(16, 10))

sns.boxplot(data=df,x="activity",y="loan_amount")
plt.show()
plt.clf()
# What does this visualization reveal that previous ones did not?
# The loan amount are grouped by activity intead of country with Farming activities having the most loans.

# Violin Plots
plt.figure(figsize=(16, 10))

sns.violinplot(data=df, x="activity", y="loan_amount")
plt.show()
plt.clf()
# Create a violin plot that visualizes the distribution of loan amount by country.
# Split Violin Plots by gender
# Some styling (feel free to modify)
sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))
sns.violinplot(data=df, x="country", y="loan_amount", hue="gender", split=True)
plt.show()
plt.clf()
# What does this visualization reveal about the distribution of loan amounts within countries by gender?
# The average amount of loans that is givent to male gender is higher overall, accept to El Salvador.

#plt.show() # Show the plot
#plt.clf() # Clear the plot