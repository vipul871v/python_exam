class DataStream:
    def __init__(self):
        self.last_seen: dict[str, int] = {}

    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        """
        Determines if the data string should be printed at the given timestamp.

        Args:
        timestamp (int): The current timestamp.
        data_str (str): The data string to evaluate.

        Returns:
        bool: True if the data string should be printed, False otherwise.
        """
        if data_str in self.last_seen and timestamp < self.last_seen[data_str] + 5:
            return False
        self.last_seen[data_str] = timestamp
        return True
