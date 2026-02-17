 # ---------------- FILE UTILITIES ----------------
    @staticmethod
    def read_file(filepath: str) -> Optional[str]:
        """Read and return the contents of a file."""
        if not isinstance(filepath, str):
            raise TypeError("File path must be a string.")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_file(filepath: str, content: str) -> None:
        """Write content to a file."""
        if not isinstance(filepath, str) or not isinstance(content, str):
            raise TypeError("File path and content must be strings.")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    # ---------------- DATE/TIME UTILITIES ----------------
    @staticmethod
    def current_datetime(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
        """Return the current date and time as a formatted string."""
        if not isinstance(fmt, str):
            raise TypeError("Format must be a string.")
        return datetime.datetime.now().strftime(fmt)

    @staticmethod
    def days_between(date1: str, date2: str, fmt: str = "%Y-%m-%d") -> int:
        """Return the number of days between two dates."""
        try:
            d1 = datetime.datetime.strptime(date1, fmt)
            d2 = datetime.datetime.strptime(date2, fmt)
        except ValueError:
            raise ValueError("Dates must match the given format.")
        return abs((d2 - d1).days)

