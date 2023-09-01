import streamlit as st
import os
import json
import datetime
from utils import json_operation
import awesome_streamlit as ast

def write():
    init()
    st.info('标题和行业每份研报都一样，注：分析一份新研报时记得修改')
    title = st.text_input('Title (研报文件名)', st.session_state['collection_title'])
    field = st.text_input('Field (行业名（参考申万）)', st.session_state['collection_field'])
    st.info('以下字段每次都会清空')
    answer = st.text_area('Answer (研报摘要)', st.session_state['collection_answer'], key=12)
    question = st.text_area('Question (研报正文)', st.session_state['collection_question'])
    instruction = st.text_area('Instruction (提问prompt)', st.session_state['collection_instruction'])
    reference = st.text_area('Reference (来源出处)', st.session_state['collection_reference'])
    submit_button = st.button('保存并提交数据', help='提交保存数据（请确认数据无误后提交）')
    if submit_button:
        refresh()
        json_operation.save_json(os.path.join("data", "qa"),
                                 title, field, answer, question,
                                 instruction, reference)
        st.success("保存成功！")

def refresh():
    '''
    提交之后重新刷新页面
    '''
    st.session_state['collection_reference'] = 'Page-'
    st.session_state['collection_question'] = ''
    st.session_state['collection_answer'] = ''
    st.session_state['collection_instruction'] = '请你'

def init():
    '''
    初始化缓存
    '''
    if 'collection_title' not in st.session_state:
        st.session_state['collection_title'] = ''
    if 'collection_field' not in st.session_state:
        st.session_state['collection_field'] = ''
    if 'collection_reference' not in st.session_state:
        st.session_state['collection_reference'] = 'Page-'
    if 'collection_question' not in st.session_state:
        st.session_state['collection_question'] = ''
    if 'collection_answer' not in st.session_state:
        st.session_state['collection_answer'] = ''
    if 'collection_instruction' not in st.session_state:
        st.session_state['collection_instruction'] = '请你'




