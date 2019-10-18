"""
File: marketModel.py
Author: Sam Bluestone and Zahin Reaz

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self.numCashiers = numCashiers
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._cashiers = [Cashier(x) for x in range(1, numCashiers + 1)]
        
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)
            
            # if successfully generated, send a customer to a cashier
            if customer != None:
                print("Cashiers:")
                for cashier in self._cashiers:
                    print(cashier.customersInLine())
            
                index = random.randint(0, len(self._cashiers) - 1)
                print("Random Index:", index)
                index = self.findShortestLine(index - 2, index + 2)
                print("Shortest Line:", index)
                self._cashiers[index].addCustomer(customer)

            # Tell all cashiers to provide another unit of service
            for cashier in self._cashiers:
                cashier.serveCustomers(currentTime)

    def findShortestLine(self, start, end):
        if start < 0:
            start = 0
        if end >= len(self._cashiers):
            end = len(self._cashiers) - 1
            
        minIndex = start
        minInLine = self._cashiers[start].customersInLine()
        for x in range(start + 1, end + 1):
            if min(minInLine, self._cashiers[x].customersInLine()) < minInLine:
                minInLine = self._cashiers[x].customersInLine()
                minIndex = x

        return minIndex
            

    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        retStr =  "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n"
        for x in range(len(self._cashiers)):
            retStr += str(self._cashiers[x]) + "\n"
                    

        return retStr
