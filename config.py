
#? 1. Getting a series of OKRs ready-to-go
# What are some relevant OKRs that I can set to [achieve specific goal]?
# What are effective Key Results I should consider if my Objective is to [objective]
# What are the best success metrics and KPIs for measuring [specific topic]?

#? 2. Finding baselines for your KRs
# What are industry benchmarks for [metric]?

#? 3. Finding potential initiatives
# What are the most effective initiatives to [achieve specific Key Result]


def OKR_O_helper(objective:str="achive 2 million gross sales in next quarter"):
    _okr_objective_helper=[
        f'What are some relevant OKRs that I can set to {objective}?',
        f'What are effective Key Results I should consider if my Objective is to {objective}',
        # f'What are the best success metrics and KPIs for measuring: "{objective}"',
    ]
    return _okr_objective_helper
def OKR_KR_helper(keyresult:str="launch our crypto network in 2 monhts"):
    _okr_keyresult_helper=[
        f'What are industry benchmarks for: "{keyresult}"?',
        # f'What are the most effective initiatives to {keyresult}'   
    ]
    return _okr_keyresult_helper