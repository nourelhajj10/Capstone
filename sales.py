import streamlit as st
import pandas as pd
import pickle
import os
import zipfile
from sklearn.ensemble import RandomForestClassifier


# Load each sheet into a DataFrame
sales = pd.read_csv("sales_encoded.csv")

# Path to your zip file
zip_file_path = 'best_rf_reg_sales.zip'

# Path to where you are currently working
working_folder = 'D:/augustmess/Fullbright/internshipMess/Internship/RMNour'

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract the pickle file to the working folder
    zip_ref.extractall(working_folder)

# Now you can proceed to use the pickle file
pickle_file_name = 'best_rf_reg_sales.pkl'
extracted_pickle_file_path = os.path.join(working_folder, pickle_file_name)

# Now you can proceed to use the pickle file
with open(extracted_pickle_file_path, 'rb') as f:
    data = pickle.load(f)
    
    
# Define custom CSS styles
custom_css = """
<style>
    body {
        background-color: #f5f5f5; /* Background color for the entire page */
        font-family: Arial, sans-serif; /* Font for the entire page */
    }

    .title {
        font-size: 30px; /* Font size for the title */
        color: #000; /* Set title color to black */
        text-align: center; /* Center the title */
        padding: 5px 0; /* Add some padding */
    }

    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .column {
        width: 45%; /* Adjust the width as needed */
        background-color: #fff; /* Background color for the columns */
        border: 1px solid #ddd; /* Add a border around columns */
        padding: 10px; /* Add padding to columns */
        margin: 10px 0; /* Add margin between columns */
    }

    .text-input {
        background-color: #eee; /* Background color for text inputs */
    }
</style>
"""

def display_day_of_week(choice):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    st.write(f"**You chose {days_of_week[choice]}.**")


def display_month(choice):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    st.write(f"**You chose {months[choice - 1]}.**")  # Adjusting for 1-based indexing of months
    
    
# Main function to run the Streamlit app
def main():
    st.set_page_config(
        page_title="Sales Prediction",
        page_icon="✅",
        layout="wide"  # Use wide layout for fixed sidebar
    )
    
    # Include custom CSS styles

    # Sidebar style
    st.sidebar.title("Navigation Menu")
    menu = st.sidebar.selectbox("Choose an option:", ["Home", "Sales Volume Prediction"])

    if menu == "Home":
        image1 = "logo.jpg"
        image2 = "aub.jpg"

        st.markdown(custom_css, unsafe_allow_html=True)
        # Display images on the top left and top right
        st.image(image1, width=200)
        st.image(image2, width=100)
        st.markdown('<p class="title"> Nour El Haj </p>', unsafe_allow_html=True)
        st.markdown('<p class="title"> Zee Optimization: Enhanced Production Efficiency and Market Dominance with a Holistic Data-Driven Approach</p>', unsafe_allow_html=True)
        
   
        
        st.write("For more than 50 years, ZEENNI STEEL INDUSTRIES & TRADING S.A.L. has been a pioneer in"
                    "the world in providing premium steel goods and services. They have established themselves as a"
                    "trustworthy collaborator by leading the business and providing innovative solutions all around the"
                    "world.")
        st.write("")  # This adds an empty line
        
        st.write("Overview of Services")
        st.write("")

        st.write("- Metal trading provides customized solutions for different sectors via smooth trades."
                    "- Steel bending services are available, offering the accuracy and skill necessary to bend steel into"
                    "specific forms that precisely satisfy the demands of various projects."
                    "- Steel drilling and sawing services to ensure the efficient execution of the project by creating"
                    "precise holes and cuts that adhere to the project standards."
                    "- Steel cutting services to guarantee top-notch results using accurate and efficient techniques, and"
                    "customizing each cut to the project criteria."
                    "- Steel manufacturing by applying modern technologies to guarantee robustness and compliance"
                    "with standards in the industry."
                    "- CNC cutting implemented to cut a wide range of materials ensuring exceptional")
        
     
     
     
    if menu == "Sales Volume Prediction":
            st.markdown(custom_css, unsafe_allow_html=True)
            st.markdown('<p class="title"> Sales Volume Prediction </p>', unsafe_allow_html=True)
            
            
            
            def create_item_number_dataframe(user_choice):
                # Define the item number
                all_item_number = ['AN20x20/2.4TRS235',
                                        'AN25x25/2.4TRS235',
                                        'AN25x25/2.5TRS235',
                                        'AN30x30/2.5TRS235',
                                        'AN30x30/2.8TRS235',
                                        'AN30x30/3TRS235',
                                        'AN30x30/3UA',
                                        'AN35x35/3.5TRS235',
                                        'AN35x35/3TRS235',
                                        'AN35x35/4TRS235',
                                        'AN40x40/3TRS235',
                                        'AN40x40/3UA',
                                        'AN40x40/4TRS235',
                                        'AN40x40/4UA',
                                        'AN50x50/3TRS235',
                                        'AN50x50/4TRS235',
                                        'AN50x50/5TRS235',
                                        'AN60x60/5TRS235',
                                        'AN60x60/6TRS235',
                                        'AN70x70/6TRS235',
                                        'AN70x70/7TRS235',
                                        'AN80x80/8TRS235',
                                        'CRROD20',
                                        'CRROD25',
                                        'CRROD30',
                                        'CRROD35',
                                        'CRROD40',
                                        'CRROD70',
                                        'HEA100ESS275',
                                        'HEA120ESS275',
                                        'HEA140ESS275',
                                        'HEA160ESS275',
                                        'HEA160ESS355',
                                        'HEA180ESS275',
                                        'HEA200ESS275',
                                        'HEA220ESS275',
                                        'HEA240ESS275',
                                        'HEA260ESS275',
                                        'HEA280ESS275',
                                        'HEA300ESS275',
                                        'HEA400ESS275',
                                        'HEA450ESS275',
                                        'HEB140ESS275',
                                        'HEB160ESS275',
                                        'HEB200ESS275',
                                        'HEB220ESS275',
                                        'HEB240ESS275',
                                        'HEB300ESS275',
                                        'HEB400ESS275',
                                        'HEB400ESS355',
                                        'HRFL100/10TRS235',
                                        'HRFL100/6TRS235',
                                        'HRFL100/8TRS235',
                                        'HRFL12/5TRS235',
                                        'HRFL120/20ESS275',
                                        'HRFL120/20ITS235',
                                        'HRFL14/5TRS235',
                                        'HRFL16/3TRS235',
                                        'HRFL16/8TRS235',
                                        'HRFL20/10TRS235',
                                        'HRFL20/3TRS235',
                                        'HRFL20/5TRS235',
                                        'HRFL20/8TRS235',
                                        'HRFL200/10ESS275',
                                        'HRFL200/15ESS275',
                                        'HRFL25/10TRS235',
                                        'HRFL25/3TRS235',
                                        'HRFL25/5TRS235',
                                        'HRFL25/8TRS235',
                                        'HRFL250/20ESS275',
                                        'HRFL30/10TRS235',
                                        'HRFL30/12TRS235',
                                        'HRFL30/3TRS235',
                                        'HRFL30/5TRS235',
                                        'HRFL30/8TRS235',
                                        'HRFL40/10TRS235',
                                        'HRFL40/12TRS235',
                                        'HRFL40/3TRS235',
                                        'HRFL40/5TRS235',
                                        'HRFL40/8TRS235',
                                        'HRFL50/10TRS235',
                                        'HRFL50/3TRS235',
                                        'HRFL50/5TRS235',
                                        'HRFL50/8TRS235',
                                        'HRFL60/30ESS275',
                                        'HRFL60/6TRS235',
                                        'HRFL60/8TRS235',
                                        'HRFL80/10TRS235',
                                        'HRFL80/20ESS275',
                                        'HRFL80/6TRS235',
                                        'HRPL10CNS275',
                                        'HRPL10CNS355',
                                        'HRPL12CNS275',
                                        'HRPL15CNS275',
                                        'HRPL15CNS355',
                                        'HRPL20CNS275',
                                        'HRPL25CNS275',
                                        'HRPL25CNS355JR',
                                        'HRPL30CNS275',
                                        'HRPL40CNS275',
                                        'HRPL6CNS355JR',
                                        'HRPL8CNS275JR',
                                        'HRPL8CNS355JR',
                                        'HRRB10TRS235',
                                        'HRRB12TRS235',
                                        'HRRB14TRS235',
                                        'HRRB16TRS235',
                                        'HRRB18TRS235',
                                        'HRRB20TRS235',
                                        'HRRB25TRS235',
                                        'HRSQ10TRS235',
                                        'HRSQ10UA',
                                        'HRSQ12TRS235',
                                        'HRSQ12UA',
                                        'HRSQ14TRS235',
                                        'HRSQ14UA',
                                        'HRSQ16TRS235',
                                        'HRSQ16UA',
                                        'HRSQ20TRS235',
                                        'HRSQ25TRS235',
                                        'HRSQ30TRS235',
                                        'HRSQ30TRS275JR',
                                        'HRSQ40TRS275JR',
                                        'HRSQ50TRS275JR',
                                        'HRSQM11.5TR',
                                        'HRSQM14TR',
                                        'HRSQM16TRS235',
                                        'IPE100TRS235',
                                        'IPE100TRS275JR',
                                        'IPE120TRS235',
                                        'IPE120TRS275JR',
                                        'IPE140TRS235',
                                        'IPE140TRS275JR',
                                        'IPE160TRS235',
                                        'IPE160TRS275JR',
                                        'IPE180ESS275',
                                        'IPE180TRS275JR',
                                        'IPE200TRS235',
                                        'IPE200TRS275JR',
                                        'IPE220ESS275',
                                        'IPE240ESS275',
                                        'IPE270ESS275',
                                        'IPE300ESS275',
                                        'IPE330ESS275',
                                        'IPE360ESS275',
                                        'IPE400ESS275',
                                        'IPE450ESS275',
                                        'IPE600ESS275',
                                        'IPE80TRS235',
                                        'IPEA100TRS275JR',
                                        'IPEA120TRS275JR',
                                        'IPEA140TRS275JR',
                                        'IPEA160TRS275JR',
                                        'IPEA220ESS275',
                                        'IPEA240ESS275',
                                        'IPEA270ESS275',
                                        'IPEA300ESS275',
                                        'IPEA360ESS275',
                                        'IPEA400ESS275',
                                        'IPEA450ESS275',
                                        'TE30TRS235',
                                        'TE35TRS235',
                                        'UPN100TRS235',
                                        'UPN120TRS235',
                                        'UPN140TRS235',
                                        'UPN160TRS235',
                                        'UPN200TRS275JR',
                                        'UPN240ESS275',
                                        'UPN260ESS275',
                                        'UPN300ESS275',
                                        'UPN40TRS235',
                                        'UPN50TRS235',
                                        'UPN60TRS235',
                                        'UPN65TRS235',
                                        'UPN80TRS235']

                # Create a dictionary with zeros for all item number
                data = {item_choice: 0 for item_choice in all_item_number}

                # Set the chosen item number to 1
                data[user_choice] = 1

                # Create a dataframe from the dictionary
                df = pd.DataFrame([data])
                return df
            
            
            def create_shape_dataframe(user_choice):
                # Define the shapes
                # remove angles
                all_shapes = ['Flat Bars','HEA Beams','HEB Beam','IPE Beams','IPEA Beams','Round Bars', 'Square Bar','Square Bar Mdarrab','T Bar','Shape_UPN Beams']

                # Create a dictionary with zeros for all shapes
                data = {shape_choice: 0 for shape_choice in all_shapes}

                # Set the chosen shape to 1
                data[user_choice] = 1

                # Create a dataframe from the dictionary
                df = pd.DataFrame([data])
                return df
            
            
            
            
            def create_origin_dataframe(user_choice):
                # remove china
                # Define the origins
                all_origin = ['italy',' lebanon','spain','turkey','ukraine']

                # Create a dictionary with zeros for all origins
                data = {origin_choice: 0 for origin_choice in all_origin}

                # Set the chosen origin to 1
                data[user_choice] = 1

                # Create a dataframe from the dictionary
                df = pd.DataFrame([data])
                return df
            

            def create_width_dataframe(user_choice):
                # Define the allowed width values
                allowed_widths = [2000, 1500, 2500, 1000, 1250]

                # Sort the allowed width values
                allowed_widths.sort()

                # Create a dictionary with zeros for all width values
                data = {width: 0 for width in allowed_widths}

                # Set the chosen width to 1
                data[user_choice] = 1

                # Create a DataFrame from the dictionary
                df = pd.DataFrame([data])
                return df
            

            def create_length_dataframe(user_choice):
                # Define the allowed length values
                allowed_lengths = [12000, 6000, 10500, 4000, 7500, 3000, 2000, 2500, 6250, 5000]

                # Sort the allowed length values
                allowed_lengths.sort()

                # Create a dictionary with zeros for all length values
                data = {length: 0 for length in allowed_lengths}

                # Set the chosen length to 1
                data[user_choice] = 1

                # Create a DataFrame from the dictionary
                df = pd.DataFrame([data])
                return df
            


            def create_price_dataframe(user_choice):
                # Validate if the entered value is within the specified range
                if user_choice < 0.3 or user_choice > 1000.0:
                    print("Please enter a valid price between 0.3 and 1000.")
                    return None

                # Define the allowed price range
                allowed_prices = [round(x * 0.01, 2) for x in range(30, 100001)]

                # Sort the allowed price range
                allowed_prices.sort()

                # Create a dictionary with zeros for all price values
                data = {price: 0 for price in allowed_prices}

                # Set the chosen price to 1
                data[user_choice] = 1

                # Create a DataFrame from the dictionary
                df = pd.DataFrame([data])
                return df
        

            def create_year_dataframe(user_choice):
                # Define the allowed year values
                allowed_years = [2021, 2022, 2023, 2024]

                # Sort the allowed year values
                allowed_years.sort()

                # Create a dictionary with zeros for all year values
                data = {year: 0 for year in allowed_years}

                # Set the chosen year to 1
                data[user_choice] = 1

                # Create a DataFrame from the dictionary
                df = pd.DataFrame([data])
                return df

                       
            def display_choice_result(choice):
                if choice == 1:
                    st.write("Yes")

                else:
                    st.write("No")

            
            item_number = st.sidebar.selectbox('Item number',(

                                        'AN20x20/2.4TRS235',
                                        'AN25x25/2.4TRS235',
                                        'AN25x25/2.5TRS235',
                                        'AN30x30/2.5TRS235',
                                        'AN30x30/2.8TRS235',
                                        'AN30x30/3TRS235',
                                        'AN30x30/3UA',
                                        'AN35x35/3.5TRS235',
                                        'AN35x35/3TRS235',
                                        'AN35x35/4TRS235',
                                        'AN40x40/3TRS235',
                                        'AN40x40/3UA',
                                        'AN40x40/4TRS235',
                                        'AN40x40/4UA',
                                        'AN50x50/3TRS235',
                                        'AN50x50/4TRS235',
                                        'AN50x50/5TRS235',
                                        'AN60x60/5TRS235',
                                        'AN60x60/6TRS235',
                                        'AN70x70/6TRS235',
                                        'AN70x70/7TRS235',
                                        'AN80x80/8TRS235',
                                        'CRROD20',
                                        'CRROD25',
                                        'CRROD30',
                                        'CRROD35',
                                        'CRROD40',
                                        'CRROD70',
                                        'HEA100ESS275',
                                        'HEA120ESS275',
                                        'HEA140ESS275',
                                        'HEA160ESS275',
                                        'HEA160ESS355',
                                        'HEA180ESS275',
                                        'HEA200ESS275',
                                        'HEA220ESS275',
                                        'HEA240ESS275',
                                        'HEA260ESS275',
                                        'HEA280ESS275',
                                        'HEA300ESS275',
                                        'HEA400ESS275',
                                        'HEA450ESS275',
                                        'HEB140ESS275',
                                        'HEB160ESS275',
                                        'HEB200ESS275',
                                        'HEB220ESS275',
                                        'HEB240ESS275',
                                        'HEB300ESS275',
                                        'HEB400ESS275',
                                        'HEB400ESS355',
                                        'HRFL100/10TRS235',
                                        'HRFL100/6TRS235',
                                        'HRFL100/8TRS235',
                                        'HRFL12/5TRS235',
                                        'HRFL120/20ESS275',
                                        'HRFL120/20ITS235',
                                        'HRFL14/5TRS235',
                                        'HRFL16/3TRS235',
                                        'HRFL16/8TRS235',
                                        'HRFL20/10TRS235',
                                        'HRFL20/3TRS235',
                                        'HRFL20/5TRS235',
                                        'HRFL20/8TRS235',
                                        'HRFL200/10ESS275',
                                        'HRFL200/15ESS275',
                                        'HRFL25/10TRS235',
                                        'HRFL25/3TRS235',
                                        'HRFL25/5TRS235',
                                        'HRFL25/8TRS235',
                                        'HRFL250/20ESS275',
                                        'HRFL30/10TRS235',
                                        'HRFL30/12TRS235',
                                        'HRFL30/3TRS235',
                                        'HRFL30/5TRS235',
                                        'HRFL30/8TRS235',
                                        'HRFL40/10TRS235',
                                        'HRFL40/12TRS235',
                                        'HRFL40/3TRS235',
                                        'HRFL40/5TRS235',
                                        'HRFL40/8TRS235',
                                        'HRFL50/10TRS235',
                                        'HRFL50/3TRS235',
                                        'HRFL50/5TRS235',
                                        'HRFL50/8TRS235',
                                        'HRFL60/30ESS275',
                                        'HRFL60/6TRS235',
                                        'HRFL60/8TRS235',
                                        'HRFL80/10TRS235',
                                        'HRFL80/20ESS275',
                                        'HRFL80/6TRS235',
                                        'HRPL10CNS275',
                                        'HRPL10CNS355',
                                        'HRPL12CNS275',
                                        'HRPL15CNS275',
                                        'HRPL15CNS355',
                                        'HRPL20CNS275',
                                        'HRPL25CNS275',
                                        'HRPL25CNS355JR',
                                        'HRPL30CNS275',
                                        'HRPL40CNS275',
                                        'HRPL6CNS355JR',
                                        'HRPL8CNS275JR',
                                        'HRPL8CNS355JR',
                                        'HRRB10TRS235',
                                        'HRRB12TRS235',
                                        'HRRB14TRS235',
                                        'HRRB16TRS235',
                                        'HRRB18TRS235',
                                        'HRRB20TRS235',
                                        'HRRB25TRS235',
                                        'HRSQ10TRS235',
                                        'HRSQ10UA',
                                        'HRSQ12TRS235',
                                        'HRSQ12UA',
                                        'HRSQ14TRS235',
                                        'HRSQ14UA',
                                        'HRSQ16TRS235',
                                        'HRSQ16UA',
                                        'HRSQ20TRS235',
                                        'HRSQ25TRS235',
                                        'HRSQ30TRS235',
                                        'HRSQ30TRS275JR',
                                        'HRSQ40TRS275JR',
                                        'HRSQ50TRS275JR',
                                        'HRSQM11.5TR',
                                        'HRSQM14TR',
                                        'HRSQM16TRS235',
                                        'IPE100TRS235',
                                        'IPE100TRS275JR',
                                        'IPE120TRS235',
                                        'IPE120TRS275JR',
                                        'IPE140TRS235',
                                        'IPE140TRS275JR',
                                        'IPE160TRS235',
                                        'IPE160TRS275JR',
                                        'IPE180ESS275',
                                        'IPE180TRS275JR',
                                        'IPE200TRS235',
                                        'IPE200TRS275JR',
                                        'IPE220ESS275',
                                        'IPE240ESS275',
                                        'IPE270ESS275',
                                        'IPE300ESS275',
                                        'IPE330ESS275',
                                        'IPE360ESS275',
                                        'IPE400ESS275',
                                        'IPE450ESS275',
                                        'IPE600ESS275',
                                        'IPE80TRS235',
                                        'IPEA100TRS275JR',
                                        'IPEA120TRS275JR',
                                        'IPEA140TRS275JR',
                                        'IPEA160TRS275JR',
                                        'IPEA220ESS275',
                                        'IPEA240ESS275',
                                        'IPEA270ESS275',
                                        'IPEA300ESS275',
                                        'IPEA360ESS275',
                                        'IPEA400ESS275',
                                        'IPEA450ESS275',
                                        'TE30TRS235',
                                        'TE35TRS235',
                                        'UPN100TRS235',
                                        'UPN120TRS235',
                                        'UPN140TRS235',
                                        'UPN160TRS235',
                                        'UPN200TRS275JR',
                                        'UPN240ESS275',
                                        'UPN260ESS275',
                                        'UPN300ESS275',
                                        'UPN40TRS235',
                                        'UPN50TRS235',
                                        'UPN60TRS235',
                                        'UPN65TRS235',
                                        'UPN80TRS235'))
            st.write("**You chose for the Item number feature:**")
            st.write(item_number)
            df_item_number = create_item_number_dataframe(item_number)
            #st.write("Encoded Item number DataFrame:")
            #st.write(df_item_number)

            
            shape = st.sidebar.selectbox('Shape',('Flat Bars','HEA Beams','HEB Beam','IPE Beams','IPEA Beams','Round Bars', 'Square Bar','Square Bar Mdarrab','T Bar','Shape_UPN Beams'))
            st.write("**You chose for the Shape feature:**")
            st.write(shape)
            df_shape= create_shape_dataframe(shape)
            #st.write("Encoded Shape DataFrame:")
            #st.write(df_shape)

            dimension = st.sidebar.number_input("Enter a non-negative integer for Dimension between 6 and 80:", min_value=6,max_value = 80,step=1)
            st.write("**You chose for the Dimension feature:**")
            st.write(dimension)
            
            origin = st.sidebar.selectbox('Origin',('italy',' lebanon','spain','turkey','ukraine'))
            st.write("**You chose for the Origin feature:**")
            st.write(origin)
            df_origin = create_origin_dataframe(origin)
            #st.write("Encoded Origin DataFrame:")
            #st.write(df_origin)
            
            width = st.sidebar.selectbox('Width',([1000,1250, 1500, 2000, 2500]))
            st.write("**You chose for the Width feature:**")
            st.write(width)
            df_width = create_width_dataframe(width)
            #st.write("Encoded Width DataFrame:")
            #st.write(df_width)
            
            length = st.sidebar.selectbox('Length',([2000, 2500, 3000, 4000, 5000, 6000, 6250, 7500, 10500,12000]))
            st.write("**You chose for the Length feature:**")
            st.write(length)
            df_length = create_length_dataframe(length)
            #st.write("Encoded Length DataFrame:")
            #st.write(df_length)
            
            
            unit_price = st.sidebar.number_input("Enter a non-negative integer for unit price between 0.5 and 1.4:", min_value=0.5,max_value = 1.4,step=0.01)
            st.write("**You chose for the Unit price feature:**")
            st.write(unit_price)
            
            price = st.sidebar.number_input("Enter a non-negative integer for price between 0.3 and 9999.1:", min_value=0.3,max_value = 9999.1,step=1.2)
            st.write("**You chose for the Price feature:**")
            st.write(price)
            
            
            year = st.sidebar.selectbox('Year',([2021, 2022, 2023, 2024]))
            st.write("**You chose for the year feature:**")
            st.write(year)
            df_year = create_year_dataframe(year)

            
            Month = st.sidebar.slider("Select a number between 1 and 12 for Month:", min_value=1, max_value=12, step=1)
            # Call the function to display the selected month
            display_month(Month)
            
            DayOfWeek = st.sidebar.slider("Select a number between 0 and 6 for DayOfWeek:", min_value=0, max_value=6, step=1)
            display_day_of_week(DayOfWeek)


            
            data = { 
                    
                'Width' : width,
                'Length' : length,
                'Dimension' : dimension,
                'Unit Price' : unit_price,
                'Price' : price,
                'Year' : year,
                'Month' : Month,
                'Weekday' : DayOfWeek,
                
                
                'Item number_AN20x20/2.4TRS235': df_item_number.iloc[0, 0],
                'Item number_AN25x25/2.4TRS235': df_item_number.iloc[0, 1],
                'Item number_AN25x25/2.5TRS235': df_item_number.iloc[0, 2],
                'Item number_AN30x30/2.5TRS235': df_item_number.iloc[0, 3],
                'Item number_AN30x30/2.8TRS235': df_item_number.iloc[0, 4],
                'Item number_AN30x30/3TRS235': df_item_number.iloc[0, 5],
                'Item number_AN30x30/3UA': df_item_number.iloc[0, 6],
                'Item number_AN35x35/3.5TRS235': df_item_number.iloc[0, 7],
                'Item number_AN35x35/3TRS235': df_item_number.iloc[0, 8],
                'Item number_AN35x35/4TRS235': df_item_number.iloc[0, 9],
                'Item number_AN40x40/3TRS235': df_item_number.iloc[0, 10],
                'Item number_AN40x40/3UA': df_item_number.iloc[0, 11],
                'Item number_AN40x40/4TRS235': df_item_number.iloc[0, 12],
                'Item number_AN40x40/4UA': df_item_number.iloc[0, 13],
                'Item number_AN50x50/3TRS235': df_item_number.iloc[0, 14],
                'Item number_AN50x50/4TRS235': df_item_number.iloc[0, 15],
                'Item number_AN50x50/5TRS235': df_item_number.iloc[0, 16],
                'Item number_AN60x60/5TRS235': df_item_number.iloc[0, 17],
                'Item number_AN60x60/6TRS235': df_item_number.iloc[0, 18],
                'Item number_AN70x70/6TRS235': df_item_number.iloc[0, 19],
                'Item number_AN70x70/7TRS235': df_item_number.iloc[0, 20],
                'Item number_AN80x80/8TRS235': df_item_number.iloc[0, 21],
                'Item number_CRROD20': df_item_number.iloc[0, 22],
                'Item number_CRROD25': df_item_number.iloc[0, 23],
                'Item number_CRROD30': df_item_number.iloc[0, 24],
                'Item number_CRROD35': df_item_number.iloc[0, 25],
                'Item number_CRROD40': df_item_number.iloc[0, 26],
                'Item number_CRROD70': df_item_number.iloc[0, 27],
                'Item number_HEA100ESS275': df_item_number.iloc[0, 28],
                'Item number_HEA120ESS275': df_item_number.iloc[0, 29],
                'Item number_HEA140ESS275': df_item_number.iloc[0, 30],
                'Item number_HEA160ESS275': df_item_number.iloc[0, 31],
                'Item number_HEA160ESS355': df_item_number.iloc[0, 32],
                'Item number_HEA180ESS275': df_item_number.iloc[0, 33],
                'Item number_HEA200ESS275': df_item_number.iloc[0, 34],
                'Item number_HEA220ESS275': df_item_number.iloc[0, 35],
                'Item number_HEA240ESS275': df_item_number.iloc[0, 36],
                'Item number_HEA260ESS275': df_item_number.iloc[0, 37],
                'Item number_HEA280ESS275': df_item_number.iloc[0, 38],
                'Item number_HEA300ESS275': df_item_number.iloc[0, 39],
                'Item number_HEA400ESS275': df_item_number.iloc[0, 40],
                'Item number_HEA450ESS275': df_item_number.iloc[0, 41],
                'Item number_HEB140ESS275': df_item_number.iloc[0, 42],
                'Item number_HEB160ESS275': df_item_number.iloc[0, 43],
                'Item number_HEB200ESS275': df_item_number.iloc[0, 44],
                'Item number_HEB220ESS275': df_item_number.iloc[0, 45],
                'Item number_HEB240ESS275': df_item_number.iloc[0, 46],
                'Item number_HEB300ESS275': df_item_number.iloc[0, 47],
                'Item number_HEB400ESS275': df_item_number.iloc[0, 48],
                'Item number_HEB400ESS355': df_item_number.iloc[0, 49],
                'Item number_HRFL100/10TRS235': df_item_number.iloc[0, 50],
                'Item number_HRFL100/6TRS235': df_item_number.iloc[0, 51],
                'Item number_HRFL100/8TRS235': df_item_number.iloc[0, 52],
                'Item number_HRFL12/5TRS235': df_item_number.iloc[0, 53],
                'Item number_HRFL120/20ESS275': df_item_number.iloc[0, 54],
                'Item number_HRFL120/20ITS235': df_item_number.iloc[0, 55],
                'Item number_HRFL14/5TRS235': df_item_number.iloc[0, 56],
                'Item number_HRFL16/3TRS235': df_item_number.iloc[0, 57],
                'Item number_HRFL16/8TRS235': df_item_number.iloc[0, 58],
                'Item number_HRFL20/10TRS235': df_item_number.iloc[0, 59],
                'Item number_HRFL20/3TRS235': df_item_number.iloc[0, 60],
                'Item number_HRFL20/5TRS235': df_item_number.iloc[0, 61],
                'Item number_HRFL20/8TRS235': df_item_number.iloc[0, 62],
                'Item number_HRFL200/10ESS275': df_item_number.iloc[0, 63],
                'Item number_HRFL200/15ESS275': df_item_number.iloc[0, 64],
                'Item number_HRFL25/10TRS235': df_item_number.iloc[0, 65],
                'Item number_HRFL25/3TRS235': df_item_number.iloc[0, 66],
                'Item number_HRFL25/5TRS235': df_item_number.iloc[0, 67],
                'Item number_HRFL25/8TRS235': df_item_number.iloc[0, 68],
                'Item number_HRFL250/20ESS275': df_item_number.iloc[0, 69],
                'Item number_HRFL30/10TRS235': df_item_number.iloc[0, 70],
                'Item number_HRFL30/12TRS235': df_item_number.iloc[0, 71],
                'Item number_HRFL30/3TRS235': df_item_number.iloc[0, 72],
                'Item number_HRFL30/5TRS235': df_item_number.iloc[0, 73],
                'Item number_HRFL30/8TRS235': df_item_number.iloc[0, 74],
                'Item number_HRFL40/10TRS235': df_item_number.iloc[0, 75],
                'Item number_HRFL40/12TRS235': df_item_number.iloc[0, 76],
                'Item number_HRFL40/3TRS235': df_item_number.iloc[0, 77],
                'Item number_HRFL40/5TRS235': df_item_number.iloc[0, 78],
                'Item number_HRFL40/8TRS235': df_item_number.iloc[0, 79],
                'Item number_HRFL50/10TRS235': df_item_number.iloc[0, 80],
                'Item number_HRFL50/3TRS235': df_item_number.iloc[0, 81],
                'Item number_HRFL50/5TRS235': df_item_number.iloc[0, 82],
                'Item number_HRFL50/8TRS235': df_item_number.iloc[0, 83],
                'Item number_HRFL60/30ESS275': df_item_number.iloc[0, 84],
                'Item number_HRFL60/6TRS235': df_item_number.iloc[0, 85],
                'Item number_HRFL60/8TRS235': df_item_number.iloc[0, 86],
                'Item number_HRFL80/10TRS235': df_item_number.iloc[0, 87],
                'Item number_HRFL80/20ESS275': df_item_number.iloc[0, 88],
                'Item number_HRFL80/6TRS235': df_item_number.iloc[0, 89],
                'Item number_HRPL10CNS275': df_item_number.iloc[0, 90],
                'Item number_HRPL10CNS355': df_item_number.iloc[0, 91],
                'Item number_HRPL12CNS275': df_item_number.iloc[0, 92],
                'Item number_HRPL15CNS275': df_item_number.iloc[0, 93],
                'Item number_HRPL15CNS355': df_item_number.iloc[0, 94],
                'Item number_HRPL20CNS275': df_item_number.iloc[0, 95],
                'Item number_HRPL25CNS275': df_item_number.iloc[0, 96],
                'Item number_HRPL25CNS355JR': df_item_number.iloc[0, 97],
                'Item number_HRPL30CNS275': df_item_number.iloc[0, 98],
                'Item number_HRPL40CNS275': df_item_number.iloc[0, 99],
                'Item number_HRPL6CNS355JR': df_item_number.iloc[0, 100],
                'Item number_HRPL8CNS275JR': df_item_number.iloc[0, 101],
                'Item number_HRPL8CNS355JR': df_item_number.iloc[0, 102],
                'Item number_HRRB10TRS235': df_item_number.iloc[0, 103],
                'Item number_HRRB12TRS235': df_item_number.iloc[0, 104],
                'Item number_HRRB14TRS235': df_item_number.iloc[0, 105],
                'Item number_HRRB16TRS235': df_item_number.iloc[0, 106],
                'Item number_HRRB18TRS235': df_item_number.iloc[0, 107],
                'Item number_HRRB20TRS235': df_item_number.iloc[0, 108],
                'Item number_HRRB25TRS235': df_item_number.iloc[0, 109],
                'Item number_HRSQ10TRS235': df_item_number.iloc[0, 110],
                'Item number_HRSQ10UA': df_item_number.iloc[0, 111],
                'Item number_HRSQ12TRS235': df_item_number.iloc[0, 112],
                'Item number_HRSQ12UA': df_item_number.iloc[0, 113],
                'Item number_HRSQ14TRS235': df_item_number.iloc[0, 114],
                'Item number_HRSQ14UA': df_item_number.iloc[0, 115],
                'Item number_HRSQ16TRS235': df_item_number.iloc[0, 116],
                'Item number_HRSQ16UA': df_item_number.iloc[0, 117],
                'Item number_HRSQ20TRS235': df_item_number.iloc[0, 118],
                'Item number_HRSQ25TRS235': df_item_number.iloc[0, 119],
                'Item number_HRSQ30TRS235': df_item_number.iloc[0, 120],
                'Item number_HRSQ30TRS275JR': df_item_number.iloc[0, 121],
                'Item number_HRSQ40TRS275JR': df_item_number.iloc[0, 122],
                'Item number_HRSQ50TRS275JR': df_item_number.iloc[0, 123],
                'Item number_HRSQM11.5TR': df_item_number.iloc[0, 124],
                'Item number_HRSQM14TR': df_item_number.iloc[0, 125],
                'Item number_HRSQM16TRS235': df_item_number.iloc[0, 126],
                'Item number_IPE100TRS235': df_item_number.iloc[0, 127],
                'Item number_IPE100TRS275JR': df_item_number.iloc[0, 128],
                'Item number_IPE120TRS235': df_item_number.iloc[0, 129],
                'Item number_IPE120TRS275JR': df_item_number.iloc[0, 130],
                'Item number_IPE140TRS235': df_item_number.iloc[0, 131],
                'Item number_IPE140TRS275JR': df_item_number.iloc[0, 132],
                'Item number_IPE160TRS235': df_item_number.iloc[0, 133],
                'Item number_IPE160TRS275JR': df_item_number.iloc[0, 134],
                'Item number_IPE180ESS275': df_item_number.iloc[0, 135],
                'Item number_IPE180TRS275JR': df_item_number.iloc[0, 136],
                'Item number_IPE200TRS235': df_item_number.iloc[0, 137],
                'Item number_IPE200TRS275JR': df_item_number.iloc[0, 138],
                'Item number_IPE220ESS275': df_item_number.iloc[0, 139],
                'Item number_IPE240ESS275': df_item_number.iloc[0, 140],
                'Item number_IPE270ESS275': df_item_number.iloc[0, 141],
                'Item number_IPE300ESS275': df_item_number.iloc[0, 142],
                'Item number_IPE330ESS275': df_item_number.iloc[0, 143],
                'Item number_IPE360ESS275': df_item_number.iloc[0, 144],
                'Item number_IPE400ESS275': df_item_number.iloc[0, 145],
                'Item number_IPE450ESS275': df_item_number.iloc[0, 146],
                'Item number_IPE600ESS275': df_item_number.iloc[0, 147],
                'Item number_IPE80TRS235': df_item_number.iloc[0, 148],
                'Item number_IPEA100TRS275JR': df_item_number.iloc[0, 149],
                'Item number_IPEA120TRS275JR': df_item_number.iloc[0, 150],
                'Item number_IPEA140TRS275JR': df_item_number.iloc[0, 151],
                'Item number_IPEA160TRS275JR': df_item_number.iloc[0, 152],
                'Item number_IPEA220ESS275': df_item_number.iloc[0, 153],
                'Item number_IPEA240ESS275': df_item_number.iloc[0, 154],
                'Item number_IPEA270ESS275': df_item_number.iloc[0, 155],
                'Item number_IPEA300ESS275': df_item_number.iloc[0, 156],
                'Item number_IPEA360ESS275': df_item_number.iloc[0, 157],
                'Item number_IPEA400ESS275': df_item_number.iloc[0, 158],
                'Item number_IPEA450ESS275': df_item_number.iloc[0, 159],
                'Item number_TE30TRS235': df_item_number.iloc[0, 160],
                'Item number_TE35TRS235': df_item_number.iloc[0, 161],
                'Item number_UPN100TRS235': df_item_number.iloc[0, 162],
                'Item number_UPN120TRS235': df_item_number.iloc[0, 163],
                'Item number_UPN140TRS235': df_item_number.iloc[0, 164],
                'Item number_UPN160TRS235': df_item_number.iloc[0, 165],
                'Item number_UPN200TRS275JR': df_item_number.iloc[0, 166],
                'Item number_UPN240ESS275': df_item_number.iloc[0, 167],
                'Item number_UPN260ESS275': df_item_number.iloc[0, 168],
                'Item number_UPN300ESS275': df_item_number.iloc[0, 169],
                'Item number_UPN40TRS235': df_item_number.iloc[0, 170],
                'Item number_UPN50TRS235': df_item_number.iloc[0, 171],
                'Item number_UPN60TRS235': df_item_number.iloc[0, 172],
                'Item number_UPN65TRS235': df_item_number.iloc[0, 173],
                'Item number_UPN80TRS235': df_item_number.iloc[0, 174],
                
                'Shape_Flat Bars' : df_shape.iloc[0, 0],
                'Shape_HEA Beams' : df_shape.iloc[0, 1],
                'Shape_HEB Beam' : df_shape.iloc[0, 2],
                'Shape_IPE Beams' : df_shape.iloc[0, 3],
                'Shape_IPEA Beams' : df_shape.iloc[0, 4],
                'Shape_Round Bars' : df_shape.iloc[0, 5],
                'Shape_Square Bar' : df_shape.iloc[0, 6],
                'Shape_Square Bar Mdarrab' : df_shape.iloc[0, 7],
                'Shape_T Bar' : df_shape.iloc[0, 8],
                'Shape_UPN Beams' : df_shape.iloc[0, 9],

                'Origin_italy' : df_origin.iloc[0, 0],
                'Origin_lebanon' : df_origin.iloc[0, 1],
                'Origin_spain' : df_origin.iloc[0, 2],
                'Origin_turkey' : df_origin.iloc[0, 3],
                'Origin_ukraine' : df_origin.iloc[0, 4],

                      
            }
            

            features = pd.DataFrame(data,index = [0])
            #st.write(features)
            #st.write(crew_edit_raw.head(1))
            sales.drop(columns=['Quantity'], inplace=True)
            df = pd.concat([features,sales],axis=0)
            df = df.fillna(0)
            # Reads in saved classification model
            load_clf = pickle.load(open('best_rf_reg_sales.pkl', 'rb'))
 
            
            prediction = load_clf.predict(df) 
            
            # Extract the predicted price
            predicted_price = prediction[0]

            # Display the extracted predicted price
            st.write("")
            st.write("**Your Predicted Volume for Sales chosen the above features is:**")
            st.write(predicted_price)
  
if __name__ == "__main__":
    main()
