# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This classification model uses Logistic Regression due its ease of implementation and feasilbiity when applied to large datasets, is based on publicly accessible census data. The model was designed to predict the annual income categories defined as "less than or equal to $50k" or "exceeds $50k" based on combinations of personal, educational, locale, income and career demographics.
## Intended Use
This model provides insight into the income inequities as it evaluates gender, race, age, native country among many of the features available. Since this data is from 1994, the results don't accurately reflect current state, however this model as designed, can be applied to a newer dataset implementing the same column layout by simply replacing the old CSV file with the new.

Insights gained from this model could lead to implementation of government or private sector sponsored programs addressing some of the income disparaties amongst specific demographic groups. 
## Training Data
The census dataset consisting of personal, educational, locale, income and career demographics captured 32.561 rows of data. When performing the training and testing functions, the data was split by 80% training and 20% testing.
## Evaluation Data

## Metrics
_Please include the metrics used and your model's performance on those metrics._
THe model was evaluated using a F1 score of.



## Ethical Considerations

## Caveats and Recommendations
Since this data is still gathered manually through surveys or interviews, the "human element" exists and therefore the potential for unintended bias. Aany insights gained from the model would need to take that into consideration.