from datetime import datetime
import pandas as pd
from utils import get_data, join_data_frames, plot_data, plot_time_series


def main():

    month: int = datetime.now().month - 2
    year: int = datetime.now().year

    url_ipca: str = (f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4449/dados?'
                     f'formato=json&dataInicial=01/03/1999&dataFinal=01/{month:02}/'
                     f'{year}'
                    )
    url_icea: str = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4394/dados?' \
        'formato=json'

    df_ipca: pd.DataFrame = get_data(url_ipca)
    df_icea: pd.DataFrame = get_data(url_icea)
    df_all: pd.DataFrame = join_data_frames(first_df=df_ipca, second_df=df_icea,
                                        old_name="valor", first_new_name="valor_ipca",
                                        second_new_name="valor_icea")

    plot_time_series(df=df_all, x_name="data", y_name="valor_ipca", xlabel='Tempo (mensal)',
     ylabel='IPCA', title='IPCA pelo tempo')
    plot_time_series(df=df_all, x_name="data", y_name="valor_icea", xlabel='Tempo (mensal)',
     ylabel='Índice de Condicões Econômicas Atuais',
     title='Índice pelo tempo')
    plot_data(df=df_all, x_name="valor_ipca", y_name="valor_icea",
              title="IPCA pelo Índice", xlabel="IPCA", ylabel="Índice")


if __name__ == '__main__':
    main()
