#strike_outs = [70, 98, 120, 84]

#def multiply_by_two(x):
#    return x/2

#strike_out_values = map(multiply_by_two, strike_outs)
#strike_out_values = list(strike_out_values)

#map "maps" over a list and runs a function across said list. it returns a map object which is NOT iterable, but you can convert
#it to a list object to be able to be iterable. the below code is the same exact code with same output, just instead with a 
#lambda expression

strike_outs = [70, 98, 120, 84]

strike_out_values = map(lambda x: x/2, strike_outs)
strike_out_values = list(strike_out_values)
print(strike_out_values)


#the syntax for writing lambda functions is rather simple, it is just lambda argument: return_value, you just specify the arg
#then how you want to manipulate that specific argument


