import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/family/Desktop/Division_Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
# departments = df['Dept'].unique()
scheduling_df = pd.DataFrame()

class Dataframe():

    def __init__(self, df):
        self.df = df



    def data_cleanup(self):
        self.df = self.df[self.df['Start'].notna()].reset_index()
        # print(self.df)

        for i in range(len(self.df)):
            item = str(self.df.loc[i, 'Start'])

            if "am" in item:
                if len(item) > 6:
                    item2 = item[:5]
                    no_colon = item2.replace(':', '')
                    self.df.loc[i, 'Start'] = int(no_colon)
                else:
                    item2 = item[:4]
                    no_colon = item2.replace(':', '')
                    self.df.loc[i, 'Start'] = int(no_colon)
            else:
                if len(item) > 6:
                    item2 = item[:5]
                    no_colon = item2.replace(':', '')
                    number_time = int(no_colon)
                    if number_time >= 1200:
                        self.df.loc[i, 'Start'] = int(no_colon)
                    else:
                        military_time = number_time + 1200
                        self.df.loc[i, 'Start'] = int(military_time)

                else:
                    item2 = item[:4]
                    no_colon = item2.replace(':', '')
                    number_time = int(no_colon)
                    military_time = number_time + 1200
                    self.df.loc[i, 'Start'] = int(military_time)
        return self.df

    def get_times(self):
        times = self.df['Start'].unique()
        timesList = times.tolist()
        timesList.sort()
        return timesList

    def ordered_list_of_days(self, day0, day1):
        M = []
        Tu = []
        W = []
        Th = []
        F = []
        Sa = []
        days_dict = {}
        days_dict[day0] == day1
        # day0.replace("'", "")
        print(days_dict)



    def get_days(self):
        m = []
        tu = []
        w = []
        th = []
        f = []
        sa = []
        all_days = []
        days_column_list = []
        days = self.df['Days'].unique()
        days_list = [day.replace('\xa0', '') for day  in days ]
        print(days_list)
        for day in days_list:
            if 'M' in day[0]:
                # Dataframe.ordered_list_of_days(self, day[0], day)
                m.append(day)
                m.sort()
                print('m', m)
            elif 'Tu' in day:
                tu.append(day)
                tu.sort()
                print('t', tu)
            elif 'W' in day[0]:
                w.append(day)
                w.sort()
                print('w', w)
            elif 'Th' in day[0:]:
                th.append(day)
                th.sort()
                print('th', th)
            elif 'F'in day[0]:
                f.append(day)
                f.sort()
            elif 'Sa'in day[0]:
                sa.append(day)
                sa.sort()
        all_days.append(m)
        all_days.append(tu)
        all_days.append(w)
        all_days.append(th)
        all_days.append(f)
        all_days.append(sa)
        print(all_days)
        for i in range(len(all_days)):
            if len(all_days[i]) > 0:
                for j in range(len(all_days[i])):
                    for item in all_days[i]:
                        if item not in days_column_list:
                            days_column_list.append(item)
        print('column', days_column_list)

        # print(days_list)
        # print('sorted', sorted)
        return days_column_list


class FillingDataframe:

    def __init__(self, df, times, days):
        self.df = df
        self.times = times
        self.days = days

    def count_sections(self):
        scheduling_df = pd.DataFrame(columns=self.times,index=self.days)
        for day in self.days:
            for time in self.times:
                section_count = 0
                for i in range(len(self.df) - 1):
                    if (df.loc[i, 'Days'] == day) & (df.loc[i, 'Start'] == time):
                        section_count += 1
                scheduling_df.loc[day, time] = section_count
        print(scheduling_df)

d = Dataframe(df)
df = d.data_cleanup()
time_list = d.get_times()
# print(time_list)
days_list = d.get_days()
# print(days_list)
f = FillingDataframe(df=df, times=time_list, days=days_list)
f.count_sections()




# for department in departments:
#     dept = df[df['Dept'] == department]
#     # print(dept)
#
# days = df['Days'].unique()
# # print(days)
# count = 0
# for day in days:
#      dy = df[df['Days']==day]
#      startTimes = dy['Start'].unique()
#      # print(startTimes)
#      for start in startTimes:
#         time_df = dy[dy['Start']==start]
#         print(f'{day} has {len(time_df.index)} sections at {start}')
#         count = count + 1