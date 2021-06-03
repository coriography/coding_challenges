def is_speeding(list_data):
    
    # input at zero = first point
    # input 1 = second point
    
    # third item from second el of list minus
    # take third item from first element of list
    
    # divide all by
    # first item of second list minus
    # first item of first list
    
    # return whether the result of above is over 100 - true/false
    # + license plate
    
#     while list_data:
    
#         i_1, i_2 = list_data[0], list_data[1]

#         time_1, time_2 = i_1[2], i_2[2]
#         position_1, position_2 = i_1[0], i_2[0]

#         speed = (position_2 - position_1) / ((time_2 - time_1)/3600)

#         print([f'{i_1[1]}', speed > 100])
        
#         list_data.pop(0)
#         list_data.pop(0)

# create dict
# iterate through input
# check whether license plate in dict
# if not, add license plate as key
# add value position, time
# if already in dict
# calculate speed & print boolean & license

    license_lookup = {}

    for speed_data in list_data:
        p, l, t = speed_data
        if l not in license_lookup:
            license_lookup[l] = [p, t]
        else:
            # speed = (position_2 - position_1) / ((time_2 - time_1)/3600)
            speed = (p - license_lookup[l][0]) / ((t - license_lookup[l][1])/3600)
            print(l, speed > 100)
        

print(is_speeding([[1, "ABC-123", 1599066000], [2, "ABC-123", 1599066030], [1, "DEF-123",1599062378], [2, "DEF-123",1599062414], [1, "GHI-123",1599062435], [2, "GHI-123",1599062495], [1, "JKL-123",1599066000], [2, "JKL-123",1599066035]]))

# print(is_speeding([[2, "JKL-123",1599066035], [2, "ABC-123",1599066030], [1, "ABC-123",1599066000], [2, "DEF-123",1599062414], [1, "GHI-123",1599062435], [2, "GHI-123",1599062495], [1, "JKL-123",1599066000], [1, "DEF-123",1599062378]]))


# speed = Position2 - Position1 / time2 - Time1