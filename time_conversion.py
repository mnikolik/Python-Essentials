def to_24_hour_clock(hours):
    ''' (number) -> number
    Return the hour as seen on a 24-hour clock.
    Precondition: hours >= 0.
    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    '''

    return hours % 24



def convert_to_minutes(hours):
    ''' (int) -> int
    Return the number of minutes there are in
    given hours. 1h = 60min
    >>> convert_to_minutes(3)
    180
    >>> convert_to_minutes(5)
    300
    >>> convert_to_minutes(10)
    600
    '''

    return hours * 60


def convert_to_seconds(hours):
    ''' (int) -> int
    Return the number of seconds there are in
    given hours. 1h = 3600s
    >>> convert_to_seconds(3)
    10800
    >>> convert_to_seconds(5)
    18000
    >>> convert_to_seconds(10)
    36000
    '''

    return convert_to_minutes(hours) * 60



def get_hours(seconds):
    ''' (int) -> int
    Return the number of hours that have elapsed since midnight,
    as seen on a 24-hour clock, by given input seconds.
    >>> get_hours(60)
    0 
    >>> get_hours(3800)
    1
    >>> get_hours(37000)
    10
    '''
    hours_all = seconds//3600
    return to_24_hour_clock(hours_all)




def get_minutes(seconds):
    ''' (int) -> int
    Return the number of minutes that have elapsed since midnight
    as seen on a clock, by given input seconds, and after reducing
    the integer hours.
    >>> get_minutes(60)
    1
    >>> get_minutes(3800)
    3
    >>> get_minutes(37000)
    16
    '''

    return (seconds%3600)//60




def get_seconds(seconds):
    ''' (int) -> int
    Return the number of seconds that have elapsed since midnight
    as seen on a clock, by given input seconds, and after reducing
    the integre hours and integer seconds. 
    >>>get_seconds(60)
    0
    >>> get_seconds(3800)
    20
    >>> get_seconds(37000)
    40
    '''
    
    return (seconds%3600)%60




def to_float_hours(hours, minutes, seconds):
    '''(int, int, int) -> float
    Return the total number of hours in float format,
    by given input of hours, minutes, and seconds.
    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60
    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(3, 45, 45)
    3.7625
    >>> to_float_hours(10, 0, 22)
    10.006
    '''
    
    return hours + (minutes/60) + (seconds/3600)





def time_to_utc(utc_offset, time):
    ''' (number, float) -> float
    Return time at UTC+0, where utc_offset is the time zone away from
    UTC+0.
    >>> time_to_utc(+2, 12.0)
    10.0
    >>> time_to_utc(-2, 12.0)
    14.0
    >>> time_to_utc(+11, 18.0)
    7.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(+1, 23.0)
    22.0
    >>> time_to_utc(-1, 23.0)
    0.0
    '''
    time_to = time - utc_offset
    return to_24_hour_clock(time_to)



def time_from_utc(utc_offset, time):
    ''' (number, float) -> float
    Return UTC time in time zone utc_offset.
    >>> time_from_utc(+2, 12.0)
    14.0
    >>> time_from_utc(-2, 12.0)
    10.0
    >>> time_from_utc(+11, 18.0)
    5.0
    >>> time_from_utc(-11, 18.0)
    7.0
    >>> time_from_utc(+1, 23.0)
    0.0
    >>> time_from_utc(-1, 23.0)
    22.0
    '''
    time_from = time + utc_offset
    return to_24_hour_clock(time_from)


