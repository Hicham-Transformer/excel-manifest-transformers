import streamlit as st
import pandas as pd
import io

column_mapping = {
    'OrderNumber': 'MawbNr',
    'ParcelBarcode': 'ParcelID',
    'BoxBagbarcode': 'PackageBarcode',
    'IOSS': 'SellerIOSSNr',
    'CSOR_COUNTRY': 'SellerCountryCode',
    'Namereceiver': 'BuyerName',
    'Addressreceiver': 'BuyerStreet',
    'Zipcodereceiver': 'BuyerZipcode',
    'Cityreceiver': 'BuyerCity',
    'Countrycodereceiver': 'BuyerCountryCode',
    'Quantity': 'Quantity',
    'Total weight': 'Weight',
    'Hscode': 'ItemHSCode',
    'Productdescription': 'GoodsDescription',
    'Currency': 'InvoiceCurrency',
    'total value': 'InvoiceAmount',
    'Shippingcosts': 'ShippingMethod'
}

st.title("📦 Excel Manifest Transformer")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
df = pd.read_excel(uploaded_file)

# Alleen kolommen gebruiken die WEL bestaan in het bestand
available_mapping = {k: v for k, v in column_mapping.items() if k in df.columns}

if not available_mapping:
    st.error("❌ No matching columns found in the uploaded file.")
else:
    transformed_df = df[list(available_mapping.keys())].rename(columns=available_mapping)
    st.success("✅ Transformation complete!")
    st.dataframe(transformed_df)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        transformed_df.to_excel(writer, index=False)
    st.download_button("📥 Download Transformed File", output.getvalue(), file_name="Transformed_Manifest.xlsx")
    else:
        transformed_df = df[list(column_mapping.keys())].rename(columns=column_mapping)
        st.success("✅ Transformation complete!")
        st.dataframe(transformed_df)

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            transformed_df.to_excel(writer, index=False)
        st.download_button("📥 Download Transformed File", output.getvalue(), file_name="Transformed_Manifest.xlsx")