import urllib.request
import json
import pandas as pd


with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as response:

    if response.status == 200:

        print("Chamado Ok.")
        
        data = response.read()
        obj = json.loads(data)

        timestamp = obj['timestamp'] 
        latitude = obj['iss_position']['latitude']
        longitude = obj['iss_position']['longitude']

        df = pd.DataFrame({

            'Timestamp': [timestamp],
            'Latitude': [latitude],
            'Longitude' : [longitude]
        })

        print("Posição da ISS atualmente:")
        print(df.to_string(index=False))

    else:
        print("Erro na chamada: ", response.status)