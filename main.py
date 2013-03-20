import sqlparse
from pprint import pprint
 
sqlparse.engine.grouping.print_process = True

def print_sql(sql):    
    show = lambda x: {x.__class__.__name__:[show(t) for t in x.tokens if not t.is_whitespace()]} if hasattr(x, 'tokens') else x
    
    parsed = sqlparse.parse(sql)
    print "******** final ********"
    pprint(show(parsed[0]))
    
#print_sql("INSERT INTO directories(inode)VALUES(:inode)LIMIT 1")

#print_sql("select * where avg(x+name-6)+name+4>4+4 AND y<8")
    
#print_sql("select a-5 where y+a-1<tester-8+b")
    
#print_sql("Select a Where func(money)>16")
#print_sql("Select a Where beauty+-16=levels")
#print_sql("Select a Where beauty--16=levels")
#print_sql("Select a Where beauty-16.2=levels")
#print_sql("Select a Where levels=beauty-16.2")
#print_sql("Select a Where beauty -16=levels")
print_sql("Select a Where levels=beauty +- 16")