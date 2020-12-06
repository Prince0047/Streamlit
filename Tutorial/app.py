import streamlit as st

# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is Header")
st.subheader("This is Subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successfull !!!")

st.info("Information")

st.warning("This is warning")

st.error("This is some error !!!")

st.exception("NameError('name three not defined')")

# Get Help Info About Python
st.help(range)

# Writting Text
st.write("Text with write here !")

st.write(range(10))


# Images
from PIL import Image
img = Image.open("example.jpg")
st.image(img , width=500 , caption="Iron Man")


# Video
vid_file = open("vid2.mp4" , "rb").read()
st.video(vid_file)

# Audio 
# audio_file = open("ex_audio").read()
# st.audio(audio_file.format='audio/mp3')

# Widget
# Checkbox
if st.checkbox("show/hide"):
   st.text("Showing or hiding widget")
   if st.checkbox("even/odd"):
   	  st.text("Showing Even")


# Radio Buttons
status = st.radio("What is your status:" , ("Active", "Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive , pls Activate:")



# SelectBox 
occupation = st.selectbox("Your occupation :" , ["Programmer","Gamer","Lawer"])
st.write("You have selected : ",occupation)


#Multiselect
languages = st.multiselect("Languages : " , ["Sankrit","Hindi","English"])
st.write("You have selectd : " , len(languages))


# Slider
level = st.slider("What is your level : ", 1,10)


# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is cool")
else:
	st.text("Streamlit is boring")



# Text Input
firstname = st.text_input("Enter your Firstname : ", "Type Here...")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)


# Text Area
message = st.text_area("Enter your Message : ", "Type Here...")
if st.button("Submit2"):
	result = message.title()
	st.success(result)


# Date Input
import datetime
today = st.date_input("Today is : ",datetime.datetime.now())

# Time 
the_time = st.time_input("The time is : ", datetime.time())



# Displaying JSON
st.text("Display JSON")
st.json({'name':"Sonu",'Gender':"Male"})


# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")


with st.echo():
	# This is also show as comment

	import pandas as pd 
	df = pd.DataFrame()

# Prgress Bar
import time
my_bar = st.progress(0)
for p in range(10):
	my_bar.progress(p+1)


# Spinner
with st.spinner("Waiting ..."):
	time.sleep(3)
st.success("Finished:")


# Balloons
st.balloons()


# Side Bars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")


# Functions
@st.cache
def run_fxn():
	return range(100)

st.write(run_fxn())
