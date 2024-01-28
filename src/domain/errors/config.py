class MissingEnvKey(Exception):
    def __init__(self, key: str) -> None:
        super().__init__(f"Env file has a missing key [{key}]")
