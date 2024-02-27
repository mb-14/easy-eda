# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report


LOGGER = get_logger(__name__)


def parse_file(uploaded_file):
    try:
        return pd.read_csv(uploaded_file)
    except Exception:
        pass
    try:
        return pd.read_excel(uploaded_file)
    except Exception:
        pass
    try:
        return pd.read_stata(uploaded_file)
    except Exception:
        pass
    st.error(f"Could not parse file ${uploaded_file.name}")


def run():
    st.set_page_config(
        page_title="Easy EDA",
        page_icon="🔍",
    )
    st.header("Easy EDA")
    st.markdown(
        "Perform automated EDA on tabular datasets using [ydata-profiling](https://github.com/ydataai/ydata-profiling)")

    uploaded_file = st.file_uploader("Upload a dataset", type=[
                                     "csv", "dta", "xlsx", "xls"])
    if uploaded_file is not None:
        data_frame = parse_file(uploaded_file)
        report = ProfileReport(data_frame, explorative=True)
        st_profile_report(report, navbar=True)


if __name__ == "__main__":
    run()
