def multiples_tbl_formatter(multiples_table_obj):
    rows = [
        "   ".join(["              ", *[f"{year:^6}" for year in multiples_table_obj["EBIT/Revenue"].keys()]]),
        "   ".join(["EBIT/Revenue  ", *[f"{val:06.3f}" for val in multiples_table_obj["EBIT/Revenue"].values()]]),
        "   ".join(["EBITDA/Revenue", *[f"{val:06.3f}" for val in multiples_table_obj["EBITDA/Revenue"].values()]]),
        "   ".join(["Leverage Ratio", *[f"{val:06.3f}" for val in multiples_table_obj["Leverage Ratio"].values()]])
    ]
    table = "\n".join(rows)
    return table

def barriers_to_entry_formatter(barriers_to_entry_obj):
    return "\n".join([f"{k + ':':<22} {v.title()}" for k, v in barriers_to_entry_obj.items()])

def main_activity_formatter(main_activity_obj):
    return "\n".join([f"{v}" for v in main_activity_obj["mainActivities"]])
     

def products_formatter(products_obj): 
    component = ["segment", "revenuePercentage", "revenueValue", "multiplier"]
    rows = [
        "                         ".join(["  ", *[f"{i:<11}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k['segment']:<64}",
                    f"{k['revenuePercentage']:<20}",
                    f"{k['revenueValue']:<20}",
                    f"{k['multiplier']:<20}"
                ]
            ) for k in products_obj["productsAndServices"]
        ]
    ]
    table = "\n".join(rows)
    return table


def major_players_formatter(major_players_obj): 
    component = ["shortName", "longName", "revenue", "revenueGrowth", "profit", "profitGrowth", "highMarketShare", "highMarketShareGrowth", "year"]
    rows = [
        "   ".join(["  ", *[f"{i:<35}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k['shortName']:<35}",
                    f"{k['longName']:<35}",
                    f"{k['revenue']:<35}",
                    f"{k['revenueGrowth']:<35}"
                    f"{k['profit']:<35}"
                    f"{k['profitGrowth']:<35}"
                    f"{k['highMarketShare']:<35}"
                    f"{k['highMarketShareGrowth']:<35}"
                    f"{k['year']:<35}"
                ]
            ) for k in major_players_obj["majorPlayers"]
        ]
    ]
    table = "\n".join(rows)
    return table

def definition_formatter(definition_obj):
    return "".join(definition_obj["industryDefinition"])

def revenue_card_formatter(revenue_card_obj): 
    metrics = ["value", "historicalGrowth", "forecastGrowth"]
    json_decode = revenue_card_obj.get("revenue", {})
    
    metric_data = [json_decode.get(metric, {}) for metric in metrics]
    
    rows = [
        "   ".join(["       ", *[f"{i:<14}" for i in metrics]]),        
        "   ".join([" year: ", *[f"{data.get('year', ''):<15}" for data in metric_data]]),
        "   ".join([" value:", *[f"{data.get('value', ''):<15}" for data in metric_data]]),
        "   ".join([" unit: ", *[f"{data.get('unit', ''):<15}" for data in metric_data]])
    ]
    
    table = "\n".join(rows)
    return table

def profit_card_formatter(profit_card_obj): 
    metrics = ["value", "historicalGrowth"]
    json_decode = profit_card_obj.get("profit", {})
    
    metric_data = [json_decode.get(metric, {}) for metric in metrics]
    
    rows = [
        "   ".join(["       ", *[f"{i:<14}" for i in metrics]]),        
        "   ".join([" year: ", *[f"{data.get('year', ''):<15}" for data in metric_data]]),
        "   ".join([" value:", *[f"{data.get('value', ''):<15}" for data in metric_data]]),
        "   ".join([" unit: ", *[f"{data.get('unit', ''):<15}" for data in metric_data]])
    ]
    
    table = "\n".join(rows)
    return table

def profit_margin_card_formatter(profit_margin_card_obj): 
    metrics = ["value", "historicalGrowth"]
    json_decode = profit_margin_card_obj.get("profitMargin", {})
    
    metric_data = [json_decode.get(metric, {}) for metric in metrics]
    
    rows = [
        "   ".join(["       ", *[f"{i:<14}" for i in metrics]]),        
        "   ".join([" year: ", *[f"{data.get('year', ''):<15}" for data in metric_data]]),
        "   ".join([" value:", *[f"{data.get('value', ''):<15}" for data in metric_data]]),
        "   ".join([" unit: ", *[f"{data.get('unit', ''):<15}" for data in metric_data]])
    ]
    
    table = "\n".join(rows)
    return table

def enterprises_card_formatter(enterprises_card_obj): 
    metrics = ["value", "historicalGrowth", "forecastGrowth"]
    json_decode = enterprises_card_obj.get("enterprises", {})
    
    metric_data = [json_decode.get(metric, {}) for metric in metrics]
    
    rows = [
        "   ".join(["       ", *[f"{i:<14}" for i in metrics]]),        
        "   ".join([" year: ", *[f"{data.get('year', ''):<15}" for data in metric_data]]),
        "   ".join([" value:", *[f"{data.get('value', ''):<15}" for data in metric_data]]),
        "   ".join([" unit: ", *[f"{data.get('unit', ''):<15}" for data in metric_data]])
    ]
    
    table = "\n".join(rows)
    return table

def pop_race_ethnicity_formatter(obj): 
    json_decode = obj.get("PopulationByRaceEthnicity", "")
    
    component = ["OneRace", "TwoOrMoreRaces", "White", "Black", "AmericanIndian", "Asian", "PacificIslander", "Other", "Hispanic"]
    rows = [
        f"{'Name':<10}{'Total':<10}{'Year':<10}"+"   ".join(["  ", *[f"{i:<10}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k.get('Name','').split(':')[-1]:<10}",
                    f"{k['Row']['Total']:<10}",
                    f"{k['Row']['Year']:<10}",
                    f"value: {k['Row']['OneRace']['Value']} percentage: {k['Row']['OneRace']['Percentage']:<25}",
                    f"value: {k['Row']['TwoOrMoreRaces']['Value']} percentage: {k['Row']['TwoOrMoreRaces']['Percentage']:<25}",
                    f"value: {k['Row']['White']['Value']} percentage: {k['Row']['White']['Percentage']:<25}",
                    f"value: {k['Row']['Black']['Value']} percentage: {k['Row']['Black']['Percentage']:<25}",
                    f"value: {k['Row']['AmericanIndian']['Value']} percentage: {k['Row']['AmericanIndian']['Percentage']:<25}",
                    f"value: {k['Row']['Asian']['Value']} percentage: {k['Row']['Asian']['Percentage']:<25}",
                    f"value: {k['Row']['PacificIslander']['Value']} percentage: {k['Row']['PacificIslander']['Percentage']:<25}",
                    f"value: {k['Row']['Other']['Value']} percentage: {k['Row']['Other']['Percentage']:<25}",
                    f"value: {k['Row']['Hispanic']['Value']} percentage: {k['Row']['Hispanic']['Percentage']:<25}",
                ]
            ) for k in json_decode["Targets"]
        ]
    ]

    table = "\n".join(rows)
    return table 

def pop_marital_status_formatter(obj):
    json_decode = obj.get("PopulationByMaritalStatus", "")
    component = ["Year","Total","Divorced", "Married", "NeverMarried", "Separated",  "Widowed"]
    rows = [
        f" {'Name':<18}"+"   ".join(["  ", *[f"{i:<23}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k.get('Name','').split(':')[-1]:<20}",
                    f"{k['Row']['Year']:<22}",
                    f"{k['Row']['Total']:<20}",
                    f"{k['Row']['Divorced']:<25}",
                    f"{k['Row']['Married']:<25}",
                    f"{k['Row']['NeverMarried']:<22}",
                    f"{k['Row']['Separated']:<22}",
                    f"{k['Row']['Widowed']:<35}"
                ]
            ) for k in json_decode["Targets"]
        ]
    ]

    table = "\n".join(rows)
    return table

def pop_relship_hh_formatter(obj):
    json_decode = obj.get("PopulationByRelationshipAndHousehold", "")
    component = ["Year","Total","MarriedCoupleFamily", "CohabitingCoupleHousehold", "MaleHouseholderNoSpousePartnerPresent", "FemaleHouseholderNoSpousePartnerPresent"]
    rows = [
        f" {'Name':<18}"+"   ".join(["  ", *[f"{i:<22}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k.get('Name','').split(':')[-1]:<20}",
                    f"{k['Row']['Year']:<22}",
                    f"{k['Row']['Total']:<23}",
                    f"{k['Row']['MarriedCoupleFamily']:<23}",
                    f"{k['Row']['CohabitingCoupleHousehold']:<30}",
                    f"{k['Row']['MaleHouseholderNoSpousePartnerPresent']:<32}",
                    f"{k['Row']['FemaleHouseholderNoSpousePartnerPresent']}",
                ]
            ) for k in json_decode["Targets"]
        ]
    ]

    table = "\n".join(rows)
    return table

def pop_gender_formatter(obj):
    json_decode = obj.get("PopulationByGender","")

    component = ["Year","Total","Male","Female"]
    rows = [
        f" {'Name':<18}"+"   ".join(["  ", *[f"{i:<22}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k.get('Name','').split(':')[-1]:<20}",
                    f"{k['Row']['Year']:<22}",
                    f"{k['Row']['Total']:<23}",
                    f"{k['Row']['Male']:<23}",
                    f"{k['Row']['Female']:<30}",
                ]
            ) for k in json_decode["Targets"]
        ]
    ]

    table = "\n".join(rows)
    return table

def pop_edu_attainment_formatter(obj):
    json_decode = obj.get("PopulationByEducationalAttainmentStatus","")

    component = ["Year","Total","<9th", "9-12th", "HighSchool", "AttendedCollege","AssociateDegree","BachelorsDegree","GraduateProfessionalDegree"]
    rows = [
        f" {'Name':<18}"+"   ".join(["  ", *[f"{i:<22}" for i in component]]),
        *[
            "   ".join(
                [
                    f"{k.get('Name','').split(':')[-1]:<20}",
                    f"{k['Row']['Year']:<22}",
                    f"{k['Row']['Total']:<23}",
                    f"{k['Row']['<9th']:<23}",
                    f"{k['Row']['9-12th']:<20}",
                    f"{k['Row']['HighSchool']:<20}",
                    f"{k['Row']['AttendedCollege']:<25}",
                    f"{k['Row']['AssociateDegree']:<23}",
                    f"{k['Row']['BachelorsDegree']:<23}",
                    f"{k['Row']['GraduateProfessionalDegree']}",
                ]
            ) for k in json_decode["Targets"]
        ]
    ]

    table = "\n".join(rows)
    return table

def demographic_overview_formatter(obj):
    json_decode = obj.get("DemographicOverview","")

    component = ["population","popGrowthRate","households", "hhGrowthRate", "unemploymentRate", "perCapitaPersonalIncome"]
    cities = ["99503","95917","95914","95901","95969"]
    rows = [
        f"{'Name':15}"+"   ".join(["  ", *[f"{i:<21}" for i in component]]),
        *[
            "".join([
                " ".join([f"{c:<22}"]),
                " ".join([f"{json_decode[c]['population']:<23}"]),
                " ".join([f"{json_decode[c]['popGrowthRate']:<24}"]),
                " ".join([f"{json_decode[c]['households']:<25}"]),
                " ".join([f"{json_decode[c]['hhGrowthRate']:<25}"]),
                " ".join([f"{json_decode[c]['unemploymentRate']:<25}"]),
                " ".join([f"{json_decode[c]['perCapitaPersonalIncome']}"]),
        ])for c in cities
        ]
    ]

    table = "\n".join(rows)
    return table

def hh_size_formatter(obj):
    jsondecoded = obj.get("HouseholdsBySize","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())

    rows = [
        "".join([f"{c:<15}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<15}"),
                "".join(f"{j['Row'][c]:<23}" for c in component)
            ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def civil_pop_formatter(obj):
    jsondecoded = obj.get("CivilianPopulation","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<29}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<40}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name")
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)

    return table

def hh_income_formatter(obj):
    jsondecoded = obj.get("HouseholdIncome","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"{j['Forecast']['Row'][c]:<23}" for c in component if c != "Name"),
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def languagesSpoken_forecast_formatter(obj):
    jsondecoded = obj.get("LanguagesSpoken","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"{j['Forecast']['Row'][c]:<23}" for c in component if c != "Name"),
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def personalIncomeSummary_forecast_formatter(obj):
    jsondecoded = obj.get("PersonalIncomeSummary","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"{j['Forecast']['Row'][c]:<23}" for c in component if c != "Name" or c != "PersonalIncome"),
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def hh_summary_forecast_formatter(obj):
    jsondecoded = obj.get("HouseholdSummary","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"{j['Forecast']['Row'][c]:<23}" for c in component if c != "Name"),
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def populationByAge_forecast_formatter(obj):
    jsondecoded = obj.get("PopulationByAge","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    forecast = ["MedianAge","Year"]
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join([
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"{j['Forecast']['Row'][f]:<23}" for f in forecast),
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

def pop_summary_forecast_formatter(obj):
    jsondecoded = obj.get("PopulationSummary","")
    component = ["Name"] +list(jsondecoded["Targets"][0]["Row"].keys())
    rows = [
        "".join([f"{c:<30}" for c in component ]),
        *[
            "".join(
                [
                "".join(f"{j['Name'].split(':')[-1]:<30}"),
                "".join(f"{j['Row'][c]:<23}" for c in component if c != "Name"),
                "".join("\nForcast                       "),
                "".join(f"Growth: {j['Forecast']['Growth']}"),
                *[
                    "".join(
                    [
                        "".join(f"{f[c]:<23}" for c in component if c != "Name"),
                    ]
                ) for f in j['Forecast']['Rows']
                ]
        ])for j in jsondecoded['Targets'] if j['Name'].split(' ')[-1] !="All"
        ]
    ]

    table = "\n".join(rows)
    return table

