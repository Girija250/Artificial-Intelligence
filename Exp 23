% Facts: disease(Name, SuggestedDiet)
disease(diabetes, low_sugar_diet).
disease(hypertension, low_sodium_diet).
disease(obesity, low_calorie_diet).
disease(anemia, iron_rich_diet).
disease(gastritis, bland_diet).

% Diet details
diet(low_sugar_diet, [vegetables, whole_grains, legumes, lean_meat]).
diet(low_sodium_diet, [fruits, vegetables, low_sodium_foods]).
diet(low_calorie_diet, [salads, fruits, oats, grilled_fish]).
diet(iron_rich_diet, [spinach, red_meat, beans, dried_fruits]).
diet(bland_diet, [boiled_rice, bananas, plain_bread, applesauce]).

% Rule to suggest a diet plan based on disease
suggest_diet(Disease, DietPlan) :-
    disease(Disease, Plan),
    diet(Plan, DietPlan).
