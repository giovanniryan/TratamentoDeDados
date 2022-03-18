#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import seaborn as srn
import statistics as sts


# In[4]:


# importar tabela
dataset = pd.read_csv("Churn.csv", sep=";")
# visualizar tabela
dataset.head()


# In[5]:


# tamanho (linhas,colunas) 
dataset.shape


# In[15]:


# dar nome as colunas
dataset.columns = ["Id", "Score", "Estado", "Genero", "Idade", "Patrimônio", "Saldo", "Produtos", "TemCartaoCred", "Ativo", "Salario", "Saiu"]


# In[16]:


# visualizar
dataset.head()


# In[10]:


# explorar dados categóricos
# estado 
agrupado = dataset.groupby(["Estado"]).size()
agrupado


# In[12]:


agrupado.plot.bar(color = "red")


# In[17]:


agrupado = dataset.groupby(["Genero"]).size()
agrupado


# In[18]:


agrupado.plot.bar(color = "blue")


# In[19]:


# explorar colunas numericas
# score
dataset["Score"].describe()


# In[20]:


srn.boxplot(dataset["Score"]).set_title("Score")


# In[24]:


srn.histplot(dataset["Score"]).set_title("Score")


# In[25]:


#idade
dataset["Idade"].describe()


# In[29]:


srn.histplot(dataset["Idade"]).set_title("Idade")


# In[31]:


srn.boxplot(dataset["Idade"]).set_title("Idade")


# In[33]:


# saldo
dataset["Saldo"].describe()


# In[35]:


srn.boxplot(dataset["Saldo"]).set_title("Saldo")


# In[37]:


srn.histplot(dataset["Saldo"]).set_title("Saldo")


# In[38]:


# salario
dataset["Salario"].describe()


# In[40]:


srn.histplot(dataset["Salario"]).set_title("Salario")


# In[41]:


srn.boxplot(dataset["Salario"]).set_title("Salario")


# In[67]:


# contamos valores NAN (valores nao prenchidos)
dataset.isnull().sum() #isnull = conta valores NAN e sum = soma eles


# In[43]:


dataset["Salario"].describe()


# In[46]:


# Conferir mediana de Salario
mediana = sts.median(dataset["Salario"])
mediana


# In[48]:


# preencher os NAN`s com a mediana
dataset["Salario"].fillna(mediana, inplace=True)
dataset["Salario"].isnull().sum()
    


# In[50]:


# genero = falta de padronizacao e NAN`s
agrupado = dataset.groupby(["Genero"]).size()
agrupado


# In[51]:


# total de NANS
dataset["Genero"].isnull().sum()


# In[53]:


# preenche NANS com moda
dataset["Genero"].fillna("Masculino", inplace=True)


# In[54]:


dataset["Genero"].isnull().sum() 


# In[65]:


# Padroniza (M -> Masculino; F, Fem -> Feminino
dataset.loc[dataset["Genero"] == "M", "Genero"] = "Masculino"
dataset.loc[dataset["Genero"].isin(["F", "Fem"]), "Genero"] = "Feminino"
# Visualizar resultado
agrupado = dataset.groupby(["Genero"]).size()
agrupado


# In[66]:


dataset["Idade"].describe()


# In[69]:


# visualizar registros
dataset.loc[(dataset["Idade"] < 0) | (dataset["Idade"] > 120)]


# In[73]:


# calcular mediana
mediana = sts.median(dataset["Idade"])
mediana 


# In[76]:


# substituir
dataset.loc[(dataset["Idade"] < 0) | (dataset["Idade"] > 120), "Idade"] = mediana
dataset.loc[(dataset["Idade"] < 0) | (dataset["Idade"] > 120)] 


# <h3> Dados duplicados </h3>

# In[85]:


# dados duplicados, unico dado que duplicado, seria prejudicativo seria o ID
dataset[dataset.duplicated(["Id"],keep=False)]


# In[89]:


# excluimos pelo id
dataset.drop_duplicates(subset="Id", keep="first", inplace=True)
# visualizamos
dataset[dataset.duplicated(["Id"],keep=False)]


# In[91]:


# estado fora do dominio
agrupado = dataset.groupby(["Estado"]).size()
agrupado


# In[101]:


# atribuimos a moda nos estados que nao existem ou nao participam do Dominio (SUL)
dataset.loc[dataset["Estado"].isin(["RP", "SP", "TD",]), "Estado"]= "RS"
# visualiza
agrupado


# In[102]:


# outliers no salario, vamos considerar 2 desvios padrao
desv = sts.stdev(dataset["Salario"])
desv


# In[107]:


# definir padrao como dois desvios padrao e checamos se algum atende o criterio

dataset.loc[dataset["Salario"] >= 2 * desv]


# In[109]:


# atualizar salarios para mediana
mediana = sts.median(dataset["Salario"])
mediana


# In[111]:


# atribuimos
dataset.loc[dataset["Salario"] >= 2 * desv, "Salario"] = mediana
# checamos se algum atende ao criterio
dataset.loc[dataset["Salario"] >= 2 * desv]


# In[112]:


dataset.head()


# In[114]:


dataset.shape


# In[ ]:




