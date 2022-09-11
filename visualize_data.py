import pandas as pd
from utils import get_data, join_data_frames, plot_data, plot_time_series


def main():
    url_ipca: str = "https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/198001-202201/variaveis/63?localidades=BR"
    url_icea: str = "https://servicodados.ibge.gov.br/api/v3/agregados/2296/periodos/all/variaveis/1196?localidades=BR"

    df_ipca: pd.DataFrame = get_data(url_ipca, date_format="%Y%m")
    df_icea: pd.DataFrame = get_data(url_icea, date_format="%Y%m")
    df_all: pd.DataFrame = join_data_frames(first_df=df_ipca, second_df=df_icea,
                                        old_name="value", first_new_name="valor_ipca",
                                        second_new_name="custo")
    df_all[["valor_ipca", "custo"]] = df_all[["valor_ipca", "custo"]].astype(float)

    plot_time_series(df=df_all, x_name="date", y_name="valor_ipca",
                     xlabel='Tempo (mensal)', ylabel='IPCA', title='IPCA pelo tempo')
    plot_time_series(df=df_all[df_all["custo"].notna()], x_name="date", y_name="custo",
                     xlabel='Tempo (mensal)', ylabel='Variação custo médio de m²',
                     title='Custo médio de m²')
    plot_data(df=df_all.loc[df_all["custo"].notna()], x_name="valor_ipca",
              y_name="custo", title="IPCA pelo custo médio",xlabel="IPCA",
              ylabel="custo médio")

    # Antes de 1995
    plot_time_series(df=df_all.loc[df_all.date < "1995-01-01"], x_name="date",
                     y_name="custo", xlabel='Tempo (mensal)',
                     ylabel='Variação custo médio de m²',
                     title='Custo médio de m² antes de 1995')
    plot_data(df=df_all.loc[df_all.date < "1995-01-01"], x_name="valor_ipca",
              y_name="custo", title="IPCA pelo custo médio antes de 1995",
              xlabel="IPCA", ylabel="custo médio")

    # Depois de 1995
    plot_time_series(df=df_all.loc[df_all.date > "1995-01-01"], x_name="date",
                     y_name="custo", xlabel='Tempo (mensal)',
                     ylabel='Variação custo médio de m²',
                     title='Custo médio de m² depois de 1995')
    plot_data(df=df_all.loc[df_all.date > "1995-01-01"], x_name="valor_ipca",
              y_name="custo", title="IPCA pelo custo médio depois de 1995",
              xlabel="IPCA", ylabel="custo médio")


if __name__ == '__main__':
    main()
