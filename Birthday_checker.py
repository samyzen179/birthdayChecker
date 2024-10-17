import streamlit as st
from datetime import datetime

st.header("BIRTHDAY CHECKER", divider= "rainbow")


st.markdown("#")

sidebar = st.sidebar

sidebar.title("About BIRTHDAY CHECKER")
sidebar.divider()
sidebar.write("BIRTHDAY CHECKER is a program that checks your birthday according to your input. It helps u feel good especially if you're celebrating your birthday today. It also reminds you of your next birthday(how many days left). It also tells those that their birthday have passed, their next birthday. Have fun as you check the days to your next birthday with BIRTHDAY CHECKER!!!")
st.write("Check your latest BIRTHDAY here")
col1, col2 = st.columns([5,1])

counter = 0

# with col1:
st.markdown("#### Welcome to :red[BIRTHDAY] CHECKER")
   

# with col2:
#     st.metric("Days to Birhthday", counter)



today = datetime.today()


user_name = st.text_input("Your name")
users_date = str(st.date_input("Enter your date of birth"))

converted_date = datetime.strptime(users_date, "%Y-%m-%d")

# new_date = converted_date.replace(year=today.year)

next_birthday = converted_date.replace(year=today.year)


if st.button("check"): 
    if user_name != "":
        if today.date() > next_birthday.date():
            next_birthday = next_birthday.replace(year = today.year + 1)
            days_to_birthday = (next_birthday - today).days
            counter = days_to_birthday
            st.markdown(f"Your bithday has passed😢 Your next birthday is in **{days_to_birthday}** days ")
            
        elif today.date() == next_birthday.date():
            st.success(f"Happy birthday {user_name}")
            st.balloons()
        
        else:
            days_to_future_birthday = (next_birthday - today).days
            st.markdown(f"Your next birthday is in **{days_to_future_birthday}** days ")
    else:
        st.warning("Please enter your name")



