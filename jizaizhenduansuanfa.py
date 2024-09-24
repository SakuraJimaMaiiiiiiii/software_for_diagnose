
import pandas as pd


class jizaizhenduan():
    def __init__(self):
        self.df = None
        self.new_columns = ['time', 'atmospheric_pressure', 'altitude', 'cockpit_pressure', 'cockpit_residual_pressure',
                            'total_flow', 'chamber_pressure', 'pressure_rate_of_change',
                            'residual_pressure_rate_of_change', 'chamber_pressure_rate_of_change']
        self.conditions = {}
        self.fault_conditions = {}
        self.potential_fault_conditions = {}
        self.fault_locations = {}

    def preprocess_data(self, file_path):
        self.df = pd.read_excel(file_path)
        self.df.columns = self.new_columns[:7]  # 假设原始表格有7列
        self.df['pressure_rate_of_change'] = self.df['cockpit_pressure'].diff() / self.df['time'].diff()
        self.df['residual_pressure_rate_of_change'] = self.df['cockpit_residual_pressure'].diff() / self.df[
            'time'].diff()
        self.df['chamber_pressure_rate_of_change'] = self.df['chamber_pressure'].diff() / self.df['time'].diff()
        self.df.fillna(0, inplace=True)

    def define_conditions(self):
        self.conditions = {
            'var_pressure_high1': self.df['cockpit_pressure'] >= 76.9178522620902,
            'var_pressure_low1': self.df['cockpit_pressure'] <= 72.59494018,
            'var_pressure_low4': self.df['cockpit_pressure'] <= 65,
            'var_pressure_low5': self.df['cockpit_pressure'] <= 40.0857960325781,
            'var_pressure_low6': self.df['cockpit_pressure'] >= 38.2165644250258,
            'var_pressure_high2': self.df['cockpit_residual_pressure'] >= 4.77311684196114,
            'var_pressure_low2': self.df['cockpit_residual_pressure'] <= -4.36430860862337,
            'var_pressure_high3': self.df['cockpit_residual_pressure'] >= 37.1443939413015,
            'var_pressure_low3': self.df['cockpit_residual_pressure'] <= 33.92158432,
            'var_residual_high': self.df['cockpit_residual_pressure'] > 40,
            'var_residual_low': self.df['cockpit_residual_pressure'] < 14.2297,
            'var_up_overrun': self.df['chamber_pressure_rate_of_change'] > 0.600124213,
            'var_down_overrun': self.df['pressure_rate_of_change'] < -1.10371071804501,
            'var_rate_up': self.df['pressure_rate_of_change'] > 0,
            'var_rate1': self.df['chamber_pressure_rate_of_change'] > 0.5958692824003029,
            'var_rate2': self.df['chamber_pressure_rate_of_change'] < 0.23549604840719752,
            'var_residual_pressure_rate_of_change': self.df['residual_pressure_rate_of_change'] > 0.68563,
            'var_nomal_pressure': self.df['atmospheric_pressure'] > 75.3,
            'var_residual_pressure': self.df['atmospheric_pressure'] < 40.8,
            'var_altitude_low': self.df['altitude'] <= 2750.430961,
            'var_altitude_high': self.df['altitude'] >= 6856.847664,
            'var_altitude_toohigh': self.df['altitude'] >= 11849.2870252768,
            'var_chamber1': self.df['chamber_pressure'] > 75.57516989,
            'var_chamber2': self.df['chamber_pressure'] < 71.4763658986152,
            'var_chamber_rate': self.df['chamber_pressure_rate_of_change'] < 0.01,
            'var_gas_flow_high': self.df['total_flow'] > 652.2815,
            'var_gas_flow_low': self.df['total_flow'] < 243.444
        }

        for var_name, condition in self.conditions.items():
            self.df[var_name] = condition.astype(int)

    def define_fault_conditions(self):
        self.fault_conditions = {
            'pressure_regulating_system_faulty': (
                                                         (
                                                                 ((~self.df['var_altitude_low']) & (
                                                                     ~self.df['var_altitude_high']) &
                                                                  self.df['var_pressure_low1']) |
                                                                 (self.df['var_altitude_low'] & self.df[
                                                                     'var_pressure_low2']) |
                                                                 (self.df['var_altitude_high'] & self.df[
                                                                     'var_pressure_low3'])
                                                         ) &
                                                         (
                                                                 self.df['var_rate1'] | self.df['var_rate2']
                                                         )
                                                 ) |
                                                 (
                                                         ((~self.df['var_altitude_low']) & (
                                                             ~self.df['var_altitude_high']) & self.df[
                                                              'var_pressure_high1']) |
                                                         (self.df['var_altitude_low'] & self.df['var_pressure_high2']) |
                                                         (self.df['var_altitude_high'] & self.df['var_pressure_high3'])
                                                 ),
            'cockpit_compromise': (
                    self.df['var_altitude_high'] & self.df['var_residual_low']
            ),
            'air_leakage_out_of_tolerance': (
                    ((~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & self.df['var_pressure_low4']) &
                    (self.df['var_rate1'] | self.df['var_rate2'])
            ),
            'pressure_change_rate_exceed': (
                self.df['var_up_overrun'] & (~self.df['var_altitude_low'])
            ),
            'residual_pressure_superhigh': (
                self.df['var_residual_high']
            ),
            'pressure_fluctuates': (
                    (self.df['var_up_overrun'] & (((~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) &
                                                   self.df['var_pressure_low1']) |
                                                  (self.df['var_altitude_low'] & self.df['var_pressure_low2']) |
                                                  (self.df['var_altitude_high'] & self.df['var_pressure_low3']))) |
                    (self.df['var_down_overrun'] & (((~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) &
                                                     self.df['var_pressure_high1']) |
                                                    (self.df['var_altitude_low'] & self.df['var_pressure_high2']) |
                                                    (self.df['var_altitude_high'] & self.df['var_pressure_high3'])))
            ),
            'low_pressure': (
                    (((~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & self.df['var_pressure_low1']) |
                     (self.df['var_altitude_low'] & self.df['var_pressure_low2']) |
                     (self.df['var_altitude_high'] & self.df['var_pressure_low3'])) &
                    (self.df['var_rate1'] | self.df['var_rate2'])
            ),
            'high_pressure': (
                    ((~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & self.df['var_pressure_high1']) |
                    (self.df['var_altitude_low'] & self.df['var_pressure_high2']) |
                    (self.df['var_altitude_high'] & self.df['var_pressure_high3'])
            )
        }

        self.potential_fault_conditions = {
            'absolute_low': (~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & self.df[
                'var_pressure_low1'],
            'absolute_high': (~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & self.df[
                'var_pressure_high1'],
            'free_low': self.df['var_altitude_low'] & (self.df['var_pressure_low2'] & (~self.df['var_rate2'])),
            'free_high': self.df['var_altitude_low'] & self.df['var_pressure_high2'],
            'residual_low': self.df['var_altitude_high'] & self.df['var_pressure_low3'],
            'residual_high': self.df['var_altitude_high'] & self.df['var_pressure_high3'],
            'residual_downlow': self.df['var_altitude_high'] & self.df['var_pressure_low3'] & self.df['var_chamber_rate'],
            'chamber_unnomal': (
                    (~self.df['var_altitude_low']) &
                    (~self.df['var_altitude_high']) &
                    (self.df['var_chamber1'] | self.df['var_chamber2']) &
                    (self.df['var_chamber_rate'])
            ),
            'protection': self.df['var_altitude_toohigh'] & self.df['var_pressure_low5'] & self.df['var_pressure_low6'],
            'unprotection': self.df['var_altitude_toohigh'] & (~self.df['var_pressure_low6']),
            'absolute_nomal': (~self.df['var_altitude_low']) & (~self.df['var_altitude_high']) & (
                ~self.df['var_pressure_low1'].astype(bool)) & (~self.df['var_pressure_high1'].astype(bool))
        }

        for fault_name, fault_condition in self.fault_conditions.items():
            self.df[fault_name] = fault_condition.astype(int)

        for potential_fault_name, potential_fault_condition in self.potential_fault_conditions.items():
            self.df[potential_fault_name] = potential_fault_condition.astype(int)

    def define_fault_locations(self):
        self.fault_locations = {
            '绝压堵塞': ['pressure_regulating_system_faulty', 'high_pressure', 'absolute_high',
                     'chamber_unnomal'],
            '余压堵塞': ['pressure_regulating_system_faulty', 'residual_pressure_superhigh', 'high_pressure',
                     'residual_high'],
            '减震器堵塞': ['pressure_regulating_system_faulty', 'pressure_change_rate_exceed', 'low_pressure','absolute_nomal'],
            '高度保护堵塞': ['pressure_regulating_system_faulty', 'pressure_change_rate_exceed','residual_pressure_superhigh',
                           'high_pressure', 'free_high', 'absolute_high', 'residual_high'],
            '控制腔泄露到大气': ['pressure_regulating_system_faulty', 'cockpit_compromise',
                                   'air_leakage_out_of_tolerance', 'low_pressure', 'absolute_low', 'residual_low',
                                   'chamber_unnomal', 'unprotection'],
            '控制腔泄露到高保': ['pressure_regulating_system_faulty', 'cockpit_compromise',
                                   'air_leakage_out_of_tolerance', 'low_pressure', 'absolute_low', 'residual_low',
                                   'chamber_unnomal', 'protection'],
            '定径孔堵塞': ['pressure_regulating_system_faulty',  'low_pressure', 'residual_low','absolute_nomal'],
            '排气活门堵塞': ['pressure_regulating_system_faulty', 'residual_pressure_superhigh', 'high_pressure', 'free_high', 'absolute_high', 'residual_high'],
            '进气量不足': ['pressure_regulating_system_faulty', 'low_pressure', 'free_low', 'residual_low', 'absolute_nomal'],
            '进气量过多': ['pressure_regulating_system_faulty', 'high_pressure', 'free_high', 'absolute_high', 'residual_high','absolute_nomal'],
            '进气量波动': ['pressure_regulating_system_faulty', 'low_pressure', 'high_pressure'],
            '座舱泄露': ['pressure_regulating_system_faulty', 'low_pressure', 'absolute_low', 'residual_low','residual_downlow'],
        }

    def detect_faults(self):
        fault_timestamps = []
        detected_locations = []
        # 检查 pressure_regulating_system_faulty
        if not self.df['pressure_regulating_system_faulty'].any():
            detected_locations.append('正常')
            return detected_locations, fault_timestamps
        for location, location_conditions in self.fault_locations.items():
            all_conditions_met = all(self.df[condition].any() for condition in location_conditions)
            other_conditions_not_met = False
            if location == '绝压堵塞':
                other_conditions_not_met = self.df['residual_high'].any() or self.df['low_pressure'].any()
            elif location == '余压堵塞':
                other_conditions_not_met = self.df['free_high'].any() or self.df['absolute_high'].any() or self.df['low_pressure'].any()
            elif location == '定径孔堵塞':
                other_conditions_not_met = self.df['unprotection'].any() or self.df['protection'].any() or self.df['free_low'].any() or self.df['high_pressure'].any() or self.df['residual_downlow'].any()
            elif location == '排气活门堵塞':
                other_conditions_not_met = self.df['pressure_fluctuates'].any() or self.df['chamber_unnomal'].any() or self.df['absolute_nomal'].any()
            elif location == '进气量不足·':
                other_conditions_not_met = self.df['unprotection'].any() or self.df['protection'].any() or self.df[
                    'air_leakage_out_of_tolerance'].any() or self.df['pressure_change_rate_exceed'].any()
            elif location == '进气量过多':
                other_conditions_not_met = self.df['chamber_unnomal'].any()
            elif location == '座舱泄露':
                other_conditions_not_met = self.df['pressure_change_rate_exceed'].any()

            if all_conditions_met and not other_conditions_not_met:
                detected_locations.append(location)
                fault_timestamps.extend(self.df.loc[(self.df[location_conditions].sum(axis=1) == len(
                    location_conditions)), 'time'].tolist())
        if not detected_locations:
            if all_conditions_met and not other_conditions_not_met:
                detected_locations.append(location)
                fault_timestamps.extend(self.df.loc[(self.df[location_conditions].sum(axis=1) == len(
                    location_conditions)), 'time'].tolist())
        if not detected_locations:
            detected_locations.append('未知故障')
        return detected_locations, fault_timestamps

    def run(self, file_path):
        self.preprocess_data(file_path)
        self.define_conditions()
        self.define_fault_conditions()
        self.define_fault_locations()
        return self.detect_faults()


if __name__ == "__main__":
    locations, _ = jizaizhenduan().run(
        r'E:\files\项目\新乡\lpy_guzhangdata_excel\kongzhiqiang_xielou2daqi\newdata_1_0.3mm\67.xlsx')
    locations = str(locations)
    print(locations)
