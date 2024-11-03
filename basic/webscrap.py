from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep
from re import findall
from csv import DictWriter

driver=WebDriver()

def conver_to_number(some_string):
    return float("".join(findall("[\d\.]",some_string)))



driver.get("https://ticker.finology.in/market/index/nse/niftyjr")
sleep(2)
#all the company names from webpage
companies=driver.find_elements("xpath","//table[@id='companylist']//td[2]/a")
_companies=[company.text for company in companies]
print(_companies)
#for all share price
sleep(1)
prices=driver.find_elements("xpath","//table[@id='companylist']//td[3]")
_prices=[conver_to_number(price.text) for price in prices]
print(_prices)
#for the changes
sleep(1)
changes=driver.find_elements("xpath",f"//table[@id='companylist']//td[4]/span/span")
_change=[conver_to_number(f'{change.text}%') for change in changes]
print(_change)
#for mcap
sleep(1)
mcapes=driver.find_elements("xpath","//table[@id='companylist']//td[5]")
_mcapes=[conver_to_number(mcap.text )for mcap in mcapes]
print(_mcapes)

# for p/e
sleep(1)
pes=driver.find_elements("xpath","//table[@id='companylist']//td[6]")
_pes=[conver_to_number(pe.text) for pe in pes]
print(_pes)

#for pb
sleep(1)
pbs=driver.find_elements("xpath","//table[@id='companylist']//td[7]")
_pbs=[conver_to_number(pb.text)  for pb in pbs]
print(_pbs)

stokes=[]
for company,price,change,mcap,pe,pb in zip(_companies,_prices,_change,_mcapes,_pes,_pbs):
     d={"company":company,
       "price":price,
       "changes":change,
       "mcap":mcap,
        "pe":pe,
        "pb":pb,

       }
     stokes.append(d)
by_price=sorted(stokes,key=lambda item:item['price'])

print(by_price)

# print("*"*150)

# for company in by_price[:3]:
#      print(company)

# print("*"*150)

# for company in by_price[-3:]:
#      print(company)
# print("*"*150)

with open("stokes.csv","w")  as f:
     writer = DictWriter(f,fieldnames=['company',"price","changes","mcap",'pe',"pb"])
     writer.writeheader()
     # for stock in stokes:
     #      writer.writerow(stock)
     writer.writerows(stokes)






input()

