import streamlit as st
import requests

def fetch_product_info(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    return response.json()

def main():
    st.title("Food Nutrition Info App")
    st.write("Enter a barcode to get nutritional information")

    barcode = st.text_input("Enter barcode:")

    if st.button("Get Info"):
        if barcode:
            with st.spinner("Fetching data..."):
                product_data = fetch_product_info(barcode)

            if product_data["status"] == 1:
                product = product_data["product"]
                st.subheader(product.get("product_name", "Unknown Product"))
                
                st.image(product.get("image_url", ""), width=200)
                
                st.write("Nutritional Information (per 100g):")
                nutrients = product.get("nutriments", {})
                st.write(f"Energy: {nutrients.get('energy-kcal_100g', 'N/A')} kcal")
                st.write(f"Fat: {nutrients.get('fat_100g', 'N/A')} g")
                st.write(f"Carbohydrates: {nutrients.get('carbohydrates_100g', 'N/A')} g")
                st.write(f"Proteins: {nutrients.get('proteins_100g', 'N/A')} g")
                st.write(f"Salt: {nutrients.get('salt_100g', 'N/A')} g")
                
                st.write("Ingredients:")
                st.write(product.get("ingredients_text", "No ingredient information available"))
            else:
                st.error("Product not found. Please check the barcode and try again.")
        else:
            st.warning("Please enter a barcode.")

if __name__ == "__main__":
    main()
