import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="💿💿💿Data sweeper",layout='wide')
st.title("💿💿💿Data sweeper")
st.write("A data sweeper generally refers to a tool or process designed to remove or clean data from a system, often to protect privacy, improve efficiency, or prepare data for analysis.  ")
uploaded_files = st.file_uploader("upload you file (CSV or Excel):", type=["csv","xlsx"],accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()


        if file_ext ==".csv":
            df =pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file types:{file_ext}")
            continue        

        st.write(f"**file name:**{file.name}")
        st.write(f"**file size:**{file.size/1024}")


        st.write("Preview the head the dataframe")
        st.dataframe(df.head())

        st.subheader("data cleaning option")
        if st.checkbox(f"clean data for {file.name}"):
            col1, col2 =st.columns(2)

            with col1:
                if st.button(f"remove duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("duplicate removed!")

            with col2:
                if st.button(f"fill missing  value for {file.name}"):        
                 numeric_cols =df .select_dtypes(include=['number']).columns
                 df[numeric_cols] =df[numeric_cols].fillna(df[numeric_cols].mean())
                 st.write("missing value been failed!")

                st.subheader("👍👍selectcolums to covertert ")
                colums = st.multiselect(f"chose colums  for {file.name}",df.columns,default=df.columns)
                df = df[colums]

                st.subheader("🥽data visualization")
                if st.checkbox(f"show visualization for {file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

                st.subheader("🎗converstion options")
                conversion_type=st.radio(f"convert {file.name}to:",["CSV","Excel"], key=file.name)
                if st.button(f"converyt{file.name}"):
                    buffer =BytesIO()
                    if conversion_type=="CSV":
                        df.to_csv(buffer,index=False)
                        file_name = file.name.replace(file_ext,".csv")
                        mime_type ="text/csv"
                    elif conversion_type=="Excel":
                        df.to_excel(buffer, index=False)
                        file_name = file.name.replace(file_ext,".xlsx")
                        mime_type= "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)

                    st.download_button(
                        label=f"👇download {file.name} as {conversion_type}",
                        data=buffer,
                        filename=file_name,
                        mime=mime_type
                    )        
st.success("✔👉🏽All file proceed")


st.title("")

st.write("Thank you use me ❤")


footer = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    <div class="footer">
        <p>Created by Engr M.Kamil Hanif | mkamilhanif789@gmail.com</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)














