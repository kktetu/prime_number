class PrimeNumber(object):
    def is_prime_number(self, x):
        
        if x%2 == 0 and x != 2:
            #TODO スピード2倍になる
            return False

        return self._is_prime_number_two(x) #TODO さらに早くなる
        #return self._is_prime_number_one(x)
        
    
    def _is_prime_number_one(self, x):
        return 0 is not [x%y for y in range(2, x)]

    def _is_prime_number_two(self, x):
        
        for y in range(2, x):
            if x%y == 0:
                return False

        return True
