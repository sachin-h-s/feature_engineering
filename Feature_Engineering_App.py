# import streamlit as st
# import pandas as pd
# import base64
# @st.cache(allow_output_mutation=True)
# @st.cache
# def load_data(file):
#     return pd.read_csv(file)


# def main():
#     st.title("Feature Engineering App")
#     st.sidebar.title("Options")

#     uploaded_file = st.sidebar.file_uploader("Choose a CSV file:")
#     if uploaded_file is not None:
#         df = load_data(uploaded_file)
#         st.write("Original Data:")
#         st.write(df)
        
#         # Drop duplicate columns
#       #  df = df.T.drop_duplicates().T


#         # Add feature transformation options to the sidebar
#         if st.sidebar.checkbox("Scale numerical columns"):
#             scaler = st.sidebar.selectbox("Select scaling method:", ["MinMaxScaler", "StandardScaler"])
#             if scaler == "MinMaxScaler":
#                 df[df.select_dtypes(include='number').columns] = (df[df.select_dtypes(include='number').columns] - df[df.select_dtypes(include='number').columns].min()) / (df[df.select_dtypes(include='number').columns].max() - df[df.select_dtypes(include='number').columns].min())
#             elif scaler == "StandardScaler":
#                 df[df.select_dtypes(include='number').columns] = (df[df.select_dtypes(include='number').columns] - df[df.select_dtypes(include='number').columns].mean()) / df[df.select_dtypes(include='number').columns].std()

#         if st.sidebar.checkbox("One-hot encode categorical columns"):
#             df = pd.get_dummies(df)

#         if st.sidebar.checkbox("Add polynomial features"):
#             degree = st.sidebar.slider("Select polynomial degree:", 1, 5, 2)
#             from sklearn.preprocessing import PolynomialFeatures
#             poly = PolynomialFeatures(degree=degree)
#             df = pd.DataFrame(poly.fit_transform(df))
            
            
#                 # Add a download button to download the processed data as a CSV file
#         if st.sidebar.button("Download processed data"):
#             st.write("Processed Data:")
#             st.write(df)
#             csv = df.to_csv(index=False)
#             b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#             href = f'<a href="data:file/csv;base64,{b64}" download="processed_data.csv">Download processed data</a>'
#             st.markdown(href, unsafe_allow_html=True)


# if __name__=='__main__':
#     main()

import streamlit as st
import pandas as pd
import base64

@st.cache(allow_output_mutation=True)
def load_data(file):
    return pd.read_csv(file)

def main():
    st.title("Feature Engineering App")
    st.sidebar.title("Options")

    uploaded_file = st.sidebar.file_uploader("Choose a CSV file:")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("Original Data:")
        st.write(df)

        # Add feature transformation options to the sidebar
        if st.sidebar.checkbox("Scale numerical columns"):
            scaler = st.sidebar.selectbox("Select scaling method:", ["MinMaxScaler", "StandardScaler"])
            if scaler == "MinMaxScaler":
                df[df.select_dtypes(include='number').columns] = (df[df.select_dtypes(include='number').columns] - df[df.select_dtypes(include='number').columns].min()) / (df[df.select_dtypes(include='number').columns].max() - df[df.select_dtypes(include='number').columns].min())
            elif scaler == "StandardScaler":
                df[df.select_dtypes(include='number').columns] = (df[df.select_dtypes(include='number').columns] - df[df.select_dtypes(include='number').columns].mean()) / df[df.select_dtypes(include='number').columns].std()

        if st.sidebar.checkbox("One-hot encode categorical columns"):
            df = pd.get_dummies(df)

        if st.sidebar.checkbox("Add polynomial features"):
            degree = st.sidebar.slider("Select polynomial degree:", 1, 5, 2)
            from sklearn.preprocessing import PolynomialFeatures
            poly = PolynomialFeatures(degree=degree)
            df = pd.DataFrame(poly.fit_transform(df))
            
        # Add a download button to download the processed data as a CSV file
        if st.sidebar.button("Download processed data"):
            st.write("Processed Data:")
            st.write(df)
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="processed_data.csv">Download processed data</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__=='__main__':
    main()

