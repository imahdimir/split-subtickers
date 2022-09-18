##

"""

    """

##

from pathlib import Path

import pandas as pd
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import read_data_according_to_type as reda
from mirutil.funcs import save_as_prq_wo_index as sprq
from mirutil.funcs import save_df_as_a_nice_xl as sxl


ipn = Path('inp.prq')  # dataset to split
btpn = Path('Unique Duo-Base Ticker-CompanyName.xlsx')  # all base tickers

tic = 'Ticker'
btic = 'BaseTicker'

def main() :


  pass

  ##
  df = reda(ipn)
  bdf = reda(btpn)

  ##
  df[tic] = df[tic].apply(norm)

  ##
  msk = df[tic].isin(bdf[btic])

  _df = df[msk]
  print(len(_df))

  _df[btic] = _df[tic]

  _df[tic] = _df[tic] + '1'

  _df = _df[
    ['JDate' , 'BaseTicker' , 'Ticker' , 'AdjOpen' , 'AdjHigh' , 'AdjLow' ,
     'AdjClose' , 'AdjLast' , 'CapitalAdjClose' , ]]

  sprq(_df , 'no.prq')

  df = df[~ msk]

  ##
  df['-1'] = df[tic].str[-1]
  df[btic] = df[tic].str[:-1]

  ##
  for k , nm in zip([2 , 3 , 4 , 'ح'] , [2 , 3 , 4 , 'h']) :
    msk = df['-1'].eq(str(k))
    msk &= df[btic].isin(bdf[btic])

    print(len(msk[msk]))

    _df = df[msk]

    _df = _df[
      ['JDate' , 'BaseTicker' , 'Ticker' , 'AdjOpen' , 'AdjHigh' , 'AdjLow' ,
       'AdjClose' , 'AdjLast' , 'CapitalAdjClose']]

    sprq(_df , f'{nm}.prq')

    df = df[~ msk]

  ##
  df['-2'] = df[tic].str[-2]
  df[btic] = df[tic].str[:-2]

  ##
  for k , nm in zip([2 , 3 , 4] , ['h2' , 'h3' , 'h4']) :
    msk = df['-1'].eq(str(k))
    msk &= df['-2'].eq('ح')
    msk &= df[btic].isin(bdf[btic])

    print(len(msk[msk]))

    _df = df[msk]

    _df = _df[
      ['JDate' , 'BaseTicker' , 'Ticker' , 'AdjOpen' , 'AdjHigh' , 'AdjLow' ,
       'AdjClose' , 'AdjLast' , 'CapitalAdjClose']]

    sprq(_df , f'{nm}.prq')

    df = df[~ msk]

  ##
  ptrn = r'اخزا' + r'.+'

  msk = df[tic].str.fullmatch(ptrn)
  msk = msk.fillna(False)

  _df = df[msk]
  _df[btic] = 'اخزا'

  _df = _df[
    ['JDate' , 'BaseTicker' , 'Ticker' , 'AdjOpen' , 'AdjHigh' , 'AdjLow' ,
     'AdjClose' , 'AdjLast' , 'CapitalAdjClose']]

  sprq(_df , 'akhza.prq')

  df = df[~ msk]

  ##
  # to be completed
  sprq(df , 'yet_cleaned.prq')

  ##

##


if __name__ == "__main__" :
  main()