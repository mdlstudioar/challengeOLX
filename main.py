"""Tenemos un archivo muy grande con documentos JSONL (que salió de un query de BigQuery),
en un URL.
● Hay que bajar el archivo (es un sample, el archivo real ocupa 50GB)
● Parsearlo

● Castear algunos de sus valores a tipos específicos (cuando BigQuery exporta como
JSONL, deja todos los valores como strings, pero en Firestore necesitamos el tipo de
dato correcto)
● Si no tenés, create una cuenta gratuita de Google Cloud Platform
● Subí estos documentos a una nueva colección de Firestore
La idea sería que en el futuro, este mismo código pueda usarse para OTROS URLs, que haya
que castear otros valores a otros tipos y subirlos a otras colecciones de Firestore.

URL del archivo: https://storage.googleapis.com/ejercicio-data-engineer-test-
data/sample_data.json
Campos a castear para almacenar en Firestore (en el JSONL están todos como strings)
● tracking_date: date
● seller_id: int
● counter1: int
● counter2: int"""

import pandas as pd
import ssl
from IPython.display import FileLink

ssl._create_default_https_context = ssl._create_unverified_context

f = pd.read_json("https://storage.googleapis.com/ejercicio-data-engineer-test-data/sample_data.json", lines=True)
# print(f)


def convert_types():
    """Al ser llamada, va a convertir los tipos de datos:
    object: en caso de que se pueda --> datetime
    float: en caso de que se pueda (parte flotante compuesta por 0/0s --> int
    """
    for i in f.columns:
        # print(f[i].dtype)
        if f[i].dtype == "object":  # str
            try:
                # lleno fechas vacías con 00-00-00 y convierto a fecha si se puede
                f[i].fillna("00-00-00", inplace=True)
                f[i] = pd.to_datetime(f[i])
            except:
                pass
        elif f[i].dtype == "float64":
            try:
                if (f[i] < 0).sum() == 0:  # son counters así que para distinguir usé - 1
                    f[i].fillna(-1, inplace=True)
                elif (f[i] < -999).sum() == 0:  # en el caso de que no sean counters
                    f[i].fillna(-1000, inplace=True)
                else:
                    f[i].fillna(round(f[i].mean(), ndigits=0))  # round == 0 digits para que se puede luego conv a int
                    # disclaimer: puse como últ opción porque considero mejor los anteriores para luego hacer análisis
                f[i] = f[i].astype(int)
            except:
                pass


# print(f.dtypes)
if __name__ == "__main__":
    convert_types()
    f.to_json("sample_typesok.json", orient="table")  # convierto el file con las modificaciones a json
    FileLink("sample_typesok.json")  # guardo el json utilizado en un archivo json que quede en el dir de programa












