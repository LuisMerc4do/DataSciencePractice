# **Vector**: A sequence of data elements of the same type
# Creating a vector of numeric values representing monthly sales
monthly_sales <- c(5000, 7000, 6000, 6500, 7200)
print(monthly_sales)  # Displaying the vector

# **Matrix**: A two-dimensional array with elements of the same data type
# Creating a matrix of sales data for two products over 3 months
sales_matrix <- matrix(c(1200, 1500, 1300, 1400, 1600, 1550), nrow = 3, byrow = TRUE)
print(sales_matrix)  # Displaying the matrix
# Rows represent months, columns represent products

# **Data Frame**: Can hold different data types in each column
# Creating a data frame with columns for month, sales, and profit
sales_data <- data.frame(
  Month = c("January", "February", "March"),
  Sales = c(8000, 8500, 9000),
  Profit = c(2000, 2200, 2400)
)
print(sales_data)  # Displaying the data frame
# Each column can hold different types of data (e.g., text for Month, numeric for Sales and Profit)

# **List**: An ordered collection of objects of different types and lengths
# Creating a list that combines the vector, matrix, and data frame created above
data_summary <- list(
  MonthlySales = monthly_sales,
  SalesMatrix = sales_matrix,
  SalesDataFrame = sales_data
)
print(data_summary)  # Displaying the list
# A list can contain objects of various types and structures, like vectors, matrices, and data frames