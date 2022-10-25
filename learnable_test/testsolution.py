

def nth_most_ratesignature(list,n):
    
    # empty dict to store array item as key and frequency as value
    frequency_count = {}
    
    for i in list:
        if i in frequency_count:
            frequency_count[i] += 1
        else:
            frequency_count[i] = 1
    
    #sorting dict values     
    sorted_frequency = sorted(frequency_count.items(), key= lambda x : x[1])
    
    #returns a pair of the requested rarest term as a tuple
    rarest_pair = sorted_frequency[n-1]
    
    #getting rarest item of the array
    rarest_item = rarest_pair[0]
    return rarest_item
    


print(nth_most_ratesignature([5,4,5,4,5,4,4,5,3,3,3,2,2,1,5], 2))
    