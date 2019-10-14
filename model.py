"""Simple example of LinearRegression."""
# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plot
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def import_data_and_split():
    """Train and test data split."""
    # Import the dataset
    d = pandas.read_csv("data.csv")
    x = d.iloc[:, :-1].values
    y = d.iloc[:, 1].values

    # Split the dataset into the training set and test set
    # We're splitting the data in 1/3, so out of 30 rows, 20 rows will go into the training set,
    # and 10 rows will go into the testing set.
    xTrain, xtest, y_Train, yTest = train_test_split(
        x, y, test_size=1 / 3, random_state=0
    )

    return (xTrain, xtest, y_Train, yTest)


if __name__ == "__main__":
    xTrain, xtest, y_Train, yTest = import_data_and_split()

    # Creating a LinearRegression object and fitting it
    # on our trainging set.
    linearRegressor = LinearRegression()
    linearRegressor.fit(xTrain, y_Train)

    # Predicting the test set results
    yPrediction = linearRegressor.predict(xtest)

    # Visualising the training set results
    plot.scatter(xTrain, y_Train, color="red")
    plot.plot(xTrain, linearRegressor.predict(xTrain), color="blue")
    plot.title("Salary vs Experience (Training set)")
    plot.xlabel("Years of Experience")
    plot.ylabel("Salary")
    plot.show()

    # Visualising the test set results
    plot.scatter(xtest, yTest, color="red")
    plot.plot(xtest, linearRegressor.predict(xtest), color="blue")
    plot.title("Salary vs Experience (Test set)")
    plot.xlabel("Years of Experience")
    plot.ylabel("Salary")
    plot.show()
