import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
np_bool = bool(True)  # or np.bool_(True)



def navigate_to_tab(tab_name):
    st.session_state.current_tab = tab_name
    st.experimental_rerun()



def create_chart_page():
    st.title("Interactive Charts with Your Data")

    # Load your data from the CSV file
    df = pd.read_csv("dataset.csv") 

    df["SEX"] = pd.to_numeric(df["SEX"])
    df["SEX"] = df["SEX"].map({1:"FEMALE", 2:"MALE", 99:"UNKNOWN"})

    df["OUTCOME"] = pd.to_numeric(df["OUTCOME"])
    df["OUTCOME"] = df["OUTCOME"].map({1:"POSITIVE", 2:"NEGATIVE", 3:"PENDING"})

    df["NATIONALITY"] = pd.to_numeric(df["NATIONALITY"])
    df["NATIONALITY"] = df["NATIONALITY"].map({1:"MEXICAN", 2:"FOREIGN", 99:"UNKNOWN"})

    df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1:"NO", 2:"YES", 99:"UNKNOWN"})

    df[["INTUBATED", "PNEUMONIA", "PREGNANCY", "SPEAKS_NATIVE_LANGUAGE", "DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "OTHER_DISEASE", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO","ANOTHER CASE", "MIGRANT", "ICU"]] = df[["INTUBATED", "PNEUMONIA", "PREGNANCY", "SPEAKS_NATIVE_LANGUAGE", "DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION", "OTHER_DISEASE", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO", "ANOTHER CASE", "MIGRANT", "ICU"]].map(lambda x: {1:"YES", 2:"NO", 97:"DOES NOT APPLY", 98:"IGNORED", 99:"UNKNOWN"}.get(x, x))
    sex_counts= df["SEX"].value_counts()
    #st.dataframe(df)
    
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Bar Chart", "Pie Chart", "Correlation Matrix", "Histogram", "+"])

    with tab1:
        st.title("Hospitalized Case")
        st.bar_chart(df['HOSPITALIZED'].value_counts())
        # Calculate value counts
        hosp_counts = df['HOSPITALIZED'].value_counts()
        # Display the value counts
        st.write("Value Counts for HOSPITALIZED Column:")
        st.table(hosp_counts)
        
        deceased_patients = df[~df['DATE_OF_DEATH'].isna()]

        diseases = ['PNEUMONIA', 'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 
                'HYPERTENSION', 'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']

        data_list = []

        for d in diseases:
            count = deceased_patients[deceased_patients[d] == 'YES'][d].count()
            data_list.append({'Disease': d, 'Count': count})

        st.title("Common Disease in Deceased Patient")
        disease_counts = pd.DataFrame(data_list)

        plt.figure(figsize=(10, 6))
        chart2=sns.barplot(x='Disease', y='Count', data=disease_counts, color='lightblue')

        for p in chart2.patches:
            height = p.get_height()
            chart2.annotate(f'{height}', 
                        (p.get_x() + p.get_width() / 2, height), 
                        ha='center', 
                        va='bottom', 
                        fontsize=10) 
            
        plt.xlabel('Disease')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        st.pyplot()


    with tab2:
        
        st.title("Case by Gender")
        # Load your dataset
        df = pd.read_csv("dataset.csv")
        # Calculate value counts for the "SEX" column
        sex_counts = df['SEX'].value_counts()
        # Create a pie chart using Plotly
        fig = px.pie(sex_counts, names=sex_counts.index, values=sex_counts.values, title='Value Counts for SEX Column')
        # Display the pie chart in Streamlit
        st.plotly_chart(fig)

    with tab3:

        # Function to create the correlation heatmap
        def plot_corr_heatmap(data):
        # Filter and convert categorical data to numerical
            corrdf = data[['ICU', 'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR',
                            'HYPERTENSION', 'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']]
            corrdf = corrdf.replace({'YES': 1, 'NO': 0, 'DOES NOT APPLY': 0, 'IGNORED': 0, 'UNKNOWN': 0})

            # Calculate correlation matrix
            corr_matrix = corrdf.corr()

            # Create the heatmap
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, ax=ax)
            plt.title('Correlation Between Diseases and ICU Admission (ICU Cases)')
            return fig
            # Display the chart in Streamlit
        fig = plot_corr_heatmap(df.copy())
        st.pyplot(fig)


    
    with tab4:

        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


        st.title("Distribution of Ages")


        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=df, x='AGE', bins=bins, color='skyblue', edgecolor='black', ax=ax)
        ax.set_xlabel('Age', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title('Distribution of Ages', fontsize=14)
        ax.set_xticks(bins)
        ax.grid(True)

        st.pyplot(fig)







    
if __name__ == "__main__":
    create_chart_page()



