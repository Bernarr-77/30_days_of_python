import pandas as pd

df = pd.read_csv("sample-1.csv")

df_filtrado = df[df["Priority"] == "High"]

print(df_filtrado)
print(f"Quantidade de itens High: {len(df_filtrado)}")