def leap_year(year):
    if year % 4 == 0 :
      if year % 100 == 0:
        if year %  400 == 0:
          print("leap year")
        else:
          print("not leap year")
      else:
        print("leap year")
    else:
      print("not a leap")    
#leap_year(2008)
def days_in_month(year,month):
   if month > 12 or month < 1:
    return "invalid month" 
   month_days=[31,28,30,31,30,31,31,30,29,31,30] 
   if leap_year(year) and month == 2 :
                                                       return 29 
    """it is a days_month function"""                                                   
   return month_days[month-1] 
year=int(input("Enter a year")) 
month=int(input("Enter a month"))
days= days_in_month(year,month)    
print(days)