from geobr.utils import test_options
import pandas as pd
import geobr


def read_capitals(as_sf=True, show_progress=True):
    """
    Download data of state capitals.

    Parameters
    ----------
    as_sf : bool, optional
        Whether to return spatial data as an `sf`-like (GeoDataFrame) object or as a simple
        `DataFrame`, by default True
    show_progress : bool, optional
        Display progress bar, by default True

    Returns
    -------
    pd.DataFrame or gpd.GeoDataFrame
        A `DataFrame` with names and codes of state capitals or a GeoDataFrame with spatial data.

    Raises
    ------
    Exception
        If parameters are not of the appropriate type
    """

    # Check input
    test_options(as_sf, "as_sf", allowed=[True, False])
    test_options(show_progress, "show_progress", allowed=[True, False])

    # Base DataFrame of capitals
    df = pd.DataFrame(
        {
            "name_muni": [
                "São Paulo",
                "Rio de Janeiro",
                "Belo Horizonte",
                "Salvador",
                "Fortaleza",
                "Vitória",
                "Goiânia",
                "Cuiabá",
                "São Luís",
                "Teresina",
                "Recife",
                "Aracaju",
                "João Pessoa",
                "Natal",
                "Maceió",
                "Porto Alegre",
                "Curitiba",
                "Florianópolis",
                "Belém",
                "Manaus",
                "Palmas",
                "Campo Grande",
                "Macapá",
                "Rio Branco",
                "Boa Vista",
                "Brasília",
                "Porto Velho",
            ],
            "code_muni": [
                3550308,
                3304557,
                3106200,
                2927408,
                2304400,
                3205309,
                5208707,
                5103403,
                2111300,
                2211001,
                2611606,
                2800308,
                2507507,
                2408102,
                2704302,
                4314902,
                4106902,
                4205407,
                1501402,
                1302603,
                1721000,
                5002704,
                1600303,
                1200401,
                1400100,
                5300108,
                1100205,
            ],
            "name_state": [
                "São Paulo",
                "Rio de Janeiro",
                "Minas Gerais",
                "Bahia",
                "Ceará",
                "Espírito Santo",
                "Goiás",
                "Mato Grosso",
                "Maranhão",
                "Piauí",
                "Pernambuco",
                "Sergipe",
                "Paraíba",
                "Rio Grande do Norte",
                "Alagoas",
                "Rio Grande do Sul",
                "Paraná",
                "Santa Catarina",
                "Pará",
                "Amazonas",
                "Tocantins",
                "Mato Grosso do Sul",
                "Amapá",
                "Acre",
                "Roraima",
                "Distrito Federal",
                "Rondônia",
            ],
            "code_state": [
                35,
                33,
                31,
                29,
                23,
                32,
                52,
                51,
                21,
                22,
                26,
                28,
                25,
                24,
                27,
                43,
                41,
                42,
                15,
                13,
                17,
                50,
                16,
                12,
                14,
                53,
                11,
            ],
        }
    )

    df = df.sort_values(by="code_muni", ascending=True)

    # Determine output format
    if not as_sf:
        return df

    # If as_sf is True, get spatial data
    temp_sf = geobr.read_municipal_seat(show_progress=show_progress)
    temp_sf = temp_sf[temp_sf["code_muni"].isin(df["code_muni"])]
    temp_sf.reset_index(drop=True, inplace=True)

    return temp_sf
