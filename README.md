# py-bot test text

## local build

1. Init virtual enviroment (only for first start)
    - for windows:
        ``` powershel
        py -m venv .venv
        ```
    - for linux/macOS
        ```
        python3 -m venv venv
        ```
2. Activate virtual enviroment
    - for windows:
        ``` powershel
        .venv\Scripts\Activate.ps1
        ```
    - for linux/macOS
        ```
        source venv/bin/activate
        ```
3. . Install dependencies from file `requirements.txt`
    - for all OS
        ``` 
        pip install -r requirements.txt 
        ```
4. After working save new dependencies in file `requirements.txt`
    - for all OS
        ``` 
        pip freeze > requirements.txt
        ```

## dev build 
1. Build container
    ```
    docker build -f docker/Dockerfile -t py-bot .
    ```
2. Run container
    ```
    docker run py-bot
    ```
