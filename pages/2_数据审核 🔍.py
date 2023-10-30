import streamlit as st
import os
from utils import json_operation
click_flag = False
def reload_session(json_data:dict, cur_file):
    for k,v in json_data.items():
        st.session_state[k] = v
    st.session_state['cur_file'] = cur_file
def main():
    global click_flag
    # 指定文件夹路径
    read_path = os.path.join("data", "qa")
    yes_save_path = os.path.join("data", "checked_qa")
    no_save_path = os.path.join("data", "unchecked_qa")
    # 获取文件夹中所有文件名
    json_files = [file for file in os.listdir(read_path) if file.endswith('.json')]
    random_button = st.button('获得打标数据', help='获得一份打标数据')
    if not json_files or len(json_files) == 0:
        st.warning('文件已经全部处理完成！')
    elif random_button:
        first_json_file_path = os.path.join(read_path, json_files[0])
        json_data = json_operation.read_json(first_json_file_path)
        reload_session(json_data, first_json_file_path)
        click_flag = True
    if click_flag:
        title = st.text_input('Title (研报文件名)', st.session_state['title'], disabled=True)
        field = st.text_input('Field (行业名（参考申万）)', st.session_state['field'], disabled=True)
        answer = st.text_area('Answer (研报摘要)', st.session_state['answer'], disabled=True)
        question = st.text_area('Question (研报正文)', st.session_state['question'], disabled=True)
        instruction = st.text_area('Instruction (提问prompt)', st.session_state['instruction'], disabled=True)
        reference = st.text_area('Reference (来源出处)', st.session_state['reference'], disabled=True)
        satisfied_button = st.radio('数据是否合格', ('是', '否'))
        submit_button = st.button('提交')
        if submit_button:
            save_path = yes_save_path if satisfied_button == '是' else no_save_path
            print("saving...."+save_path)
            json_operation.save_json(save_path,
                                     title, field, answer, question,
                                     instruction, reference)
            json_operation.delete_json(st.session_state['cur_file'])
            st.success('打标成功！')
            click_flag = False

if "shared" not in st.session_state:
    st.error("请在Home页输入邮箱")
elif st.session_state.shared:
    main()
else:
    st.error("邮箱未激活或已过期")