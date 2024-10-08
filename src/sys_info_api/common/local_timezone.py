# From https://docs.python.org/3/library/datetime.html#tzinfo-objects

from datetime import tzinfo, timedelta, datetime
import time as _time

ZERO = timedelta(0)
HOUR = timedelta(hours=1)
SECOND = timedelta(seconds=1)

# A class capturing the platform's idea of local time.
# (May result in wrong values on historical times in
#  timezones where UTC offset and/or the DST rules had
#  changed in the past.)

STDOFFSET = timedelta(seconds=-_time.timezone)
if _time.daylight:
	DSTOFFSET = timedelta(seconds=-_time.altzone)
else:
	DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET


class LocalTimezone(tzinfo):

	def fromutc(self, dt):
		assert dt.tzinfo is self
		stamp = (dt - datetime(1970, 1, 1, tzinfo=self)) // SECOND
		args = _time.localtime(stamp)[:6]
		dst_diff = DSTDIFF // SECOND
		# Detect fold
		fold = (args == _time.localtime(stamp - dst_diff))
		return datetime(
			*args,
			microsecond=dt.microsecond,
			tzinfo=self, fold=fold
		)

	def utcoffset(self, dt):
		if self._isdst(dt):
			return DSTOFFSET
		else:
			return STDOFFSET

	def dst(self, dt):
		if self._isdst(dt):
			return DSTDIFF
		else:
			return ZERO

	def tzname(self, dt):
		return _time.tzname[self._isdst(dt)]

	def _isdst(self, dt):
		tt = (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday(), 0, 0)
		stamp = _time.mktime(tt)
		tt = _time.localtime(stamp)
		return tt.tm_isdst > 0
