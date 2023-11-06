from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    # SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    # AIMessagePromptTemplate
)
from langchain.schema import SystemMessage
from langchain.output_parsers import CommaSeparatedListOutputParser


# Output Parsers
output_parser = CommaSeparatedListOutputParser()

# System Message
system_msg_prompt = SystemMessage(content="You are a helpful assistant that can answer questions about an industry")
# or
# system_template = "You are a helpful assistant that can answer questions about an industry"
# system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# Human Prompts
human_prompts_and_parsers_and_headings = [
    (
        PromptTemplate(
            template="What is the definition of the {industry_title} industry?",
            input_variables=["industry_title"]
        ),
        None,
        "Definition"
    ),
    (
        PromptTemplate(
            template="What is the primary focus or purpose of the {industry_title} industry?",
            input_variables=["industry_title"]
        ),
        None,
        "Main focus/purpose"
    ),
    (
        PromptTemplate(
            template="How has the {industry_title} industry evolved over time?",
            input_variables=["industry_title"]
        ),
        None,
        "Development over time"
    ),
    (
        PromptTemplate(
            template="What is the state of the {industry_title} industry ?",
            input_variables=["industry_title"]
        ),
        None,
        "Current state"
    ),
    (
        PromptTemplate(
            template="What are the current trends shaping the {industry_title} industry ?",
            input_variables=["industry_title"]
        ),
        None,
        "Current shaping trends"
    ),
    (
        PromptTemplate(
            template="What is the supply and demand for {industry_title} industry ?",
            input_variables=["industry_title"]
        ),
        None,
        "State of Supply/Demand"
    ),
    (
        PromptTemplate(
            template="What is the size of the {industry_title} market?",
            input_variables=["industry_title"]
        ),
        None,
        "Market Size"
    ),
    (
        PromptTemplate(
            template="in which US regions is {industry_title} mostly concentrated?",
            input_variables=["industry_title"]
        ),
        None,
        "Market Geography"
    ),
    (
        PromptTemplate(
            template="Who are the main players in {industry_title} industry and what is the market share of each one of these players?",
            input_variables=["industry_title"]
        ),
        None,
        "Main Players"
    ),
    (
        PromptTemplate(
            template="What is the state of the competition and what are some key aspects of the competition in the {industry_title} industry?",
            input_variables=["industry_title"]
        ),
        None,
        "Competition intensity"
    ),
    (
        PromptTemplate(
            template="Analyze Porter's 5 forces for this {industry_title} industry ?",
            input_variables=["industry_title"]
        ),
        None,
        "Porter's Five forces"
    ),
    (
        PromptTemplate(
            template="Who are the target customers for the {industry_title} industry and what are the key aspects of their lifeStyle? ",
            input_variables=["industry_title"]
        ),
        None,
        "Target Customers"
    ),
    (
        PromptTemplate(
            template="What skills or qualifications are typically needed for careers in the {industry_title} industry?"
                     "\n{format_instructions}",
            input_variables=["industry_title"],
            partial_variables={"format_instructions": output_parser.get_format_instructions()}
        ),
        output_parser,
        "Required skills and qualifications"
    ), 
    (
        PromptTemplate(
            template="How does the supply chain work in the {industry_title} industry ?",
            input_variables=["industry_title"]
        ),
        None,
        "Supply chain"
    ),
    (
        PromptTemplate(
            template="What are the list of key financial indicators of the {industry_title} industry?",
            input_variables=["industry_title"]
        ),
        None,
        "Key metrics to track"
    ),
    (
        PromptTemplate(
            template="How is the {industry_title} industry in US affected by economic factors "
                     "such as inflation, unemployment rate, etc?",
            input_variables=["industry_title"]
        ),
        None,
        "Influential economic factors"
    ),
    (
        PromptTemplate(
            template="What are the legal or regulatory factors affecting the {industry_title} industry?",
            input_variables=["industry_title"]
        ),
        None,
        "Influential legal factors"
    ),
    (
        PromptTemplate(
            template="How do political factors influence the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Influential political factors"
    ),
    (
        PromptTemplate(
            template="How is technology influencing the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Influential technological factors"
    ),
    (
        PromptTemplate(
            template="How does the {industry_title} industry in US affect the environment "
                     "and how is it addressing these impacts?",
            input_variables=["industry_title"]
        ),
        None,
        "Effects on the environments"
    )
]


human_prompts, OUTPUT_PARSERS, HEADINGS = list(zip(*human_prompts_and_parsers_and_headings))

PROMPTS = [
    ChatPromptTemplate.from_messages([
        system_msg_prompt,
        HumanMessagePromptTemplate(prompt=prompt)
    ])
    for prompt in human_prompts
]

MULTIPLES_TBL_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
                     "Analyze the last 6 years of this table, point out key figures and percentage changes and present key takeaways"
                     "\n\n>>>\n{multiples_table}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["multiples_table"]
        )
    )
])

BARRIERS_TO_ENTRY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Help me understand the barriers to entry for {industry_title} using this data."
            "Provide a bullet-point summary highlighting crucial insights and value ."
            "\n\n>>>\n{barriers_to_entry}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["barriers_to_entry","industry_title"]
        )
    )
])

PRODUCT_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Perform a summary analysis of this list of products and services of the {industry_title} ,"
            " including pertinent definitions and context  to facilitate understanding "
            "\n\n>>>\n{products_and_services}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["products_and_services","industry_title"]
        )
    )
])

MAJOR_PLAYER_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Produce a brief company overview (including date founded, number of employees and key strengths) "
            "and analyze performance for each player below"
            "\n\n>>>\n{major_players}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["major_players"]
        )
    )
])
# ////////////////////////  Done  //////////////
# ////////////////////////  for Here after the first meet //////////////

#/////////////////// Demographic //////////////////////////

POP_RACE_ETHN_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize population by race/ethnicity data, highlighting the key demographic trends and disparities in the distribution of racial and ethnic groups. Include information on the largest ethnic groups, their percentages, and any significant changes over recent years."
            "\n\n>>>\n{obj1}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj1"]
        )
    )
])

POP_MATERIAL_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize population by marital status data, including key statistics and trends. Highlight the distribution of individuals across marital status categories, and provide insights into any changes or patterns observed over the years."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

POP_RELSHIP_HH_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize and provide key insights on population by relationship and household data"
            " Analyze the distribution of various relationships within households"
            "Highlight trends in household size, composition, and changes over time."
            "Use this data to extract relevant information and draw meaningful conclusions about "
            "the demographics and living arrangements of the population."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

POP_GENDER_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            # "Summarize the population by gender data for a specific region or country of your choice. Provide key insights, including the total population, gender distribution, age groups, and any notable trends or patterns observed in the data"
            "Provide a concise summary of gender-based population data, focusing on significant demographic trends, gender distribution, and noteworthy shifts or disparities within the last ten years."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

POP_EDU_ATTAINMENT_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize and provide key insights from this data."
            "Include information about educational levels, regional disparities,"
            " and any notable trends or patterns observed in the data."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

DEMOGRAPHIC_OVERVIEW_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize and provide key insights from this data"
            "Analyze the trends and patterns in the data to highlight significant findings,"
            "potential challenges, and opportunities based on the demographic information."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

HH_SIZE_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize and provide key insights from the Household by Size data,"
            " including trends, distribution, and any notable patterns or variations "
            "in household sizes over this data."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

CIVIL_POP_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

HH_INCOME_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

GENERAL_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Given a JSON schema representing your data, please provide a summary of the key insights and trends "
            "that can be derived from this data. Highlight any important data points, patterns, or relationships that "
            "are significant. Feel free to include relevant statistics or observations to make the summary as informative as possible."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

LANGUAGE_SPOKEN_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the Json data and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

PERSONAL_INCOME_SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

HH_SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            ""
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])


POP_AGE_SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize the Population by Age Summary data, highlighting key insights and trends in age distribution, demographic shifts, and any notable patterns or anomalies."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

POP_SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Summarize the key insights from the latest Population Summary data. Include information about population trends, demographics, and any significant changes observed in the data."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

CIVI_EMP_POP_IND_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

CONSUMER_SPEND_INFO_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please perform  the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

IND_PERFORM_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please perform  the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

IND_SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please perform  the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])


