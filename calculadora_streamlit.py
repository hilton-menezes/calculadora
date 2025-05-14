import streamlit as st
from calculadora import soma, subtrai, multiplica, divide

st.set_page_config(page_title="Calculadora Simples", page_icon="🧮", layout="centered")
st.title("🧮 Calculadora Simples")
st.write("Insira dois números e escolha a operação desejada:")

num1 = st.number_input("Primeiro número", value=0.0, format="%f")
num2 = st.number_input("Segundo número", value=0.0, format="%f")

operacao = st.radio(
    "Operação",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

if st.button("Calcular"):
    if operacao == "Soma (+)":
        resultado = soma(num1, num2)
        st.success(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == "Subtração (-)":
        resultado = subtrai(num1, num2)
        st.success(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == "Multiplicação (*)":
        resultado = multiplica(num1, num2)
        st.success(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == "Divisão (/)":
        resultado = divide(num1, num2)
        if isinstance(resultado, str):
            st.error(resultado)
        else:
            st.success(f"Resultado: {num1} / {num2} = {resultado}") 