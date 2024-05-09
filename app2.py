pip install matplotlib

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 500
plt.rcParams['font.family'] = 'times new roman'



# Sidebar inputs for variables
st.sidebar.header("Project 1")
A = st.sidebar.slider("Input Magnitue", min_value=-10.0, max_value=100.0, value=1.0, step=0.1)
b = st.sidebar.slider("Mass [kg]", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
c = st.sidebar.slider("Damping Ratio [N/s]", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
d = st.sidebar.slider("Spring Constant [N/m]", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

st.sidebar.header("Project 2")

def quadratic_function(x, b, c, d): # Function definition
    return b * x ** 2 + c * x + d

x_values = np.linspace(-10, 10, 400) # Generate data based on the quadratic function
y_values = quadratic_function(x_values, b, c, d)

def unit_step(x, A): # Function to generate unit step function with amplitude A
    return A * np.where(x >= 0, 1, 0)

x = np.linspace(-10, 10, 400) # Generate x values
y = unit_step(x, A) # Generate y values for the unit step function

# Plotting
fig1, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label=f'Unit Step Function (A = {A})', lw = 5, color = 'green')
ax.set_xlabel('time [s]', fontsize = 15)
ax.set_ylabel('x(t)', fontsize = 15)
ax.set_title('Input')
ax.legend(fontsize = 12, loc = 'upper left')
ax.grid(False)

# Plotting
fig2, ax = plt.subplots(figsize = (8,4))
ax.plot(x_values, y_values, label=f"y = {b}$x^{2}$ + {c}$x$ + {d}")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.legend()
ax.set_title("Quadratic Function")
ax.set_xlabel("x")
ax.set_ylabel("y")


st.title('신호 및 시스템 Term Project')
st.write('### 노재현 (기계공학부, 201921203)')

st.write('# Project 1')
st.write('## 1. 기계시스템 설계 및 선형 상미분 방정식 표현')
st.image("figure4.png", caption="Local Image", use_column_width=True)
st.markdown(r"""
    $$
    y = a \cdot x^2 + b \cdot x + c
    $$
""")

st.write('## 2. 입력 신호 및 출력 신호 그래프')
st.pyplot(fig1)
st.pyplot(fig2)