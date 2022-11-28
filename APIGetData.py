
import requests
import json
from flask import Flask

response = requests.get("https://eflex-backend.azurewebsites.net/data/api/avgConsumption")
print(response.status_code)
print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())


pass_times = response.json()
jprint(pass_times)

#EANs = []
#for d in pass_times:
 #   time = d['features']
  #  EANs.append(time)

#print(EANs)
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0

Res = []

result_dict = {}


Rems1 = []
Rems2 = []
Rems3 = []
Rems4 = []
Rems5 = []
Rems6 = []
Rems7 = []
Rems8 = []
Rems9 = []
Rems10 = []
Rems11 = []
Rems12 = []



EAN1_Green = []
EAN1_Red = []


EAN2_Green = []
EAN2_Red = []


EAN3_Green = []
EAN3_Red = []


EAN4_Green = []
EAN4_Red = []

EAN5_Green = []
EAN5_Red = []

EAN6_Green = []
EAN6_Red = []

EAN7_Green = []
EAN7_Red = []

EAN8_Green = []
EAN8_Red = []

EAN9_Green = []
EAN9_Red = []

EAN10_Green = []
EAN10_Red = []

EAN11_Green = []
EAN11_Red = []

EAN12_Green = []
EAN12_Red = []




for f in pass_times:
    if f['Month'] == '1':
        month1 = 'January'
        consumption = f['Consumption']
        Rems1.append(float(consumption))
        count1 = count1 + 1
        avg_con1 = sum(Rems1)/count1
        if float(consumption) < avg_con1:
            EAN = f['EAN']
            EAN1_Green.append(EAN)
            Month = 'Jan'
            Meter = EAN
            Category = 'Green'
            Cost = 9.3
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con1:
            EAN = f['EAN']
            EAN1_Red.append(EAN)
            Month = 'Jan'
            Meter = EAN
            Category = 'Red'
            Cost = 11.4
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})

    if f['Month'] == '2':
        month2 = 'February'
        consumption = f['Consumption']
        Rems2.append(float(consumption))
        count2 = count2 + 1
        avg_con2 = sum(Rems2)/count2
        if float(consumption) < avg_con2:
            EAN = f['EAN']
            EAN2_Green.append(EAN)
            Month = 'Feb'
            Meter = EAN
            Category = 'Green'
            Cost = 13.4
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con2:
            EAN = f['EAN']
            EAN2_Red.append(EAN)
            Month = 'Feb'
            Meter = EAN
            Category = 'Red'
            Cost = 16.2
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '3':
        month3 = 'March'
        consumption = f['Consumption']
        Rems3.append(float(consumption))
        count3 = count3 + 1
        avg_con3 = sum(Rems3)/count3
        if float(consumption) < avg_con3:
            EAN = f['EAN']
            EAN3_Green.append(EAN)
            Month = 'March'
            Meter = EAN
            Category = 'Green'
            Cost = 9.2
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con3:
            EAN = f['EAN']
            EAN3_Red.append(EAN)
            Month = 'March'
            Meter = EAN
            Category = 'Red'
            Cost = 14.6
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '4':
        month4 = 'April'
        consumption = f['Consumption']
        Rems4.append(float(consumption))
        count4 = count4 + 1
        avg_con4 = sum(Rems4)/count4
        if float(consumption) < avg_con4:
            EAN = f['EAN']
            EAN4_Green.append(EAN)
            Month = 'April'
            Meter = EAN
            Category = 'Green'
            Cost = 12
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con4:
            EAN = f['EAN']
            EAN4_Red.append(EAN)
            Month = 'April'
            Meter = EAN
            Category = 'Red'
            Cost = 16.3
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '5':
        month5 = 'May'
        consumption = f['Consumption']
        Rems5.append(float(consumption))
        count5 = count5 + 1
        avg_con5 = sum(Rems5)/count5
        if float(consumption) < avg_con5:
            EAN = f['EAN']
            EAN5_Green.append(EAN)
            Month = 'May'
            Meter = EAN
            Category = 'Green'
            Cost = 13.5
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con5:
            EAN = f['EAN']
            EAN5_Red.append(EAN)
            Month = 'May'
            Meter = EAN
            Category = 'Red'
            Cost = 15.9
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '6':
        month6 = 'June'
        consumption = f['Consumption']
        Rems6.append(float(consumption))
        count6 = count6 + 1
        avg_con6 = sum(Rems6)/count6
        if float(consumption) < avg_con6:
            EAN = f['EAN']
            EAN6_Green.append(EAN)
            Month = 'June'
            Meter = EAN
            Category = 'Green'
            Cost = 12.1
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con6:
            EAN = f['EAN']
            EAN6_Red.append(EAN)
            Month = 'June'
            Meter = EAN
            Category = 'Red'
            Cost = 14.3
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '7':
        month7 = 'July'
        consumption = f['Consumption']
        Rems7.append(float(consumption))
        count7 = count7 + 1
        avg_con7 = sum(Rems7)/count7
        if float(consumption) < avg_con7:
            EAN = f['EAN']
            EAN7_Green.append(EAN)
            Month = 'July'
            Meter = EAN
            Category = 'Green'
            Cost = 14.2
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con7:
            EAN = f['EAN']
            EAN7_Red.append(EAN)
            Month = 'July'
            Meter = EAN
            Category = 'Red'
            Cost = 15.2
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '8':
        month8 = 'Aug'
        consumption = f['Consumption']
        Rems8.append(float(consumption))
        count8 = count8 + 1
        avg_con8 = sum(Rems8)/count8
        if float(consumption) < avg_con8:
            EAN = f['EAN']
            EAN8_Green.append(EAN)
            Month = 'August'
            Meter = EAN
            Category = 'Green'
            Cost = 8.6
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con8:
            EAN = f['EAN']
            EAN8_Red.append(EAN)
            Month = 'August'
            Meter = EAN
            Category = 'Red'
            Cost = 11.5
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '9':
        month9 = 'Sept'
        consumption = f['Consumption']
        Rems9.append(float(consumption))
        count9 = count9 + 1
        avg_con9 = sum(Rems9)/count9
        if float(consumption) < avg_con9:
            EAN = f['EAN']
            EAN9_Green.append(EAN)
            Month = 'Sept'
            Meter = EAN
            Category = 'Green'
            Cost = 9.3
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con9:
            EAN = f['EAN']
            EAN9_Red.append(EAN)
            Month = 'Sept'
            Meter = EAN
            Category = 'Red'
            Cost = 12.6
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '10':
        month10 = 'Oct'
        consumption = f['Consumption']
        Rems10.append(float(consumption))
        count10 = count10 + 1
        avg_con10 = sum(Rems10)/count10
        if float(consumption) < avg_con10:
            EAN = f['EAN']
            EAN10_Green.append(EAN)
            Month = 'Oct'
            Meter = EAN
            Category = 'Green'
            Cost = 10.4
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con10:
            EAN = f['EAN']
            EAN10_Red.append(EAN)
            Month = 'Oct'
            Meter = EAN
            Category = 'Red'
            Cost = 16.7
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '11':
        month11 = 'Nov'
        consumption = f['Consumption']
        Rems11.append(float(consumption))
        count11 = count11 + 1
        avg_con11 = sum(Rems11)/count11
        if float(consumption) < avg_con11:
            EAN = f['EAN']
            EAN11_Green.append(EAN)
            Month = 'Nov'
            Meter = EAN
            Category = 'Green'
            Cost = 13.4
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con11:
            EAN = f['EAN']
            EAN11_Red.append(EAN)
            Month = 'Nov'
            Meter = EAN
            Category = 'Red'
            Cost = 17.3
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
    if f['Month'] == '12':
        month12 = 'Dec'
        consumption = f['Consumption']
        Rems12.append(float(consumption))
        count12 = count12 + 1
        avg_con12 = sum(Rems12)/count12
        if float(consumption) < avg_con12:
            EAN = f['EAN']
            EAN12_Green.append(EAN)
            Month = 'Dec'
            Meter = EAN
            Category = 'Green'
            Cost = 14.2
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})
        elif float(consumption) > avg_con12:
            EAN = f['EAN']
            EAN12_Red.append(EAN)
            Month = 'Dec'
            Meter = EAN
            Category = 'Red'
            Cost = 16.7
            Res.append({"EAN": Meter, "Month": Month, "Category": Category, "Energy Saving": Cost})



print(Res)



print(Rems1)
print(Rems2)

print(EAN12_Green)
print(EAN12_Red)
print('The average consumption for {}: {}'.format(month1,avg_con1))
print('The average consumption for {}: {}'.format(month2,avg_con2))
print('The average consumption for {}: {}'.format(month3,avg_con3))
print('The average consumption for {}: {}'.format(month4,avg_con4))
print('The average consumption for {}: {}'.format(month5,avg_con5))
print('The average consumption for {}: {}'.format(month6,avg_con6))
print('The average consumption for {}: {}'.format(month7,avg_con7))
print('The average consumption for {}: {}'.format(month8,avg_con8))
print('The average consumption for {}: {}'.format(month9,avg_con9))
print('The average consumption for {}: {}'.format(month10,avg_con10))
print('The average consumption for {}: {}'.format(month11,avg_con11))
print('The average consumption for {}: {}'.format(month12,avg_con12))

print(Res)

app = Flask(__name__)
@app.route('/')
def hello_world():
    return str(Res)



if __name__ == '__main__':
    app.run()


#new = pass_times
#print(new)




