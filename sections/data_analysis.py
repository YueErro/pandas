import os
import pandas as pd
import matplotlib.pyplot as plt

def readCSV(pPath, pUseCols=None, pNumRows=None, pDtype=None):
    try:
        return pd.read_csv(pPath, usecols=pUseCols, nrows=pNumRows, dtype=pDtype)
    except IOError:
        raise Exception(pPath + 'not found')

def createDF(pDict, pColOrder=None):
    return pd.DataFrame(pDict, columns=pColOrder)

def main():
    sectionPath = os.path.dirname( os.path.realpath(__file__) )
    dataPath = os.path.dirname(sectionPath) + "/data/"

    imdbData = readCSV(dataPath + 'imdb.csv')
    ufoData = readCSV(dataPath + 'ufo.csv')
    drinksData = readCSV(dataPath + 'drinks.csv')
    titanicData = readCSV(dataPath + 'titanic.csv')

    print("\nSelect by specific genre ( data.genre.isin() ):")
    print(imdbData[imdbData.genre.isin(['History', 'Fantasy', 'Family'])])
    print("\nGroup by to know some details from num type column:")
    print("( data.groupby( '<ColName>'.<NumTypeColName>.agg() ) )")
    print( imdbData.groupby('genre').duration.agg(['min', 'median', 'max', 'mean', 'count']) )
    print("\nFrequency appearance ( data.<ColName>.value_counts() ):")
    print( imdbData.genre.value_counts() )
    print("\nCount unique and it's names:")
    print("( data.<ColName>.unique(), nunique() )")
    print( imdbData.genre.unique() )
    print( imdbData.genre.nunique() )
    print("\nIterate by index and row ( data.iterrows() ):")
    for index, row in imdbData.head(3).iterrows():
        print(index, row.title)
    print("\nGet mean value of all the num type rows and columns( data.mean() ):")
    print("(axis=0 --> rows, axis=1 --> columns)")
    print( imdbData.mean(axis=0) )
    print("")
    print( imdbData.tail(3).mean(axis=1) )
    print("\nChange column data.dtypes ( data.<ColName>.astype() ):")
    print(imdbData.dtypes)
    imdbData.duration = imdbData.duration.astype(float)
    print("")
    print(imdbData.dtypes)
    print("\nHistogram plotted")
    imdbData.duration.plot(kind='hist')
    plt.show()
    print("Bar plotted")
    imdbData.genre.value_counts().plot(kind='bar')
    plt.show()

    print("\nCheck if null and count them:")
    print( "data.isnull(), plus .sum()" )
    print( ufoData.isnull().tail(3) )
    print(ufoData.isnull().sum())
    print("\nSet index ( data.set_index('<ColName>', inplace=True) ):")
    ufoData.set_index('City', inplace=True)
    print( ufoData.head(3) )
    print("\nSelect specific values (data.loc['<CellValue/Index>', '<ColName2>']):")
    print(ufoData.loc['Ithaca', 'Colors Reported'])
    print("\n( data.reset_index(inplace=True) )")
    ufoData.reset_index(inplace=True)
    print("\nRandom sampling ( data.sample() ):")
    print( ufoData.sample(3) )
    print("\nConvert to datetime ( pd.to_datetime(data.<ColName>) ):")
    print(ufoData.dtypes)
    ufoData.Time = pd.to_datetime(ufoData.Time)
    print("")
    print(ufoData.dtypes)
    print("")
    print( ufoData.head(1) )

    print("\nSplitted and total memory space:")
    print("( data.memory_usage(deep=True), plus .sum() )")
    print( drinksData.memory_usage(deep=True) )
    print( "Total: ", drinksData.memory_usage(deep=True).sum() )
    print("\nReduce space ( astype('category') ):")
    drinksData.continent = drinksData.continent.astype('category')
    print( drinksData.memory_usage(deep=True) )
    print("\nChange display row options ( pd.set_option('display.max_rows', <NumRows>) ):")
    print("(Use 'display.max_colwidth' for columns)")
    print(pd.get_option('display.max_rows'), "rows by default")
    pd.set_option('display.max_rows', 2)
    print(drinksData)
    pd.reset_option('display.max_rows')
    print(drinksData)
    print("Set to " + str( pd.get_option('display.max_rows') ) + " rows.")


    print("\nCreate Data Frame with dict:")
    print("pd.DataFrame({'<ColName1>':[<Val1>], '<ColName2>':[<Val1>]}, columns=[<ColOrder>]) ")
    dict = {
        'id': [      0,       1,      2,       1,     0,     2],
        'name': ['Yue', 'Leire', 'Erro', 'Leire', 'yue', 'Yue']
    }
    colOrder = ['id', 'name']
    newDictDF = createDF(dict, colOrder)
    print(newDictDF)
    print("\nDrop duplicates ( data.drop_duplicates(keep=False, inplace=True) ):")
    print( newDictDF.drop_duplicates(keep=False) )
    print("\nCreate Data Frame with list of list:")
    print("pd.DataFrame([[<Val1Col1>,<Val1Col2>],[<Val2Col1>,<Val2Col2>]], columns=[<ColOrder>]) ")
    listOflist = [[0, 'Yue'], [1, 'Erro']]
    newListsDF = createDF(listOflist, colOrder)
    print(newListsDF)

    print("\nNew column according to an existing column:")
    print("( data.<ColName>.map({'<CellValue>':<NewCelValue>}) )")
    titanicData['Male'] = titanicData.Sex.map({'male':True, 'female':False})
    print( titanicData.head(2) )
    print("\nBinary table with unique values:")
    print("( pd.get_dummies(data.<ColName>) )")
    embarkedBT = pd.get_dummies(titanicData.Embarked)
    print( embarkedBT.head(2) )
    print("\nAdd concatenate data to a data ( pd.concat([data, newData], axis=1)")
    print( pd.concat([titanicData, embarkedBT], axis=1).tail(5) )

if __name__ == '__main__':
    main()
