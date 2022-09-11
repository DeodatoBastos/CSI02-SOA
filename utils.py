from operator import le
from turtle import left
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_data(url: str) -> pd.DataFrame:
    response: requests.Response = requests.get(url)
    data: str = response.text
    parse_data: list[dict[str, str]] = json.loads(data)
    df: pd.DataFrame = pd.DataFrame(parse_data)

    return df


def join_data_frames(first_df: pd.DataFrame, second_df: pd.DataFrame, old_name: str = None,
                     first_new_name: str = None, second_new_name: str = None) -> pd.DataFrame:
    if old_name is not None:
        first_df.rename(columns={old_name: first_new_name}, inplace=True)
        second_df.rename(columns={old_name: second_new_name}, inplace=True)

    new_df: pd.DataFrame = pd.merge(left=first_df, right=second_df, how="left")

    return new_df


def plot_time_series(df: pd.DataFrame, x_name: str, y_name: str, title: str,
                     xlabel: str, ylabel: str) -> None:
    sns.set_theme(style="darkgrid")
    ax = sns.lineplot(x=x_name, y=y_name, data=df)
    ax.set_title(title, weight='bold', size=18)
    ax.set_xlabel(xlabel, size=12)
    ax.set_ylabel(ylabel, size=12)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


def plot_data(df: pd.DataFrame, x_name: str, y_name: str,
              title: str, xlabel: str, ylabel: str) -> None:
    ax = sns.scatterplot(data=df, x=x_name, y=y_name)
    ax.set_title(title, weight='bold', size=18)
    ax.set_xlabel(xlabel, size=12)
    ax.set_ylabel(ylabel, size=12)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()
