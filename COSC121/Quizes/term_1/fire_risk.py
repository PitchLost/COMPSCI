def fire_risk(temp, rainless_days):
    '''
    Write a function fire_risk(temperature, rainless_days) that takes two positive numeric 
    arguments into parameters rainless_days and temperature and returns a string 
    Low, Medium, or High according to the table: 

    Temp less than 25 and rainless days under 28: Low
    Temp less than 25 and rainless days over 28: medium
    Temp 25 or more and rainless days under 28: medium
    Temp 25 or more and rainless days over 28: high
    '''
    if temp < 25.0:
        if rainless_days < 28.0: 
            return 'Low'
        if rainless_days >= 28.0: 
            return 'Medium'
    elif temp >= 25.0:
        if rainless_days < 28.0: 
            return 'Medium'
        if rainless_days >= 28.0: 
            return 'High'
