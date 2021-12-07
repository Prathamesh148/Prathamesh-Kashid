import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt                 
import seaborn as sns                       
import sys
import warnings                                  
warnings.filterwarnings('ignore')  
#---------------------------------------------------------------------------------------------------
st.title('Research Paper By Prathamesh Kashid')
#--------------------------------------------------------------------------------------------------------
st.subheader('Topic: Will Emerging Technologies Relplace Data Scientist???')
#---------------------------------------------------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload a file for analysis",type=['csv','xlsx'])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File was uploaded successfully !!!")
        st.markdown('File type of uploaded file is CSV :smile:')
    except Exception:
        df = pd.read_excel(uploaded_file)
        st.success("File was uploaded successfully !!!")
        st.markdown('File type of uploaded file is Excel:smile:')
#---------------------------------------------------------------------------------------------------------------------    
    click= st.checkbox(" YOU WANT TO SEE UPLOADED FILE ???")
    if click==True:
        st.dataframe(df)
        st.success('UPLOADED FILE AS READED SUCCESSFULLY !!!')
#------------------------------------------------------------------------------------------------------------------------------------------
    click= st.checkbox("YOU WANT TO DO EDA ON UPLOADED FILE ???")
    if click==True:
        A=['Number of rows & columns in uploaded file','Describe uploaded file','Information of uploaded file','columns in uploaded file','corelation between columns of file','Pairplot of all columns of file']
        col=st.selectbox("Select what you want to known:",A)
        if col=='Number of rows & columns in uploaded file':
            a=df.shape
            st.write('shape of dataframe:',a)
            st.success('EDA IS DONE SUCCESSFULLY !!!')
        elif col=='Describe uploaded file':
            st.write('Describing dataframe:')
            b=df.describe()
            st.dataframe(b)
            st.success('EDA IS DONE SUCCESSFULLY !!!')
        elif col=='Information of uploaded file':
            c=df.info
            st.write('Information of file:',c)
            st.success('EDA IS DONE SUCCESSFULLY !!!')
        elif col=='columns in uploaded file':
            d=df.columns
            st.write('Columns in file:',d)
            st.success('EDA IS DONE SUCCESSFULLY !!!')
        elif col=='corelation between columns of file':
            d=df.corr()
            st.dataframe(d)
            fig=sns.set(rc={"figure.figsize":(10, 10)})
            sns.heatmap(df.corr(),annot=True,cmap='coolwarm');
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(fig)
            st.success('EDA IS DONE SUCCESSFULLY !!!')
        elif col=='Pairplot of all columns of file':
            fig=sns.pairplot(df)
            st.pyplot(fig)
            st.success('EDA IS DONE SUCCESSFULLY !!!')

#---------------------------------------------------------------------------------------------------------------------------------------------            
    click= st.checkbox("WANT TO SEE CLEANING & PREPROCESSING OF FILE ???")
    if click==True:    
        e=df.isnull().sum().sort_values(ascending=False)
        st.write('Checking null values in dataframe:',e)
        f=(df.isnull().sum()*100/df.isnull().count()).sort_values(ascending=False)
        st.write('Percentage of null values in dataframe:',f)
        
        
        
    
        
    
