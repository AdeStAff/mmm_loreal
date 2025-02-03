import pandas as pd 

def merge(metric= 'investment (in pound)'):
    df_ap_variables = pd.read_csv('../data/A&P_Variables.csv')
    df_commercial_variables = pd.read_csv('../data/Commercial_Variables.csv')
    df_kpi = pd.read_csv('../data/KPI_to_model.csv')

    media_levers = ['growth_driver_l1', 'growth_driver_l2', 'growth_driver_l3', 'growth_driver_l4', 'growth_driver_l5', 'metric']
    df_ap_variables['media_lever_combination'] = df_ap_variables[media_levers].apply(lambda x: ' | '.join(x), axis=1)

    df = df_ap_variables.pivot_table(index='Starting week', columns='media_lever_combination', values=metric)
    df.columns.name = None 
    df.index.name = None
    df.fillna(0, inplace=True)

    df_commercial_variables.set_index('Starting Week', inplace=True)
    df_commercial_variables.drop(columns=['Year'], inplace=True)
    df = df.join(df_commercial_variables, how='left')

    df_kpi.set_index('Starting Week', inplace=True)
    df_kpi.drop(columns=['Year'], inplace=True)
    df = df.join(df_kpi, how='left')

    return df

df_invest = merge('investment (in pound)')
df_execution = merge('execution')
df_invest.to_csv('../data/Final_df_investment.csv', index=True)
df_execution.to_csv('../data/Final_df_excution.csv', index=True)

# Pour download the df
# df_invest = pd.read_csv('../data/Final_df_investment.csv', index_col=0)
