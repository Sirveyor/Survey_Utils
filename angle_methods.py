def dms_to_decimal(dms):
    degrees = int(dms)
    minutes = int((dms * 100) % 100)
    seconds = int((dms * 10000) % 100)
    return degrees + minutes / 60 + seconds / 3600

def decimal_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    return str(degrees) + 'º' + str(minutes).zfill(2) + "'" + str(seconds).zfill(2) + '"' 
    #return degrees, minutes, seconds

def degrees_to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def radians_to_degrees(radians):
    import math
    return radians * (180 / math.pi)
