import pandas as pd


def formating(df):
        """This function prepares the date column, it has to be used previous to the 
        function every_row. It removes undesired characters and whitespaces in the column."""
        df.reset_index(drop=True,inplace=True)
        df["Fecha"] = df["Fecha"].astype(str)
        df["Fecha"] = df["Fecha"].str.replace("00:00:00","")
        df["Fecha"] = df["Fecha"].str.strip()
        return df
def every_row(row):
        """This function changes the order of dates.
        Example: Changes YYYY-mm-dd to dd-mm-YYYY"""
        lista = row.split("-")
        lista_invertida = lista[::-1]
        new_row = "-".join(lista_invertida)
        return new_row

