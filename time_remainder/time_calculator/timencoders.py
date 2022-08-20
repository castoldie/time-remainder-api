from datetime import datetime

def date_diff_in_seconds(dt2: datetime, dt1: datetime):

  delta = dt2 - dt1

  return delta.days * 24 * 3600 + delta.seconds

def dhms_from_seconds(seconds):

	minutes, seconds = divmod(seconds, 60)

	hours, minutes = divmod(minutes, 60)

	days, hours = divmod(hours, 24)

	return (days, hours, minutes, seconds)