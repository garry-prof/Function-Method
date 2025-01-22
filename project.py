import streamlit as st
import sympy as sp

#Fanny Rorencia Ribowo - 160422005
#Nathan Garzya Santoso - 160422041
#Alexander Kent So - 160422057
#Antonius Kustiono Putra - 160422065
#Fransiscus Xaverius Petrus Jonathan Surhargo - 160422070

st.set_page_config(layout="wide")
st.header("Project Numerical Method")
st.subheader("Menentukan Akar Persamaan Menggunakan Metode Terbuka Newton Raphson")
input_fungsi = st.text_input("Memasukkan fungsi matematika Contoh:(misalnya: x**3 + 2*x + 1)")
input_x0 = st.number_input("Masukkan angka tebakan awal Contoh:(misalnya: 2)", min_value=0.001, step=0.001, format="%.3f")


options = ["|f(x)|", "|f(x)|=0", "Digit signifikan (%)"]
pilihan = st.selectbox("Pilih Kriteria Berhenti : ", options)

kriteria_berhenti = st.number_input("Tentukan syarat kriteria berhenti kurang dari : ", min_value=0.000001, step=0.000001, format="%.6f")

iterasi_max = st.number_input("Tentukan maximum iterasi : ", min_value = 1, step = 1)


def digit_signifikan(x_new,x_old):
    return abs(((x_new-x_old)/x_new)*100)

def xiplus1(xi,fxi,fdivxi):
    return(xi-(fxi/fdivxi))

def newton_raphson(fx, x0, imax, berhenti):
    var = sp.symbols('x')
    f = sp.simplify(fx)
    f_dif = sp.diff(f, var)
    
    hasil = []
    hasil.append(["Iterasi","xi","f(xi)","f'(xi)","|f(xi)|","|∈a|(%)"])

    x = x0
    for i in range(imax):
        x_old = x
        f_value = f.subs(var,x_old).evalf()
        f_dif_value = f_dif.subs(var,x_old).evalf()
        
        if f_dif_value == 0:
            hasil.append(["Error", "Turunan nol, metode gagal. Iterasi ke =", i+1])  # Tambahkan pesan error ke hasil
            return hasil
        
        x_new = xiplus1(x, f_value, f_dif_value)

        f_value_abs = abs(f_value)
        digitsignifikan = digit_signifikan(x_new, x_old)
        hasil.append([i+1, x_old, f_value, f_dif_value, f_value_abs, digitsignifikan])
        if(pilihan == "|f(x)|"):
            if(f_value_abs<float(berhenti)):
                return hasil
        elif(pilihan == "|f(x)|=0"):
            if(f_value_abs == 0):
                return hasil
        else:
            if(digitsignifikan<float(berhenti)):
                return hasil
        x = x_new
    return hasil

if st.button ("RUN"):
    imax = int(iterasi_max)
    fx = str(input_fungsi)
    x0 = float(input_x0)
    berhenti = float(kriteria_berhenti)
    hasil = newton_raphson(fx, x0, imax, berhenti)
    if isinstance(hasil, list) and isinstance(hasil[0], str):
        st.write(hasil[0])
    else:
        st.table(hasil)
