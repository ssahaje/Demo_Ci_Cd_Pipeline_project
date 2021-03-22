import requests
from flask import Flask, render_template

app = Flask(__name__)
response = requests.get('https://api.covid19india.org/state_district_wise.json')
data = response.json()
# print(data)
T_Confirmed, T_Active, T_Deceased, T_Recovered, Overall_Recovery_Rate = 0, 0, 0, 0, 0
District_Data = []
for states in data:
    # print(states)
    for dist in data[states]['districtData'].items():
        print(dist)
        print(f'District {dist[0]} from {states}')
        dist_data = list(dist[1].items())
        print(dist_data)
        Confirmed = dist_data[2][1]
        print(f'Confirmed Cases: {Confirmed}')
        Active = dist_data[1][1]
        print(f'Active Cases: {Active}')
        Recovered = dist_data[4][1]
        print(f'Recovered Cases: {Recovered}')
        Deceased = dist_data[3][1]
        print(f'Deceased Cases: {Deceased}')
        if Confirmed == 0:
            print('Recovery rate: 0')
        else:
            Recovery_Rate = round(float(Recovered) / Confirmed * 100, 2)
            print(f'Recovery Rate: {Recovery_Rate} %')

        District_Name = dist[0]
        T_Confirmed = T_Confirmed + Confirmed
        T_Active = T_Active + Active
        T_Deceased = T_Deceased + Deceased
        T_Recovered = T_Recovered + Recovered
        if T_Confirmed == 0:
            Overall_Recovery_Rate = 0
            # print('Overall_Recovery_Rate: 0.00')
        else:
            Overall_Recovery_Rate = round(float(T_Recovered) / T_Confirmed * 100, 2)

print(f'Total Cases: {T_Confirmed}, Active Cases: {T_Deceased}, Total Recovered: {T_Recovered}, '
      f'Total Deceased: {T_Deceased}, Overall Recovery Rate: {Overall_Recovery_Rate} %')

total = [T_Confirmed, T_Active, T_Recovered, T_Deceased, Overall_Recovery_Rate]
print(total)


@app.route('/')
def index():
    return render_template('index.html', total=total)


if __name__ == "__main__":
    app.run(debug=True)
