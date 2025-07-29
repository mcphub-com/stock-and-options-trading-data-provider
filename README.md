markdown
# Stock and Options Trading Data Provider

## Overview

The Stock and Options Trading Data Provider is a cloud-based service that offers comprehensive stock and options data for U.S. listed stocks and ETFs. This service is designed to provide real-time data in an easy-to-consume JSON format through a RESTful API, ensuring seamless integration into your applications.

Developed by Inter Data Limited, this service is renowned for being a top-rated provider of U.S. listed stock and options data, offering the lowest cost for such services. The API is specifically designed to handle large volumes of data efficiently, making it ideal for tickers with numerous strikes and expiration dates.

## Features

- **Real-Time Data:** Access up-to-the-minute data for U.S. listed options and stocks.
- **JSON Format:** Data is provided in an easy-to-consume JSON format for seamless integration.
- **Comprehensive Coverage:** Includes options prices for all expiration dates of listed options.
- **Efficient Data Handling:** Use the "length" parameter to limit data volume and improve response times for tickers with extensive data.

## Tools and Functions

The Stock and Options Trading Data Provider offers the following tools to cater to different data needs:

### Options

- **Function Name:** `Options`
- **Description:** Provides comprehensive stock and options data.
- **Parameters:**
  - **`ticker`**: A string representing the ticker for U.S. trading stocks and ETFs. This parameter is optional.

### Straddle

- **Function Name:** `Straddle`
- **Description:** Provides data in a straddle format.
- **Parameters:**
  - **`ticker`**: A string representing the ticker for Intel Stock. This parameter is optional.

## Usage

To access stock and options data, use the following endpoint format:

```
[endpoint]/options/[ticker]
```

For improved efficiency, especially with tickers that have a large data volume, you can use the length parameter to limit the response:

```
[endpoint]/options/[ticker]?length=[number]
```

Replace `[endpoint]` with the actual endpoint URL of the service and `[ticker]` with the desired stock or ETF ticker symbol.

## Subscription Plans

The service offers a range of subscription plans to suit different needs:

- **BASIC:** Free of charge
- **PRO:** $9.99 per month
- **ULTRA:** $19.99 per month
- **MEGA:** $99.99 per month

Choose a plan that best fits your data requirements and budget.

---

This README provides a comprehensive guide to using the Stock and Options Trading Data Provider. For further details and to explore the full capabilities, please refer to the specific documentation provided with your subscription.