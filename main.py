"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
from resource import about,index,ranklist,resources,vision,data_collection,home,mark
ast.core.services.other.set_logging_format()

PAGES = {
    # "Home": home,
    # "Resources": resources,
    # "Gallery": index,
    # "Vision": vision,
    # "About": about,
    "数据收集": data_collection,
    "数据审核": mark,
    "LRHF": ranklist
}


def main():
    #
    # st.set_page_config(
    # page_title="Rank List Labeler",
    # page_icon='📌',
    # layout="wide"
    # )

    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    st.sidebar.title("Contribute")
    st.sidebar.info('waiting ')
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by SZRI."""
    )


if __name__ == "__main__":
    main()