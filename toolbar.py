import streamlit as st


def render_toolbar(key):
    col11, col12, col13 = st.columns(3)
    with col11:
        mode = st.radio('Mode', ('Drawing', 'Editing'), horizontal=True, label_visibility='collapsed', key=f'mode_{key}')
        st.button('**(\*)** Double-click on a box to remove it.', disabled=True)
        rec_clicked = st.button('Extract Text', type='primary', use_container_width=True)
    with col12:
        saved_format = st.radio('Type', ('csv', 'json'), horizontal=True, label_visibility='collapsed')
        st.download_button(
            label = f'📥 Export OCR result to data.{saved_format}',
            data = open(f'data/data.{saved_format}', encoding='utf-8'),
            file_name = f'data.{saved_format}',
            use_container_width = True, 
        )
        st.download_button(
            label = f'🖼️ Download patches',
            data = open('data/patches.zip', 'rb'),
            file_name = 'patches.zip',
            use_container_width = True, 
        )
    with col13: 
        st.checkbox('Dark mode')
        if st.button('🧹 Clear cache of computations', use_container_width=True):
            st.cache_data.clear()
        if st.button("🧹 Clear model resources", use_container_width=True):
            st.cache_resource.clear()
    return mode, rec_clicked