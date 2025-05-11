import streamlit as st

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def main():
    st.title("BMI Calculator")
    
    st.write("Calculate your Body Mass Index (BMI)")
    
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height_ft = st.number_input("Enter your height (feet):", min_value=1.0, format="%.2f")
    height_in = st.number_input("Enter your height (inches):", min_value=0.0, format="%.2f")
    
    height_m = (height_ft * 0.3048) + (height_in * 0.0254)  # Convert feet and inches to meters
    
    if st.button("Calculate BMI"):
        if height_m > 0:
            bmi = calculate_bmi(weight, height_m)
            st.success(f"Your BMI is {bmi}")
            
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Height must be greater than zero.")

if __name__ == "__main__":
    main()

