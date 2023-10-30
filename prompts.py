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
            template="What is the primary focus or purpose of the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Main focus/purpose"
    ),
    (
        PromptTemplate(
            template="What is the wearable technology industry {industry_title}?",
            input_variables=["industry_title"]
        ),
        None,
        "Current state"
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
            template="What is the state of the competition in the {industry_title} industry?",
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
            template="What skills or qualifications are typically needed for careers in the {industry_title} industry in US?"
                     "\n{format_instructions}",
            input_variables=["industry_title"],
            partial_variables={"format_instructions": output_parser.get_format_instructions()}
        ),
        output_parser,
        "Required skills and qualifications"
    ),
    (
        PromptTemplate(
            template="How has the {industry_title} industry in US evolved over time?",
            input_variables=["industry_title"]
        ),
        None,
        "Development over time"
    ),
    (
        PromptTemplate(
            template="How does the supply chain work in the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Supply chain"
    ),
    (
        PromptTemplate(
            template="What are the list of key financial indicators of the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Key metrics to track"
    ),
    (
        PromptTemplate(
            template="What are the current trends shaping the {industry_title} industry in US?",
            input_variables=["industry_title"]
        ),
        None,
        "Current shaping trends"
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
            template="What are the legal or regulatory factors affecting the {industry_title} industry in US?",
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
            # "Examine the provided multiples table, which offers a comprehensive overview of key valuation "
                    #  "multiples pertinent to a specific industry. "
                     "write a bullet points summary about it and present key values. "
                     "please do not get any thing from outside the values I gave it to you"
                     "\n\n>>>\n{multiples_table}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["multiples_table"]
        )
    )
])


# RISK_TBL_PROMPT = ChatPromptTemplate.from_messages([
#     system_msg_prompt,
#     HumanMessagePromptTemplate(
#         prompt=PromptTemplate(
#             template="Analyze the presented table showcasing the risk components associated with a specific industry. "
#                      "for each analysis present a summary key insights and values in one connected paragrph . "
#                      "\n\n>>>\n{risk_table}\n<<<\n\nYOUR RESPONSE:",
#             input_variables=["risk_table"]
#         )
#     )
# ])

SUPPLY_DEMAND_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is the supply and demand for wearable technologies?",
            input_variables=[]
        ),
    )
])

MARKET_SIZE_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is the size of the wearable technology market?",
            input_variables=[]
        ),
    )
])

MARKET_GEO_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="Where in the US wearable technologies mostly sold?",
            input_variables=[]
        ),
    )
])

BARRIERS_TO_ENTRY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Help me understand the barriers to entry for {industry} using this data."
            # "Examine the dataset and compile a checklist of industry-specific entry barriers. "
            # "Provide a bullet-point summary highlighting crucial insights and value ."
            "\n\n>>>\n{barriers_to_entry}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["industry","barriers_to_entry"]
        )
    )
])

TARGET_CUSTOMER_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is the size of target customers for wearable technologies? "
            "What is the size of health and fitness enthusiasts?",
            input_variables=[]
        ),
    )
])

# ////////////////////////  first file for editing  //////////////

MAIN_ACTIVITY_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            # "Examine the Main Activities of an industry,elucidate each activity with a comprehensive explanation, "
            # "and include definition or relevant contextual information to facilitate a clear understanding of the activity."
            "Conduct a comprehensive analysis of the key activities within an industry, beginning with an initial overview of these activities,"
            "followed by detailed explanations for each, including relevant definitions and context to aid comprehension,"
            "and conclude with a summarization of these activities."
            "\n\n>>>\n{main_activity}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["main_activity"]
        )
    )
])

PRODUCT_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Perform an in-depth analysis of a list of products and services," 
            "each featuring segments, revenue percentages, revenue values, and multipliers." 
            "Start with a broad overview of these items, followed by detailed explanations for each, "
            "including pertinent definitions and context to facilitate understanding, and conclude with a comprehensive summary."
            "\n\n>>>\n{products_and_services}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["products_and_services"]
        )
    )
])

MAJOR_PLAER_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Perform an in-depth analysis of a list of products and services," 
            "each featuring segments, revenue percentages, revenue values, and multipliers." 
            "Start with a broad overview of these items, followed by detailed explanations for each, "
            "including pertinent definitions and context to facilitate understanding, and conclude with a comprehensive summary."
            "\n\n>>>\n{major_players}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["major_players"]
        )
    )
])

DEFINITION_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "First optimize this definition in detailed  then summarize it"
            "\n\n>>>\n{definition}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["definition"]
        )
    )
])

REVENUE_CARD_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please provide a comprehensive explanation of the key data points depicted in the revenue growth graph for the {industry_title} sector, "
            "with a focus on quarterly or monthly revenue figures. "
            "Additionally, incorporate historical growth values dating back to 2017 to provide context for the industry's performance. "
            "Lastly, include forecasts for revenue growth up to 2027, outlining any notable trends, fluctuations, "
            "or influencing factors in at least one detailed paragraph to ensure a thorough and easily understandable analysis."
            "\n\n>>>\n{revenue_card}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["revenue_card", "industry_title"]
        )
    )
])

PROFIT_CARD_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "explain a detailed graph illustrating the profit growth values for the {industry_title} sector in 2022. Include key data points, such as quarterly or monthly profit figures, and highlight any significant trends, events, or factors that influenced the industry's profit performance during that year. make the explain informative and easy to understand."
            # "Analyze the profit growth graph for the {industry_title} sector in 2022, delving into both quarterly and monthly profit figures. Offer a comprehensive and accessible explanation, highlighting notable trends, events, and factors shaping the industry's financial performance for the year. Additionally, provide historical context by examining growth trends from 2017 to 2022. Illuminate the key drivers behind the industry's profit performance in 2022, drawing comparisons with previous years."
            # "Explain the significant data points depicted in the profit growth graph for the {industry_title} sector,"
            # "including quarterly and monthly profit figures for the year 2022. "
            # "Ensure that your explanation is comprehensive and easily comprehensible. "
            # "highlight any significant trends, events, or factors that influenced the industry's profit performance during that year."
            # "Additionally, provide context by discussing the historical growth trends from 2017 to 2021. "
            # "Your explanation should offer insights into what drove the industry's profit performance throughout the year "
            # "and how it compares to previous years."
            "\n\n>>>\n{profit_card}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["profit_card", "industry_title"]
        )
    )
])

PROFIT_MARGIN_CARD_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please analyze the profit margin graph values for the {industry_title} sector, focusing on key data points,"
            "such as quarterly or monthly profit margin figures for the year 2022." 
            "Additionally, provide an overview of the historical profit margin growth values starting from 2017." 
            "Your explanation should be comprehensive and easy to understand, highlighting any notable trends, "
            "fluctuations, or significant events that impacted the industry's profit margins during this time period."
            "\n\n>>>\n{profit_margin_card}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["profit_margin_card", "industry_title"]
        )
    )
])

ENTERPRISES_CARD_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Analyze the critical data points within the growth graph representing the performance of enterprises in the {industry_title} sector. "
            "This analysis should encompass quarterly or monthly figures for enterprises growth from 2022, examining key trends and influential factors. "
            "Additionally, provide an insightful historical context by tracing growth values back to 2017. "
            "Extend the analysis to include a forecast of growth trends up to 2027. "
            "Present this information in a detailed yet easily understandable manner, "
            "ensuring that the explanations are comprehensive and concise, "
            "offering valuable insights into the industry's evolution and future trajectory."
            "\n\n>>>\n{enterprises_card}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["enterprises_card", "industry_title"]
        )
    )
])

POP_RACE_ETHN_PROMPT = ChatPromptTemplate.from_messages([
    system_msg_prompt,
    HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template=
            "Please review the graph and provide a summary of the most significant insights, focusing on."
            # "Please analyze the graph and provide a summary of its key insights."
            # "Please help me to understand the key insights graph  "
            # "please help me to understand this graph with this data for each name by replacing the name with name the country of this zipcode "
            # "with providing first a brief introducion and in the last brief summary to all paragraph"
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

POP_MATERIAL_PROMPT = ChatPromptTemplate.from_messages([
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

POP_RELSHIP_HH_PROMPT = ChatPromptTemplate.from_messages([
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

POP_GENDER_PROMPT = ChatPromptTemplate.from_messages([
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

POP_EDU_ATTAINMENT_PROMPT = ChatPromptTemplate.from_messages([
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

DEMOGRAPHIC_OVERVIEW_PROMPT = ChatPromptTemplate.from_messages([
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

HH_SIZE_PROMPT = ChatPromptTemplate.from_messages([
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
            "Given a JSON schema representing your data, please provide a summary of the key insights and trends that can be derived from this data. Highlight any important data points, patterns, or relationships that are significant. Feel free to include relevant statistics or observations to make the summary as informative as possible."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
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
            "Please analyze the graph and provide a summary of its key insights."
            "\n\n>>>\n{obj}\n<<<\n\nYOUR RESPONSE:",
            input_variables=["obj"]
        )
    )
])

