# **Airbnb Listings EDA Project: New York 2024**  

## Project Overview   

This project explores the New York Airbnb dataset through comprehensive Exploratory Data Analysis (EDA) to identify key trends and patterns in rental listings. It leverages powerful libraries like Pandas, NumPy, Matplotlib, and Seaborn for data cleaning, visualization, and insightful analysis.   

![New York City](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmoRqBDH2UEA2ieApEhLVWdTvS99InlWK8gA)   

## Objective  

The goal of this project is to:

* Analyze room types, prices, and availability across different neighborhoods.  
* Understand host behavior and listing patterns.  
* Detect potential outliers in prices.  
* Provide recommendations for guests and hosts based on insights.

## Dataset  

The dataset contains 20,765 entries and 22 features, including:

id: Unique identifier for each listing  
- name: Title of the Airbnb listing
- host_name: Name of the host
- neighborhood_group: Group (borough) where the listing is located
- latitude/longitude: Geolocation of listings
- price: Nightly rental price
- room_type: Type of accommodation (e.g., entire home, private room)
- reviews_per_month: Average monthly reviews for the listing
- availability_365: Number of available days in the year

## Steps and Workflow  

1. Data Cleanin
Handle missing data: price, neighborhood, and beds columns had null values.
Fix data types: Converted last_review to a datetime object.
Remove outliers: Listings with prices > $1,000 were capped to avoid skewed visualizations.
3. EDA (Exploratory Data Analysis)
Room type distribution:

Visualized the count of each room type using bar plots.  
Identified Entire home/apt as the most common room type.  
Neighborhood group insights:  

Analyzed price variations by boroughs.  
Manhattan had the highest average prices.  
Availability trends:  

Used heatmaps to show correlations among price, availability_365, number_of_reviews, and beds.  
Price distribution:  
Used histograms to show the distribution of prices.  
Majority of the listings were priced between $50 - $300.  

Host listings:  

Analyzed hosts with multiple listings using boxplots to identify key contributors.
Review behavior:  

Used pair plots to show relationships between number of reviews, price, and availability.  

3. Data Visualization
Pairplot: To see correlations among price, availability, and number of reviews.
Heatmap: Showing correlations among numerical features.
Histograms and Boxplots: To detect outliers in price.
Bar Charts: Displaying room types and neighborhood group distributions.

