import os
import data_analysis
import numpy as np
import pandas as pd

def readExcel(pPath):
    try:
        return pd.read_excel(pPath)
    except IOError:
        raise Exception(pPath + 'not found')

def main():
    listCitiesRegions = [['Vitoria-Gasteiz', 'Basque Country'], ['Barcelona', 'Catalonia'], ['Santander', 'Cantabria']]
    dfCR = data_analysis.createDF(listCitiesRegions, ['City', 'Region'])

    listCitiesLanguages = [['Vitoria-Gasteiz', 'Basque'], ['Barcelona', 'Catalan'], ['Santander', 'Spanish']]
    dfCL = data_analysis.createDF(listCitiesLanguages, ['City', 'Language'])

    daysDict = {
        'Days':        ['Sat', 'Sun'],
        'Temperature': [   25,    26],
        'Humidity':    [   25,    26],
        'Wind':        [   19,    18],
        'Rain':        ['Yes',  'No']
    }
    dfWeather = data_analysis.createDF(daysDict)

    scoreDict = {
        'FirstScore':  [100,     90, np.nan, 95],
        'SecondScore': [ 30, np.nan,     56, 45]
    }
    dfScore = data_analysis.createDF(scoreDict)

    sectionPath = os.path.dirname( os.path.realpath(__file__) )
    dataPath = os.path.dirname(sectionPath) + "/data/"
    titanicData = data_analysis.readCSV(dataPath + 'titanic.csv')

    weatherData = readExcel(dataPath + 'weather.xlsx')

    print("\nMake inner join with City column:")
    print("pd.merge(data1, data2, how='inner', on='City')")
    print( pd.merge(dfCR, dfCL, how='inner', on='City') )

    print("\nMelt:")
    print(dfWeather)
    print("")
    print( pd.melt(dfWeather, id_vars='Days', var_name='Metric', value_name='ºC') )
    print("\nReshape the data:")
    print("( data.pivot(index=<ColName1>, columns=<ColName2>, values=<SpecificColNames>) )")
    print("(Do not use values to display all)")
    print("(Use pivot_table() if index is not unique)")
    print( dfWeather.pivot(index='Days', columns='Rain') )
    dfWeather.to_csv(dataPath + 'weather.csv', index=False)
    print("\nData frame saved as csv file ( data.to_csv(pPath, index=False) ).")
    dfWeather.to_excel(dataPath + 'weather.xlsx', sheet_name='Weather', index=False)
    print("\nData frame saved as excel (.xlsx) file.")
    print("( data.to_excel(pPath, sheet_name='<Name>', index=False) )")

    print("\nStack/Unstack ( data.stack() or .unstack() ):")
    print( weatherData.stack().unstack() )
    print("")
    print( weatherData.stack() )

    with pd.ExcelWriter(dataPath + 'score.xlsx') as writer:
        dfScore.to_excel(writer, sheet_name='Score', index=False)
    print("\nWritten into excel file with writer.")
    print("(pd.ExcelWriter(pPath) as writer:)")
    print("     ( data.to_excel(writer, sheet_name='<Name>', index=False) )")
    print("\nReplace NaN values ( data.fillna(<Value>) ):")
    print("or: ( data.fillna({'<ColName1>':<Val1>, '<ColName2>':<Val2>}) )")
    print(dfScore)
    print("")
    print( dfScore.fillna({'FirstScore':'NULL1', 'SecondScore':'NULL2'}) )
    print("\nFill NaN value with the previous value (ffill) or next value (bfill):")
    print("( data.fillna(method='ffill') )")
    print("(limit=1 --> Only the first NaN value in a chain)")
    print( dfScore.fillna(method='ffill') )
    print("")
    print( dfScore.fillna(method='bfill') )
    print("\nInterpolate NaN values:")
    print( dfScore.interpolate() )

    print("\nFrequency of appearance of a column (ColName2) according to another column (ColName1):")
    print("pdcrosstab(data.<ColName1>, data.<ColName2>)")
    print("(margins=True --> Shows the sum in each row and column)")
    print("(normalize=True --> Gives the percentage)")
    print( pd.crosstab(titanicData.Pclass, titanicData.Survived, margins=True, normalize=True) )

if __name__ == '__main__':
    main()
