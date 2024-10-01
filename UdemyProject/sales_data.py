countries =['USA','NEW YORK','CANADA','MEXICO','FRANCE','INDIA','CHINA']
sales = [2400,3300,4500,1200 ,3100,3200,3200]
sales_dict ={country: sale  for  country, sale in zip(countries ,sales)if sale >1000}
print(sales_dict)
