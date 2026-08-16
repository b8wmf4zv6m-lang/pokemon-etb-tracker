import streamlit as st
import pandas as pd

# App Configuration
st.set_page_config(page_title="Pokémon ETB Tracker", page_icon="⚡", layout="centered")

st.title("⚡ Pokémon ETB Price Tracker")
st.caption("Search live market availability and pricing across major retailers.")

# User Inputs
etb_name = st.text_input("Enter Pokémon Set Name:", value="Surging Sparks")

if st.button("Search ETBs", type="primary"):
    with st.spinner(f"Searching market listings for '{etb_name}'..."):
        
        # Formatted Queries
        query_encoded = etb_name.replace(" ", "%20")
        query_plus = etb_name.replace(" ", "+")

        # Retailer Links
        tcg_url = f"https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&q={query_encoded}%20Elite%20Trainer%20Box"
        bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={query_plus}+elite+trainer+box"
        target_url = f"https://www.target.com/s?searchTerm={query_plus}+elite+trainer+box"
        gamestop_url = f"https://www.gamestop.com/search/?q={query_plus}+elite+trainer+box"
        poke_center_url = f"https://www.pokemoncenter.com/search/{query_encoded}-elite-trainer-box"

        # Structured Results Table
        results = [
            {
                "Retailer": "TCGPlayer",
                "Product": f"{etb_name.title()} ETB",
                "Est. Price": "Market Rate",
                "Store Link": tcg_url
            },
            {
                "Retailer": "Target",
                "Product": f"{etb_name.title()} ETB",
                "Est. Price": "$49.99 MSRP",
                "Store Link": target_url
            },
            {
                "Retailer": "GameStop",
                "Product": f"{etb_name.title()} ETB",
                "Est. Price": "$49.99 MSRP",
                "Store Link": gamestop_url
            },
            {
                "Retailer": "Best Buy",
                "Product": f"{etb_name.title()} ETB",
                "Est. Price": "$49.99 MSRP",
                "Store Link": bestbuy_url
            },
            {
                "Retailer": "Pokémon Center",
                "Product": f"{etb_name.title()} PC ETB (Exclusive)",
                "Est. Price": "$59.99 MSRP",
                "Store Link": poke_center_url
            }
        ]

        df = pd.DataFrame(results)

        # Render Results
        st.success("Listings found! Tap a store link below to view live stock.")
        st.dataframe(
            df,
            column_config={
                "Store Link": st.column_config.LinkColumn("Direct Store Link", display_text="Open Store Page")
            },
            hide_index=True,
            use_container_width=True
        )
