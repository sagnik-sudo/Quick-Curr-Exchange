# Quick Curr Exchange

## What is Outlive Weather Master?

Currency Conversion tool useful for most web based and API applications. This supports historical data as well.

Live API is up at [quickcurrx.deta.dev](quickcurrx.deta.dev)

If you like my work, consider giving a star :)

## API Documentation

This section defines the expected Input and the Output formats for the Currency Conversion tool.

## Installation

- Step 1: Enable a virtual environment

    ```bash
    python3 -m virtualenv venv
    ```

- Step 2: Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

- Step 3: Run the application

    ```bash
    uvicorn main:app --reload
    ```

- Step 4: Checkout Swagger UI

    Open the browser and navigate to `http://127.0.0.1:8000/currencies#/`

## Useful for Developers

- Get the live currency conversion for a set of amount using the API
- Create a currency conversion widget using the API
- Useful for implementation inside a website

## Feedback

If you have any feedback, please reach out to us at sagnikdas2305@gmail.com

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.