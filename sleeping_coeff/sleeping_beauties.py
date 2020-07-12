import pandas as pd
import math
import warnings
warnings.filterwarnings("ignore")

cases_citations = pd.read_csv('../datasets/all_cases_citations.csv', encoding='utf-8')
cases_metadata = pd.read_csv('../datasets/all_cases_metadata.csv', encoding='utf-8')
#cases_metadata2 = pd.read_csv('judgementstest_metadata_kody.csv', names=["source", "advocate", "ruling_title",  "chamber", "ruling_name" , 	"ruling_type", "ruling_content", "case_label" , "ecli", "lodge_date" , "document_date" ,"country", "judge" , "main_subject"])
#cases_metadata3 = pd.read_csv('orders_publication_year.csv')
cases_with_no_metadata = []

publication_year = 0
# Number of citations in the year (after publication) with the maximum number of citations
ctm = 0
# Number of years after publication to get to the year with maximum number of citations
tm = 0 
# Citation distribution 
# c[0] = number of citations in the same year of publication,
# c[1] = number of citations in the first year after publication,
# c[2] = number of citations in the second year after publication,
# ...
# etc.
c = [] 
#awakening time
ta = 0
dt = []
dt_dict = {}

#62006CJ0256
#print(cases_citations.target.value_counts()['62006CJ0256'])
#print(cases_citations[cases_citations['target'] == '62006CJ0256']['source'].tolist())

# function to return key for any value 
def get_key(val, my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
            return key 
    return "key doesn't exist"

def get_publication_year(case_id):
    global cases_metadata
    global cases_metadata2
    global cases_metadata3
    global cases_with_no_metadata
    
    if len(cases_metadata[cases_metadata['source'] == case_id]['year_document'].values) > 0:
        return cases_metadata[cases_metadata['source'] == case_id]['year_document'].values[0]
    elif len(cases_metadata3[cases_metadata3['source'] == case_id]['year'].values) > 0:
        return cases_metadata3[cases_metadata3['source'] == case_id]['year'].values[0]
    elif len(cases_metadata2[cases_metadata2['source'] == case_id]['document_date'].values) > 0:
        date = cases_metadata2[cases_metadata2['source'] == case_id]['document_date'].values[0]
        dateparts = date.split("/")
        if len(dateparts) >= 1:
            return dateparts[len(dateparts)-1]
        else:
            return -1
    else:
        #print("ERROR")
        cases_with_no_metadata.append(case_id)
        return -1
        #print(case_id + " : " + str(cases_metadata[cases_metadata['source'] == case_id]['year_document'].values))
    
def get_citations_in_year(case_id, year):
    global cases_citations
    citing_cases_in_year = []
    citing_cases = cases_citations[cases_citations['target'] == case_id]['source'].tolist()
    for citing_case in citing_cases:
        if (get_publication_year(citing_case) == year):
            citing_cases_in_year.append(citing_case)
    return len(citing_cases_in_year)
    
def get_total_citations(case_id):
    global cases_citations
    return len(cases_citations[cases_citations['target'] == case_id]['source'].tolist())  
    #return cases_citations.target.value_counts()[case_id]

def get_citations(case_id):
    global cases_citations
    return cases_citations[cases_citations['target'] == case_id]['source'].tolist()   

def calculate_citation_distribution_by_year(case_id, publication_year):
    global c
    global tm
    global ctm
    
    done = False
    current_year = publication_year
    index = 0
    while not done:
        #print("year: " + str(current_year))
        citations = get_citations_in_year(case_id, current_year)   
        current_year = current_year + 1
        done = (current_year == 2020)
        #print(citations)
        c.append(citations)        
    ctm = max(c)
    tm = c.index(max(c))

def calculate_beauty_coefficient(case_id):
    global ctm
    global tm
    global c
    global publication_year
    global dt
    global dt_dict
    
    beauty_coefficient = 0
    publication_year = get_publication_year(case_id)
    calculate_citation_distribution_by_year(case_id, publication_year)
    
    if tm == 0:
        distance_t = 0
        dt.append(distance_t)
        #print(dt)
        dt_dict[0] = distance_t
    
    for i in range(0,tm):        
        # calculate distance
        distance_t = abs(((ctm - c[0])*i) - (tm*c[i]) + (tm*c[0])) / (math.sqrt(((ctm - c[0])**2 + tm**2)))
        dt.append(distance_t)
        #print(dt)
        dt_dict[i] = distance_t
        
        if (c[i] > 1):
            beauty_coefficient = beauty_coefficient + (((ctm - c[0])*i) + c[0] - c[i])/c[i]
        else:
            beauty_coefficient = beauty_coefficient + (((ctm - c[0])*i) + c[0] - c[i])
    
    return beauty_coefficient
            
bcoefficients = {}
index = 0

#listf = cases_metadata['source']
for item in cases_metadata['source']:#while (index <= 8):
    print(str(index) + ". " + item)
    b = calculate_beauty_coefficient(item)
    ta = get_key(max(dt), dt_dict)    
    bcoefficients[item] = [item, str(b), str(publication_year), str(get_total_citations(item)), str(ctm), str(publication_year+tm), str(publication_year+ta),str(ta),str(tm-ta)]    
    index = index + 1
    dt = []
    publication_year = 0
    dt_dict = {}
    ta = 0
    ctm = 0
    # Number of years after publication to get to the year with maximum number of citations
    tm = 0 
    # Citation distribution 
    # c[0] = number of citations in the same year of publication,
    # c[1] = number of citations in the first year after publication,
    # c[2] = number of citations in the second year after publication,
    # ...
    # etc.
    c = [] 
    #bcoefficients[item] = calculate_beauty_coefficient(item)
    
#     for item in cases_metadata['source']:
#     index = index + 1

# #     citations = get_citations(item)
# #     for citation in citations:
# #         get_publication_year(citation)
    
import json

json = json.dumps(bcoefficients)
f = open("bcoefficients"+str(index)+".json","w")
f.write(json)
f.close()


