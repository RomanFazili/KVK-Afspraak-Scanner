import difflib
from datetime import datetime
from typing import List, Optional, Union

def format_date(date_str: str) -> str:
    """Formats the date objects given by the API from `2025-03-13T00:00:00` to `13-03-2025`"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    formatted_date = date_obj.strftime("%d-%m-%Y")
    return formatted_date

def format_dates(dates: Union[list[str], set[str]]) -> list[str]:
    """Formats the list or set of dates given by the API from `2025-03-13T00:00:00` to `13-03-2025`"""
    return ', '.join([format_date(date) for date in dates])

def get_suggestion(input_str: str, valid_options: List[str]) -> Optional[str]:
    """Get the closest match for the input string from the list of valid options."""
    matches = difflib.get_close_matches(input_str, valid_options)
    return matches[0] if matches else None

def print_suggestion(input_str: str, valid_options: List[str], input_type: str) -> None:
    """Print a suggestion for the invalid input."""
    suggestion = get_suggestion(input_str, valid_options)
    if suggestion:
        print(f"Invalid {input_type} '{input_str}'. Did you mean '{suggestion}'?")
    else:
        print(f"Invalid {input_type} '{input_str}'. No suggestions available.")