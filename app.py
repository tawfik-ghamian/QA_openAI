import time
import json

import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from dotenv import load_dotenv

from prompts import (PROMPTS, OUTPUT_PARSERS, HEADINGS,
                     MULTIPLES_TBL_PROMPT, BARRIERS_TO_ENTRY_PROMPT, PRODUCT_PROMPT, MAJOR_PLAYER_PROMPT,
                     POP_RACE_ETHN_PROMPT,POP_EDU_ATTAINMENT_PROMPT,POP_RELSHIP_HH_PROMPT,POP_MATERIAL_PROMPT,POP_GENDER_PROMPT,
                     DEMOGRAPHIC_OVERVIEW_PROMPT,HH_SIZE_PROMPT,CIVIL_POP_PROMPT,HH_INCOME_PROMPT,LANGUAGE_SPOKEN_PROMPT,
                     PERSONAL_INCOME_SUMMARY_PROMPT,HH_SUMMARY_PROMPT,POP_AGE_SUMMARY_PROMPT,POP_SUMMARY_PROMPT,CIVI_EMP_POP_IND_PROMPT,
                     CONSUMER_SPEND_INFO_PROMPT,IND_PERFORM_PROMPT,IND_SUMMARY_PROMPT,WAGES_PROMPT)
from chains import get_chains_results, get_chain_result
from gpt_params import MODELS, MAX_TOKEN
from enums import FN
import formatters


# Environment Variables
load_dotenv()


# === Helpers ===
def to_formatted_string(input_str, formatter):
    return formatter(json.loads(input_str))


def get_chain_execution_result(chain, input_vars, multi=False):
    with st.spinner("Wait for it ..."):
        start_time = time.perf_counter()
        with get_openai_callback() as cb:
            result = get_chain_result(chain, input_vars) if not multi else get_chains_results(chain, input_vars)
        elapsed_time = time.perf_counter() - start_time
    return result, elapsed_time, cb


def show_chain_execution_info(elapsed_time, cb):
    st.success(f"Executed in {elapsed_time:.2f} seconds.", icon="✅")
    st.info(
        f"""
        Total Tokens: {cb.total_tokens}\n
        Prompt Tokens: {cb.prompt_tokens}\n
        Completion Tokens: {cb.completion_tokens}\n
        Total Cost: ${cb.total_cost:.4f}
        """,
        icon="ℹ️"
    )


# === APP ===
st.set_page_config(page_title="Industry Info", page_icon=":robot_face:")

# ** Configurations Sidebar **
with st.sidebar:
    llm_model = MODELS[st.radio("Model", list(MODELS.keys()))]
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, step=0.1, value=1.0)
    max_tokens = st.slider("Max Tokens", min_value=1, max_value=MAX_TOKEN[llm_model], step=1, value=2000)

# Large Language Model (LLM)
llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_tokens)

# Chains
CHAINS = [LLMChain(llm=llm, prompt=prompt, verbose=False) for prompt in PROMPTS]
MULTIPLE_TBL_CHAIN = LLMChain(llm=llm, prompt=MULTIPLES_TBL_PROMPT, verbose=True)
BARRIERS_TO_ENTRY_CHAIN = LLMChain(llm=llm, prompt=BARRIERS_TO_ENTRY_PROMPT, verbose=True)
PRODUCT_CHAIN = LLMChain(llm=llm, prompt=PRODUCT_PROMPT, verbose=True)
MAJOR_PLAYER_CHAIN = LLMChain(llm=llm, prompt=MAJOR_PLAYER_PROMPT, verbose=True)


POP_RACE_ETHN_CHAIN = LLMChain(llm=llm, prompt=POP_RACE_ETHN_PROMPT, verbose=True)
POP_MATERIAL_CHAIN = LLMChain(llm=llm, prompt=POP_MATERIAL_PROMPT, verbose=True)
POP_RELSHIP_HH_CHAIN = LLMChain(llm=llm, prompt=POP_RELSHIP_HH_PROMPT, verbose=True)
POP_GENDER_CHAIN = LLMChain(llm=llm, prompt=POP_GENDER_PROMPT, verbose=True)
POP_EDU_ATTAINMENT_CHAIN = LLMChain(llm=llm, prompt=POP_EDU_ATTAINMENT_PROMPT, verbose=True)
DEMOGRAPHIC_OVERVIEW_CHAIN = LLMChain(llm=llm, prompt=DEMOGRAPHIC_OVERVIEW_PROMPT, verbose=True)
HH_SIZE_CHAIN = LLMChain(llm=llm, prompt=HH_SIZE_PROMPT, verbose=True)
CIVIL_POP_CHAIN = LLMChain(llm=llm, prompt=CIVIL_POP_PROMPT, verbose=True)
HH_INCOME_CHAIN = LLMChain(llm=llm, prompt=HH_INCOME_PROMPT, verbose=True)
# GENERAL_CHAIN = LLMChain(llm=llm, prompt=GENERAL_PROMPT, verbose=True)
POP_SUMMARY_CHAIN = LLMChain(llm=llm, prompt=POP_SUMMARY_PROMPT, verbose=True)
HH_SUMMARY_CHAIN = LLMChain(llm=llm, prompt=HH_SUMMARY_PROMPT, verbose=True)
POP_AGE_CHAIN = LLMChain(llm=llm, prompt=POP_AGE_SUMMARY_PROMPT, verbose=True)
PERSONAL_INCOME_SUMMARY_CHAIN = LLMChain(llm=llm, prompt=PERSONAL_INCOME_SUMMARY_PROMPT, verbose=True)
LANGUAGE_SPOKEN_CHAIN = LLMChain(llm=llm, prompt=LANGUAGE_SPOKEN_PROMPT, verbose=True)
CIVI_EMP_POP_IND_CHAIN = LLMChain(llm=llm, prompt=CIVI_EMP_POP_IND_PROMPT, verbose=True)
CONSUMER_SPEND_INFO_CHAIN = LLMChain(llm=llm, prompt=CONSUMER_SPEND_INFO_PROMPT, verbose=True)
IND_PERFORM_CHAIN = LLMChain(llm=llm, prompt=IND_PERFORM_PROMPT, verbose=True)
IND_SUMMARY_CHAIN = LLMChain(llm=llm, prompt=IND_SUMMARY_PROMPT, verbose=True)
WAGES_CHAIN = LLMChain(llm=llm, prompt=WAGES_PROMPT, verbose=True)

# ** Main **
st.header("Powered by :robot_face:")
st.write("")
selected_fn = st.selectbox(label="Select a function", options=[fn.value for fn in FN])
st.divider()

# == Function 1 ==
if selected_fn == FN.FN1.value:

    st.markdown("Function 1: The AI will give you some information about the entered industry")

    input_text = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=25,
        label_visibility="collapsed"
    )

    if input_text:

        results, exec_time, tkn_cb = get_chain_execution_result(CHAINS, [{"industry_title": input_text} for i in
                                                                         range(len(CHAINS))], multi=True)

        results = [OUTPUT_PARSERS[r].parse(result) if OUTPUT_PARSERS[r] is not None else result
                   for r, result in enumerate(results)]

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        for r, result in enumerate(results):
            with st.expander(f"##### {HEADINGS[r]}"):
                if isinstance(result, str):
                    st.markdown(result)
                elif isinstance(result, list):
                    for item in result:
                        st.markdown(f"- {item.capitalize()}")

# == Function 2 ==
if selected_fn == FN.FN2.value:

    st.markdown("Function 2: The AI will explain the entered multiples table of an industry")

    input_text = st.text_area(
        label="Industry Multiples Table",
        placeholder="Enter a multiples table object",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(MULTIPLE_TBL_CHAIN, {
            "multiples_table": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)


# == Function 4 ==
if selected_fn == FN.FN4.value:

    st.markdown("Function 4: The AI will explain the entered barriers to entry checklist of an industry")
    
    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=25,
        label_visibility="collapsed"
    )

    input_text = st.text_area(
        label="Barriers To Entry Checklist",
        placeholder="Enter a barriers to entry checklist object",
        label_visibility="collapsed"
    )


    if input_text and industry_title :

        result, exec_time, tkn_cb = get_chain_execution_result(BARRIERS_TO_ENTRY_CHAIN, {
            "barriers_to_entry": input_text,
            "industry_title": industry_title
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 6 ==
if selected_fn == FN.FN6.value:

    st.markdown("Function 6: The AI will explain the entered Products and services of an industry")

    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=25,
        label_visibility="collapsed"
    )
    
    input_text = st.text_area(
        label="Products and Services of an industry",
        placeholder="Enter the products and services of an industry",
        label_visibility="collapsed"
    )

    if input_text and industry_title:

        result, exec_time, tkn_cb = get_chain_execution_result(PRODUCT_CHAIN, {
            "products_and_services": input_text,
            "industry_title": industry_title
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 7 ==
if selected_fn == FN.FN7.value:

    st.markdown("Function 7: The AI will explain the entered Major Players of an industry")

    input_text = st.text_area(
        label="Major Players of an industry",
        placeholder="Enter the Major Players of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(MAJOR_PLAYER_CHAIN, {
            "major_players": input_text,})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

#////////////////////////////////for here ////////////////////

#/////////////// Demographic ///////////////////

# == Function 13 ==
if selected_fn == FN.FN13.value:

    st.markdown("Function 13: The AI will explain the entered population by race ethnicity card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_RACE_ETHN_CHAIN, {
            "obj1": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 14 ==
if selected_fn == FN.FN14.value:

    st.markdown("Function 14: The AI will explain the entered population by marital status card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_MATERIAL_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 15 ==
if selected_fn == FN.FN15.value:

    st.markdown("Function 15: The AI will explain the entered population by relationship and household card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_RELSHIP_HH_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 16 ==
if selected_fn == FN.FN16.value:

    st.markdown("Function 16: The AI will explain the entered population by gender card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_GENDER_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 17 ==
if selected_fn == FN.FN17.value:

    st.markdown("Function 17: The AI will explain the entered population by educational attainment status card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_EDU_ATTAINMENT_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 18 ==
if selected_fn == FN.FN18.value:

    st.markdown("Function 18: The AI will explain the entered demographic overview card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(DEMOGRAPHIC_OVERVIEW_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 19 ==
if selected_fn == FN.FN19.value:

    st.markdown("Function 19: The AI will explain the entered house hold by size chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(HH_SIZE_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 20 ==
if selected_fn == FN.FN20.value:

    st.markdown("Function 20: The AI will explain the entered civilian population card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(CIVIL_POP_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 21 ==
if selected_fn == FN.FN21.value:

    st.markdown("Function 21: The AI will explain the entered household income card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(HH_INCOME_CHAIN, {
            "obj": input_text,
            })

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 22 ==
# if selected_fn == FN.FN22.value:

#     st.markdown("Function 22: The AI will explain the entered general card chart of an industry")

#     input_text = st.text_area(
#         label=" chart values",
#         placeholder="Enter the chart values ",
#         label_visibility="collapsed"
#     )

#     if input_text:
        
#         result, exec_time, tkn_cb = get_chain_execution_result(GENERAL_CHAIN, {"obj": input_text})

#         st.markdown(f"#### Here are your results")

#         show_chain_execution_info(exec_time, tkn_cb)

#         with st.expander("##### Explanation"):
#             st.markdown(result)

# == Function 23 ==
if selected_fn == FN.FN23.value:

    st.markdown("Function 23: The AI will explain the entered Population Summary chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_SUMMARY_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 24 ==
if selected_fn == FN.FN24.value:

    st.markdown("Function 24: The AI will explain the entered Population by Age Summary chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(POP_AGE_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 25 ==
if selected_fn == FN.FN25.value:

    st.markdown("Function 25: The AI will explain the entered House Hold Summary chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(HH_SUMMARY_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 26 ==
if selected_fn == FN.FN26.value:

    st.markdown("Function 26: The AI will explain the entered Personal Income Summary chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(PERSONAL_INCOME_SUMMARY_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 27 ==
if selected_fn == FN.FN27.value:

    st.markdown("Function 27: The AI will explain the entered Language Spoken chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(LANGUAGE_SPOKEN_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 28 ==
if selected_fn == FN.FN28.value:

    st.markdown("Function 28: The AI will explain the entered Civilian Employee population Industry card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(CIVI_EMP_POP_IND_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 29 ==
if selected_fn == FN.FN29.value:

    st.markdown("Function 29: The AI will explain the entered Consumer Spend Information card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(CONSUMER_SPEND_INFO_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 30 ==
if selected_fn == FN.FN30.value:

    st.markdown("Function 30: The AI will explain the entered Industry Perform card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(IND_PERFORM_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 31 ==
if selected_fn == FN.FN31.value:

    st.markdown("Function 31: The AI will explain the entered Consumer Spend Information card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(IND_SUMMARY_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 32 ==
if selected_fn == FN.FN32.value:

    st.markdown("Function 32: The AI will explain the entered Wages card chart of an industry")

    input_text = st.text_area(
        label=" chart values",
        placeholder="Enter the chart values ",
        label_visibility="collapsed"
    )

    if input_text:
        
        result, exec_time, tkn_cb = get_chain_execution_result(WAGES_CHAIN, {"obj": input_text})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

