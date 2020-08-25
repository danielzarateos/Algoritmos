import pandas as pd
mercado_uni= pd.Series({'Libra de solomito':16960,'leche':2400,'huevos':13000,'pan':13000,'gaseosa':3950,'lonchitas':12550,'jamon':8600,'libra de arroz ':8900,'mantequilla de mesa':7000,'mantequilla de barra':3000,})
print(mercado_uni)

mercado_bi_bien=pd.DataFrame({'enero':50000,'febrero':543523,'marzo':423423,'abril':213123},index=['Libra de solomito','leche','huevos','pan','gaseosa','lonchitas','jamon','libra de arroz','mantequilla de untar','mantequilla de barra'])
print(mercado_bi_bien)

print(mercado_bi_bien[['febrero','marzo']])

print(mercado_bi_bien['abril'])