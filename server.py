# importing pandas as pd
import pandas as pd
import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get('https://api.covid19india.org/state_district_wise.json')
data = response.json()
# print(data)
T_Confirmed, T_Active, T_Deceased, T_Recovered, Overall_Recovery_Rate = 0, 0, 0, 0, 0
District_List = []
Confirmed_List = []
Active_List = []
Recovered_List = []
Deceased_List = []
Recovery_Rate_List = []
for states in data:
    # print(states)
    for dist in data[states]['districtData'].items():
        # print(dist)
        print('District ' + dist[0] + ' from ' + states)
        District_List.append(dist[0])
        dist_data = list(dist[1].items())
        # print(dist_data)
        Confirmed = dist_data[2][1]
        print('Confirmed Cases: ' + str(dist_data[2][1]))
        Confirmed_List.append(Confirmed)
        Active = dist_data[1][1]
        print('Active Cases: ' + str(dist_data[1][1]))
        Active_List.append(Active)
        Recovered = dist_data[5][1]
        print('Recovered Cases: ' + str(dist_data[5][1]))
        Recovered_List.append(Recovered)
        Deceased = dist_data[4][1]
        print('Deceased Cases: ' + str(dist_data[4][1]))
        Deceased_List.append(Deceased)
        if Confirmed == 0:
            print('Recovery rate: 0')
            Recovery_Rate_List.append(0)
        else:
            Recovery_Rate = round(float(Recovered) / Confirmed * 100, 2)
            print('Recovery Rate: ' + str(Recovery_Rate) + '%')
            Recovery_Rate_List.append(str(Recovery_Rate) + '%')
        # print(District_List)
        # print(Confirmed_List)
        # print(Active_List)
        # print(Deceased_List)
        # print(Recovered_List)
        # print(Recovery_Rate_List)
        T_Confirmed = T_Confirmed + Confirmed
        T_Active = T_Active + Active
        T_Deceased = T_Deceased + Deceased
        T_Recovered = T_Recovered + Recovered
        if T_Confirmed == 0:
            Overall_Recovery_Rate = 0
            # print('Overall_Recovery_Rate: 0.00')
        else:
            Overall_Recovery_Rate = round(float(T_Recovered)/T_Confirmed*100, 2)

# Create the dataframe
df = pd.DataFrame({'District': District_List,
                   'Confirmed Cases': Confirmed_List,
                   'Active Cases': Active_List,
                   'Deceased Cases': Deceased_List,
                   'Recovered Cases': Recovered_List,
                   'Recovery Rate %': Recovery_Rate_List,})

# Print the dataframe
print(df)
total = ['{:,}'.format(T_Confirmed), '{:,}'.format(T_Active),
         '{:,}'.format(T_Recovered), '{:,}'.format(T_Deceased), Overall_Recovery_Rate]

df.to_excel('district_data.xlsx', index = False)


@app.route('/')
def index():
    return render_template('index.html', total=total, column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Patient ID", zip=zip)


if __name__ == "__main__":
    app.run(debug=True)
