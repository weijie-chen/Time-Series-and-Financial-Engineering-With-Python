"""Utility functions for financial engineering.
"""

import datetime as dt

import numpy as np
import pandas as pd
import scipy as sp
import yfinance as yf
from const.numbers import *


def download_data(
    security: list[str],
    dropna: bool,
    start_date: dt.date,
    end_date: dt.date,
    column: list[str] = ["Close"],
) -> pd.DataFrame:
    """
    Download historical data from Yahoo Finance.
    Args:
        security: List of tickers.
        dropna: Drop missing values.
        start_date: Start date.
        end_date: End date.
        column: Column to pick, default to close.
    Returns:
        pd.DataFrame: DataFrame with historical price.
    """

    security_df = pd.DataFrame()
    for i in security:
        ticker = yf.Ticker(i)
        security_df[i] = ticker.history(start=start_date, end=end_date)[column]
    if dropna == True:
        df = pd.DataFrame(security_df).dropna()
    else:
        df = pd.DataFrame(security_df)
    return df


def calculate_parametric_var(value, confidence, mu, sigma) -> float:
    """
    Calculate the parametric VaR using the normal distribution.
    Args:
        value: The value of the portfolio.
        confidence: The confidence level.
        mu: Annualized expected return of the portfolio.
        sigma: Annualized volatility of the portfolio.
    Returns:
        float: Annual parametric VaR.
    """
    F_inv = sp.stats.norm.ppf(1 - confidence)
    para_var = abs(value * (mu - sigma * F_inv))

    return para_var


def simulate_stocks(iterations, s_0, mu, sigma, n) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate stock prices using Geometric Brownian Motion.
    Args:
        iterations: Number of iterations.
        s_0: Initial stock price.
        mu: Expected return.
        sigma: Volatility.
        n: Number of trading days.
    returns:
        tuple[np.ndarray, np.ndarray]: Stock prices and returns.
    """
    rand_w = np.random.standard_normal(iterations)
    s_t = s_0 * np.exp((mu - 0.5 * sigma**2) * n + sigma * np.sqrt(n) * rand_w)
    returns = s_t / s_0 - 1

    return s_t, returns


def age_weight_series(num_period: int, decay_param: float) -> pd.Series:
    """
    Generate a series of weights for exponential decay.
    Args:
        num_period: Number of periods.
        decay_param: Decay parameter.
    Returns:
        pd.Series: Series of weights.
    """
    return pd.Series(
        [
            (decay_param ** (i - 1) * (1 - decay_param)) / (1 - decay_param**num_period)
            for i in range(1, num_period + 1)
        ]
    )
