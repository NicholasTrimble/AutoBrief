# utils.py
from datetime import datetime, timedelta


def iso(days=0, hours=0):
    """
    Return a timestamp string in ISO format, offset by days/hours.
    Example: "2025-10-13T12:34:56.789Z"
    """
    # Ensure dt is always a datetime object
    dt = datetime.utcnow() - timedelta(days=days, hours=hours)

    # Convert to ISO format string
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def short_sha():
    """Producing a fake sha"""
    return datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S')
