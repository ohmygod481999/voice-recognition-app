import pandas as pd

def saveFileCsv(filename, detail, columns):
    # detail = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
    #         'Price': [22000,25000,27000,35000]
    #         }
    df = pd.DataFrame(detail, columns= columns)
    df.to_csv (f'csv_file/{filename}', index = True, header=True)
    print("success")
