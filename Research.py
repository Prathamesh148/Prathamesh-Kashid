import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt                 
import seaborn as sns                       
import sys
import warnings                                  
warnings.filterwarnings('ignore')  
#---------------------------------------------------------------------------------------------------
st.title('Automating Machine Learning Task')
st.markdown('Note: Application is under-development code will updated once completed @Prathamesh_Kashid :sunglasses:')
#---------------------------------------------------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload a file for analysis & leave evething to us!!! ",type=['csv','xlsx'])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully & File type is CSV !!!")
    except Exception:
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully & File type is Excel !!!")
#---------------------------------------------------------------------------------------------------------------------    
    click= st.checkbox("DO YOU WANT TO SEE UPLOADED FILE DATA ???")
    if click==True:
        st.dataframe(df)
#------------------------------------------------------------------------------------------------------------------------------------------
    click= st.checkbox("DO YOU WANT TO DO EDA - Exploratory Data Analysis ON UPLOADED FILE ???")
    if click==True:
        A=['Number of rows & columns in uploaded file','Describe uploaded file','Information of uploaded file','columns in uploaded file','corelation between columns of file','Pairplot of all columns of file']
        col=st.selectbox("Select what you want from drop down list:",A)
        if col=='Number of rows & columns in uploaded file':
            a=df.shape
            st.write('shape of dataframe:',a)
        elif col=='Describe uploaded file':
            st.write('Describing dataframe:')
            b=df.describe()
            st.dataframe(b)
        elif col=='Information of uploaded file':
            c=df.info
            st.write('Information of file:',c)
        elif col=='columns in uploaded file':
            d=df.columns
            st.write('Columns in file:',d)
        elif col=='corelation between columns of file':
            d=df.corr()
            st.dataframe(d)
            fig=sns.set(rc={"figure.figsize":(10, 10)})
            sns.heatmap(df.corr(),annot=True,cmap='coolwarm');
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(fig)
        elif col=='Pairplot of all columns of file':
            fig=sns.pairplot(df)
            st.pyplot(fig)

#---------------------------------------------------------------------------------------------------------------------------------------------            
    click= st.checkbox("DO YOU WANT TO SEE CLEANING & PREPROCESSING OF FILE ???")
    if click==True:    
        e=df.isnull().sum().sort_values(ascending=False)
        st.write('Checking null values in dataframe:',e)
        f=(df.isnull().sum()*100/df.isnull().count()).sort_values(ascending=False)
        st.write('Percentage of null values in dataframe:',f)
        
        
        
    
        
    
