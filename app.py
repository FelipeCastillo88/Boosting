import pickle 
import streamlit as st 
import numpy as np

st.title("Modelo Boosting")

st.divider()

st.write("Ingrese los datos")

assess= st.slider("Assess",0,20)
bdrms= st.slider("Bdrms",0,50)
lotsize= st.slider("Lotsize",0,20)
sqrft= st.slider("sqrft",0, 10)
colonial=st.slider("colonial",0,1)

#with open ("model.pickle",'rb') as doc:
 #   model= pickle.load(doc)

#print (type(model))

#prediccion =modelo.predict(np.array([[assess, bdrms, lotsize, sqrft, colonial]]))
if st.button("Predecir:"):
    st.write(f"El precio es de {pediccion[0]}")