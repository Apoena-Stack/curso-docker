import os
import urllib.request
import json
import pandas as pd


# Persistência de Dados
# Bind Mount

output_dir = "/app/data" # CONSIDERANDO FILESYSTEM DO CONTAINER 
output_file = os.path.join(output_dir, "iss_position.csv")


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

        df.to_csv(output_file, index=False)
        print(f"Dados escritos em: {output_file}")
        print(pd.read_csv(output_file))

    else:
        print("Erro na chamada: ", response.status)