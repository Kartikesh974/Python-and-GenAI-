a = open("r1.log","w")
a.write("Sample data\n")
a.write("Product name is:pA Cost is:4565\n")
p_name = 'pB'
p_cost = 35523.23
a.write(f'Product name is:{p_name} Cost is:{p_cost}\n')
a.write('---------------------------------\n')
a.close()