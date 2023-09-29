import time
import json

import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from dotenv import load_dotenv

from prompts import (PROMPTS, OUTPUT_PARSERS, HEADINGS,
                     MULTIPLES_TBL_PROMPT, RISK_TBL_PROMPT, BARRIERS_TO_ENTRY_PROMPT, 
                     MAIN_ACTIVITY_PROMPT, PRODUCT_PROMPT, MAJOR_PLAER_PROMPT, 
                     DEFINITION_PROMPT, REVENUE_CARD_PROMPT, PROFIT_CARD_PROMPT, PROFIT_MARGIN_CARD_PROMPT, ENTERPRISES_CARD_PROMPT)
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
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, step=0.1, value=0.0)
    max_tokens = st.slider("Max Tokens", min_value=1, max_value=MAX_TOKEN[llm_model], step=1, value=2000)

# Large Language Model (LLM)
llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_tokens)

# Chains
CHAINS = [LLMChain(llm=llm, prompt=prompt, verbose=False) for prompt in PROMPTS]
MULTIPLE_TBL_CHAIN = LLMChain(llm=llm, prompt=MULTIPLES_TBL_PROMPT, verbose=True)
RISK_TBL_CHAIN = LLMChain(llm=llm, prompt=RISK_TBL_PROMPT, verbose=True)
BARRIERS_TO_ENTRY_CHAIN = LLMChain(llm=llm, prompt=BARRIERS_TO_ENTRY_PROMPT, verbose=True)
MAIN_ACTIVITY_CHAIN = LLMChain(llm=llm, prompt=MAIN_ACTIVITY_PROMPT, verbose=True)
PRODUCT_CHAIN = LLMChain(llm=llm, prompt=PRODUCT_PROMPT, verbose=True)
MAJOR_PLAYER_CHAIN = LLMChain(llm=llm, prompt=MAJOR_PLAER_PROMPT, verbose=True)
DEFINITION_CHAIN = LLMChain(llm=llm, prompt=DEFINITION_PROMPT, verbose=True)
REVENUE_CARD_CHAIN = LLMChain(llm=llm, prompt=REVENUE_CARD_PROMPT, verbose=True)
PROFIT_CARD_CHAIN = LLMChain(llm=llm, prompt=PROFIT_CARD_PROMPT, verbose=True)
PROFIT_MARGIN_CARD_CHAIN = LLMChain(llm=llm, prompt=PROFIT_MARGIN_CARD_PROMPT, verbose=True)
ENTERPRISES_CARD_CHAIN = LLMChain(llm=llm, prompt=ENTERPRISES_CARD_PROMPT, verbose=True)

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
            "multiples_table": to_formatted_string(input_text, formatters.multiples_tbl_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 3 ==
if selected_fn == FN.FN3.value:

    st.markdown("Function 3: The AI will explain the entered risk table of an industry")

    input_text = st.text_area(
        label="Risk Table",
        placeholder="Enter a risk table object",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(RISK_TBL_CHAIN, {
            "risk_table": to_formatted_string(input_text, formatters.risk_tbl_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 4 ==
if selected_fn == FN.FN4.value:

    st.markdown("Function 4: The AI will explain the entered barriers to entry checklist of an industry")

    input_text = st.text_area(
        label="Barriers To Entry Checklist",
        placeholder="Enter a barriers to entry checklist object",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(BARRIERS_TO_ENTRY_CHAIN, {
            "barriers_to_entry": to_formatted_string(input_text, formatters.barriers_to_entry_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 5 ==
if selected_fn == FN.FN5.value:

    st.markdown("Function 5: The AI will explain the entered Main Activity of an industry")

    input_text = st.text_area(
        label="Main Activity on an industry",
        placeholder="Enter the main activity of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(MAIN_ACTIVITY_CHAIN, {
            "main_activity": to_formatted_string(input_text, formatters.main_activity_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 6 ==
if selected_fn == FN.FN6.value:

    st.markdown("Function 6: The AI will explain the entered Products and services of an industry")

    input_text = st.text_area(
        label="Products and Services of an industry",
        placeholder="Enter the products and services of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(PRODUCT_CHAIN, {
            "products_and_services": to_formatted_string(input_text, formatters.products_formatter)})

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

        result, exec_time, tkn_cb = get_chain_execution_result(MAJOR_PLAER_PROMPT, {
            "major_players": to_formatted_string(input_text, formatters.major_players_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 8 ==
if selected_fn == FN.FN8.value:

    st.markdown("Function 8: The AI will explain the entered definition of an industry and summarize it")

    input_text = st.text_area(
        label="Definition of an industry",
        placeholder="Enter the Definition of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        result, exec_time, tkn_cb = get_chain_execution_result(DEFINITION_CHAIN, {
            "definition": to_formatted_string(input_text, formatters.definition_formatter)})

        st.markdown(f"#### Here are your results")

        show_chain_execution_info(exec_time, tkn_cb)

        with st.expander("##### Explanation"):
            st.markdown(result)

# == Function 9 ==
if selected_fn == FN.FN9.value:

    st.markdown("Function 9: The AI will explain the entered revenue growth chart of an industry")

    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=100,
        label_visibility="collapsed"
    )

    input_text = st.text_area(
        label="Revenue growth chart values of an industry",
        placeholder="Enter the growth values of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        if industry_title:
        
            result, exec_time, tkn_cb = get_chain_execution_result(REVENUE_CARD_CHAIN, {
                "revenue_card": to_formatted_string(input_text, formatters.revenue_card_formatter),
                "industry_title": industry_title
                })

            st.markdown(f"#### Here are your results")

            show_chain_execution_info(exec_time, tkn_cb)

            with st.expander("##### Explanation"):
                st.markdown(result)

# == Function 10 ==
if selected_fn == FN.FN10.value:

    st.markdown("Function 10: The AI will explain the entered profit growth chart of an industry")

    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=100,
        label_visibility="collapsed"
    )

    input_text = st.text_area(
        label="Profit growth chart values of an industry",
        placeholder="Enter the growth values of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        if industry_title:

            result, exec_time, tkn_cb = get_chain_execution_result(PROFIT_CARD_CHAIN, {
                "profit_card": to_formatted_string(input_text, formatters.profit_card_formatter),
                "industry_title": industry_title
                })

            st.markdown(f"#### Here are your results")

            show_chain_execution_info(exec_time, tkn_cb)

            with st.expander("##### Explanation"):
                st.markdown(result)

# == Function 11 ==
if selected_fn == FN.FN11.value:

    st.markdown("Function 11: The AI will explain the entered profit margin growth chart of an industry")

    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=100,
        label_visibility="collapsed"
    )

    input_text = st.text_area(
        label="Profit margin growth chart values of an industry",
        placeholder="Enter the growth values of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        if industry_title:

            result, exec_time, tkn_cb = get_chain_execution_result(PROFIT_MARGIN_CARD_CHAIN, {
                "profit_margin_card": to_formatted_string(input_text, formatters.profit_margin_card_formatter),
                "industry_title": industry_title
                })

            st.markdown(f"#### Here are your results")

            show_chain_execution_info(exec_time, tkn_cb)

            with st.expander("##### Explanation"):
                st.markdown(result)

# == Function 12 ==
if selected_fn == FN.FN12.value:

    st.markdown("Function 12: The AI will explain the entered enterprises growth chart of an industry")

    industry_title = st.text_input(
        label="Industry Title",
        placeholder="Enter an industry title e.g. HR Consulting",
        max_chars=100,
        label_visibility="collapsed"
    )

    input_text = st.text_area(
        label="Enterprises growth chart values of an industry",
        placeholder="Enter the growth values of an industry",
        label_visibility="collapsed"
    )

    if input_text:

        if industry_title:

            result, exec_time, tkn_cb = get_chain_execution_result(ENTERPRISES_CARD_CHAIN, {
                "enterprises_card": to_formatted_string(input_text, formatters.enterprises_card_formatter),
                "industry_title": industry_title
                })

            st.markdown(f"#### Here are your results")

            show_chain_execution_info(exec_time, tkn_cb)

            with st.expander("##### Explanation"):
                st.markdown(result)
