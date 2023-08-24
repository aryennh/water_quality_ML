import streamlit as st

# ph = 0
pH = st.number_input('Insert a pH value (0-14)')
if pH <8.5 and pH > 7 : pH = 100
elif pH <8.6 and pH > 8.5 or 6.9>=pH and 6.8<=pH: pH = 80
elif  pH <8.8 and pH > 8.6 : pH = 60
elif pH <9 and pH > 8.8  : pH = 40
else : 0

ndo = st.number_input("Insert value for DO")
if ndo >= 6 : ndo =100
elif ndo>=5.1 and ndo<=6 : ndo = 80
elif ndo<=5 and ndo>=4.1 : ndo = 60
elif ndo>=3 and ndo<=4 : ndo = 40
else: ndo = 0


nco = st.number_input("Insert value for Coliform")
if nco >= 0 and nco<=5  : nco =100
elif nco>=5 and nco<=50 : ndo = 80
elif nco<=500 and nco>=50 : ndo = 60
elif nco>=500 and nco<=1000 : ndo = 40
else: nco =0


nbdo = st.number_input('Insert value for BO')
if nbdo >= 0and nbdo<=3  : nco =100
elif nbdo>=3 and nbdo<=6 : ndo = 80
elif nbdo<=80 and nbdo>=6 : ndo = 60
elif nbdo>=80 and nbdo<=125 : ndo = 40
else: nbdo =0



nec = st.number_input("Insert value for Conductivity")
if nec >= 0 and nec<=75  : nco =100
elif nec>=75 and nec<=150 : ndo = 80
elif nec<=225 and nec>=150 : ndo = 60
elif nec>=225 and nec<=300 : ndo = 40
else: nec =0



nna = st.number_input("Insert value for Nitrate values ")

if nna  >= 0 and nna <=20  : nco =100
elif nna >=20 and nna<=50 : ndo = 80
elif nna <=100 and nna >=50 : ndo = 60
elif nna >=100 and nna <=200 : ndo = 40
else: nna = 0


wqi = pH *0.56 + ndo*0.281 + nbdo*0.234 + nec*0.09 + nna*0.28 + nco*0.281


if wqi < 40 :
    st.write("The WQI value is ", wqi)
    st.write("The water quality is very poor")
elif wqi > 40 and wqi < 60 :
    st.write("The WQI value is ", wqi)
    st.write("The water quality is Poor")
elif wqi > 60 and wqi < 80 :
    st.write("The WQI value is ", wqi)
    st.write("The water quality is Good")
elif wqi > 80 and wqi < 90 :
    st.write("The WQI value is ", wqi)
    st.write("The water quality is suitable")
elif wqi > 90 :
    st.write("The WQI value is ", wqi)
    st.write("The water quality is Potable")


