import streamlit as st
import csv

# Sidebar Logo
logo_image = "logo.jpg"  # Ruta de la imagen del logotipo
st.sidebar.image(logo_image, use_column_width=True)

def enter_data(firstname, lastname, title, age, nationality, education, registration_status, numcourses, numsemesters):
    """
    Ingresa los datos del usuario.

    Args:
        firstname (str): Nombre del usuario.
        lastname (str): Apellidos del usuario.
        title (str): Título del usuario.
        age (int): Edad del usuario.
        nationality (str): Continente de origen del usuario.
        education (str): Nivel educativo del usuario.
        registration_status (str): Estado de registro del usuario.
        numcourses (int): Número de cursos completados por el usuario.
        numsemesters (int): Número de semestres completados por el usuario.
    """
    accepted = st.checkbox("Acepto los términos y condiciones")

    if accepted:
        if firstname and lastname:
            if st.button("Ingresar Datos"):
                # Guardar los datos en un archivo CSV
                data = [title, firstname, lastname, age, nationality, education, registration_status, numcourses, numsemesters]
                save_data(data)

                st.write("Datos guardados correctamente.")
                st.write("---------------------------------------------")
        else:
            st.warning("Nombre y Apellidos son requeridos.")
    else:
        st.warning("No ha aceptado los términos y condiciones")

def save_data(data):
    """
    Guarda los datos en un archivo CSV.

    Args:
        data (list): Lista con los datos a guardar.
    """
    with open('registros.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Sidebar Menu
st.sidebar.title("Menú")
selected_menu = st.sidebar.radio("Seleccionar opción", ["Información de usuario", "Solicitud de inscripción"])

# User Info Form
if selected_menu == "Información de usuario":
    st.subheader("Informacion de usuario")
    firstname = st.text_input("Nombre")
    lastname = st.text_input("Apellidos")
    title = st.selectbox("Titulo Académico", ["", "Sr.", "Srita.", "Sra."])
    age = st.number_input("Edad", min_value=18, max_value=110)
    nationality = st.selectbox("Continente", ["Africa", "Antartida", "Europa", "Norteamerica", "Sudamerica", "Oceania"])
    education = st.selectbox("Nivel educativo", ["Educación Superior", "Universitario", "Ciclo Formativo", "Máster Profesional"])
    comentario = st.text_input("Comentario Breve")

    # Validar la longitud del comentario
    if len(comentario) > 120:
        st.warning("El comentario no puede exceder los 120 caracteres.")

    # Course Info
    st.subheader("Informacion de cursos")
    registration_status = st.radio("Estado de registro", ["Registrado", "No registrado"], index=1)
    numcourses = st.number_input("# Cursos completados", min_value=0)
    numsemesters = st.number_input("# Semestres completados", min_value=0)

    # Button

    enter_data(firstname, lastname, title, age, nationality, education, registration_status, numcourses, numsemesters)

# Inscription Request Form
elif selected_menu == "Solicitud de inscripción":
    st.subheader("Solicitud de inscripción")
    # Agrega los campos y la lógica correspondiente para la solicitud de inscripción
