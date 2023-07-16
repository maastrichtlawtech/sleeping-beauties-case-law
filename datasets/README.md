## Datasets

1. `all_cases_metadata.csv`: This dataset contains metadata for each court case, with each row representing a single case. The fields are as follows:

   - `source`: The unique identifier for the case.
   - `case_label`: A human-readable label for the case.
   - `ecli`: The European Case Law Identifier, a unique identifier for European court decisions.
   - `case_type`: The type of the case, for example, "Judgement".
   - `judge`: The name of the judge.
   - `advocate`: The name of the advocate.
   - `country`: The country where the case was judged.
   - `country-chamber`: The specific chamber where the case was judged.
   - `chamber`: The chamber of the court.
   - `main_subject`: The main subject of the case.
   - `month_document`: The month when the case document was created.
   - `year_lodge`: The year when the case was lodged.
   - `month_lodge`: The month when the case was lodged.
   - `case_time`: The duration of the case.
   - `n_countries`: The number of countries involved in the case.
   - `joined_cases`: Whether the case was joined with other cases.
   - `ruling_title`: The title of the ruling.
   - `ruling_name`: The name of the ruling.
   - `ruling_type`: The type of the ruling.
   - `ruling_content`: The content of the ruling.
   
2. `all_cases_citations.csv`: This dataset contains citation relationships between the court cases. Each row represents a single citation, with the `source` case citing the `target` case.