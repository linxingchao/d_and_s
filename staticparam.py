def get_dlt_url(start,end): 
    return 'http://datachart.500.com/dlt/history/newinc/history.php?start=%s&end=%s' % (start,end)

def get_ssq_url(start,end): 
    return 'http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=%s' % (start,end)

def get_pls_url(start,end):
    return 'http://datachart.500.com/pls/history/newinc/history.php?start=%s&end=%s' % (start,end)