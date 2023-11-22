# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from asyncore import write
import streamlit as st
from streamlit.logger import get_logger
from search_engine.searche_engine import df_ordenanza,query_search_engine
from pdf2image import convert_from_path
from agent_ai.agent_ai import query_function


LOGGER = get_logger(__name__)

def read_pdf(file_path):
    images = convert_from_path(file_path)
    return images

def chat_bot(ordenanza):
    st.session_state.messages = []

    # React to user input
    if prompt := st.chat_input("Que quieres saber de esta ordenanza?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response_msg = query_function(ordenanza,prompt)
        response = f"Gunther: {response_msg}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def dump_pdf(nro_ordenanza):
    if "dict_ordenanza" not in st.session_state:
        st.session_state.dict_ordenanza = {}
        st.session_state.dict_ordenanza[nro_ordenanza] = read_pdf(f"./ordenanzas/ORD_{nro_ordenanza}.pdf")
        pdf_images =  st.session_state.dict_ordenanza[nro_ordenanza]
    else:
        if nro_ordenanza in st.session_state.dict_ordenanza:
            pdf_images = st.session_state.dict_ordenanza[nro_ordenanza]
        else:
            st.session_state.dict_ordenanza[nro_ordenanza] = read_pdf(f"./ordenanzas/ORD_{nro_ordenanza}.pdf")
            pdf_images =  st.session_state.dict_ordenanza[nro_ordenanza]
    return pdf_images        


def run():
    st.set_page_config(
        page_title="Demo Municipalidad de Córdoba",
        page_icon="👋",
    )

    st.write("# Bienvenidos a la Demo de la Municipalidad! 👋")

    nro_ordenanza = st.sidebar.text_input("Ingrese el número de ordenanza que está buscando")
    string_query = st.sidebar.text_input("Ingrese el tema de lo que está buscando?")

    # if st.sidebar.button("Buscar Ordenanza"):
    # Llamada a la función cuando se presiona el botón
    if nro_ordenanza == "" and string_query == "":
        st.error("Ingrese un número de ordenanza o el tema de lo que está buscando")
    elif nro_ordenanza:
        # if "ordenanza" not in st.session_state:
        #     df_ordenanza = nro_ordenanza

        df_ordenanza_astype = df_ordenanza.copy()
        df_ordenanza_astype=df_ordenanza_astype[df_ordenanza_astype["nro_ordenanza"] == nro_ordenanza]
        if df_ordenanza_astype.empty:
            st.error("Ese número de ordenanza no se encuentra cargado en la base de datos")
        else:
            # pdf_images = dump_pdf(nro_ordenanza)
            with st.container():
                    
                with st.expander(f"ORDENANZA {nro_ordenanza}"):
                    for page_num, image in enumerate(pdf_images, start=1):
                        st.image(image, caption=f"Página {page_num}", use_column_width=True)

                chat_bot(nro_ordenanza)
                
    elif string_query:
        results = query_search_engine(string_query)
        list_ord=[]
        dict_ord = dict()
        for ord in results:
            key_nro_affair = f"{ord[1]} - {ord[3]}"
            list_ord.append(key_nro_affair)
            dict_ord[key_nro_affair] = ord[1]
        selected_ord = st.radio("",options=list_ord)
        nro_ordenanza = dict_ord[selected_ord]

        if selected_ord:
            # pdf_images = dump_pdf(nro_ordenanza)
            with st.container():
                    
                with st.expander(f"ORDENANZA {nro_ordenanza}"):
                    for page_num, image in enumerate(pdf_images, start=1):
                        st.image(image, caption=f"Página {page_num}", use_column_width=True)

            chat_bot(nro_ordenanza)


if __name__ == "__main__":
    run()
