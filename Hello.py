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
import matplotlib.pyplot as plt
import numpy as np
import csv

LOGGER = get_logger(__name__)


def getGraph():
    try:
        X = []
        Y = []
        Y2 = []
        with open('growth.csv', 'r') as datafile:
            plotting = csv.reader(datafile, delimiter=';')

            for ROWS in plotting:
                X.append(float(ROWS[0]))
                Y.append(float(ROWS[1].replace(',','.')))
                Y2.append(float(ROWS[2].replace(',','.')))
        plt.bar(X,Y,align='edge',color='#0088cc')
        plt.bar(X,Y2,align='edge',color='#686e7a') 
        plt.xticks(np.arange(1,19,1))
        plt.title('График прироста цен по месяцам')
        plt.xlabel('Месяц')
        plt.ylabel('Цена')
        return plt
    except Exception:
        return {"message":"error in generating plot"}
    
def getInfo():
    getGraph().savefig('growth.png')
    templates={"message":"generated succesfully"}
    return templates

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    getInfo()
    st.image("growth.png")


if __name__ == "__main__":
    run()
