python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    # Load the dataset
    bus_routes_df = pd.read_csv('public_transportation_routes.csv')
    infrastructure_df = pd.read_excel('infrastructure_projects.xlsx')
    return bus_routes_df, infrastructure_df


def preprocess_data(bus_routes_df, infrastructure_df):
    # Basic data cleaning
    bus_routes_df.dropna(inplace=True)
    infrastructure_df.dropna(inplace=True)

    # Convert date columns to datetime
    bus_routes_df['start_date'] = pd.to_datetime(bus_routes_df['start_date'])
    infrastructure_df['completion_date'] = pd.to_datetime(infrastructure_df['completion_date'])

    return bus_routes_df, infrastructure_df


def visualize_data(bus_routes_df, infrastructure_df):
    # Visualization of bus routes
    plt.figure(figsize=(10, 6))
    sns.countplot(x='route_name', data=bus_routes_df)
    plt.title('Frequency of Bus Routes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization of infrastructure projects over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='completion_date', y='project_count', data=infrastructure_df)
    plt.title('Infrastructure Projects Over Time')
    plt.tight_layout()
    plt.show()


def main():
    bus_routes_df, infrastructure_df = load_data()
    bus_routes_df, infrastructure_df = preprocess_data(bus_routes_df, infrastructure_df)
    visualize_data(bus_routes_df, infrastructure_df)

if __name__ == "__main__":
    main()
