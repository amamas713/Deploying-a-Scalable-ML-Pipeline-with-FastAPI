# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This classification model utilizing Logistic Regression due its ease of implementation and feasilbiity when applied to large datasets; is based on publicly accessible census data. The model was designed to predict the annual income categories defined as "less than or equal to $50k" or "exceeds $50k" based on combinations of personal, educational, locale, income and career demographics.
## Intended Use
This model provides insight into the income inequities as it evaluates gender, race, age, native country among many of the features available. Since this data is from 1994, the results don't accurately reflect current state, however this model as designed, can be applied to a newer dataset implementing the same column layout by simply replacing the old CSV file with the new.

Insights gained from this model could lead to implementation of government or private sector sponsored programs addressing some of the income disparaties amongst specific demographic groups. 
## Training Data
The census dataset consisting of personal, educational, locale, income and career demographics captured 32.561 rows of data. When performing the training and testing functions, the data was split by 80% training and 20% testing.
## Evaluation Data

## Metrics
Utilizing the Logistic Regression model, the model metrics are as follows:

Precision: 0.7110
Recall: 0.2576
F1: 0.3782

The model performed not ideally, contriubtors to this may have been bias in the data, convergence issues with the orignal solver whihch were resolved by implementing the "liblearner" solver and max iterations. Precision calculated 71% of the time accurately classifying the income category on the demographics provided, conversely 39% were inaccurately classified. Recall on the other hand calculated at 25% of accurately classifying those predicted that were accurate, yielding a less tha favorable result. Overall the F1 score was impacted substantially due to the poor performance of the Recall.

## Ethical Considerations
From an ethical perspective, while the data doesn't provide personal protected information, inferences into the data may lead to stereotypes gained through subjective rather than evaluation through objective reasoning.

## Caveats and Recommendations
Since this data is still gathered manually through surveys or interviews, the "human element" exists and therefore the potential for unintended bias. Any insights gained from the model would need to take that into consideration.

Since the Logistic Regression didn't perform as well as perhaps other models, it may be worthwhile to review other models or perhaps review and address an data bias.