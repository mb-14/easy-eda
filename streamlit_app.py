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
import magic


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Quick EDA",
        page_icon="🔍",
    )
    st.text("A simple EDA tool for tabular data")

    uploaded_file = st.file_uploader("Choose a data file", type=["csv", "dta", "xlsx", "xls"])
    if uploaded_file is not None:
      file_type = magic.from_buffer(uploaded_file.read(1024), mime=True)
      st.write(file_type)
      # Can be used wherever a "file-like" object is accepted:
      dataframe = pd.read_csv(uploaded_file)
      
      report = ProfileReport(dataframe)

      st_profile_report(report, navbar=True)




if __name__ == "__main__":
    run()
