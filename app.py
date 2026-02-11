import streamlit as st

st.title("Тест по География")

st.write("Коя е столицата на Япония?")
user_answer1=st.radio("Вашия отговор:"["Токио","Осака","Хипошима","Франция"])
if st.button("Провери отговор 1"):
                      if user_answer 1=="Токио":st.succes("Верен отговор")
                      else:st.error("Столицата на япония е Токио")


