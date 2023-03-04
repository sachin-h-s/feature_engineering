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

# import streamlit as st
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import OneHotEncoder
# from base64 import b64encode


# # Define function to preprocess the data
# def preprocess_data(data, numeric_cols, categorical_cols):
#     # Scale numerical columns
#     scaler = StandardScaler()
#     data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
#     # One-hot encode categorical columns
#     encoder = OneHotEncoder()
#     encoded_data = encoder.fit_transform(data[categorical_cols])
#     encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_cols))
    
#     # Combine numerical and categorical columns
#     preprocessed_data = pd.concat([data[numeric_cols], encoded_df], axis=1)
    
#     return preprocessed_data


# # Define Streamlit app
# def main():
#     # Set app title
#     st.title("Data Preprocessing App")
    
#     # Create file uploader
#     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
#     if uploaded_file is not None:
#         # Load data from uploaded file
#         data = pd.read_csv(uploaded_file)
        
#         # Show original data
#         st.subheader("Original Data")
#         st.write(data)
        
#         # Select columns to preprocess
#         numeric_cols = st.multiselect("Select numeric columns to scale", data.select_dtypes(include=['float', 'int']).columns.tolist())
#         categorical_cols = st.multiselect("Select categorical columns to encode", data.select_dtypes(include=['object']).columns.tolist())
        
#         # Preprocess data
#         preprocessed_data = preprocess_data(data, numeric_cols, categorical_cols)
        
#         # Show preprocessed data
#         st.subheader("Preprocessed Data")
#         st.write(preprocessed_data)
        
#         # Create download link for preprocessed data
#         csv = preprocessed_data.to_csv(index=False)
#         href = f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="preprocessed_data.csv">Download Preprocessed Data</a>'
#         st.markdown(href, unsafe_allow_html=True)


# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import FeatureHasher
from base64 import b64encode


# Define function to preprocess the data
def preprocess_data(data, numeric_cols, categorical_cols):
    # Scale numerical columns
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    # Hash encode categorical columns
    hasher = FeatureHasher(n_features=1000, input_type='string')
    hashed_data = hasher.transform(data[categorical_cols].astype(str))
    hashed_df = pd.DataFrame(hashed_data.toarray(), columns=['hashed_' + str(i) for i in range(1000)])
    
    # Combine numerical and categorical columns
    preprocessed_data = pd.concat([data[numeric_cols], hashed_df], axis=1)
    
    return preprocessed_data


# Define Streamlit app
def main():
    # Set app title
    st.title("Data Preprocessing App")
    
    # Create file uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Load data from uploaded file
        data = pd.read_csv(uploaded_file)
        
        # Show original data
        st.subheader("Original Data")
        st.write(data)
        
        # Select columns to preprocess
        numeric_cols = st.multiselect("Select numeric columns to scale", data.select_dtypes(include=['float', 'int']).columns.tolist())
        categorical_cols = st.multiselect("Select categorical columns to hash", data.select_dtypes(include=['object']).columns.tolist())
        
        # Preprocess data
        preprocessed_data = preprocess_data(data, numeric_cols, categorical_cols)
        
        # Show preprocessed data
        st.subheader("Preprocessed Data")
        st.write(preprocessed_data)
        
        # Create download link for preprocessed data
        csv = preprocessed_data.to_csv(index=False)
        href = f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="preprocessed_data.csv">Download Preprocessed Data</a>'
        st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
