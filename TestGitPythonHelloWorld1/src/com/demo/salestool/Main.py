'''
Created on Dec 8, 2018

@author: fleth
'''
from com.demo.salestool.SalesData import SalesData

class Main (object):
    '''
    classdocs
    '''
 
    def __init__(self):
        salesData = SalesData
        '''
        Constructor
        '''
        
   
   
    def displayGreeting(self): 
        print("Hello Happy SalsePeople")
        print("This app shows sales data")
        
        
        
        
    def execute(self):
        self.displayGreeting()
        print("hello world")
        
        
if __name__ == '__main__':
    main = Main()
    main.execute()
    pass