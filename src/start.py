import re
from data import travel_cards, dining_data



def convert_spend_cap(spend_cap):
    if "no cap" in spend_cap.lower():
        return float('inf')  # Representing no cap with infinity
    else:
        # Using regex for a concise replacement
        cleaned_spend_cap = re.sub(r'[\$,/quarter,/month,/ month,/ quarter,/ year,]', '', spend_cap)
        return float(cleaned_spend_cap)
    

def calculate_cashback(spending, card, string_name, num_years=1):
    max_cap = convert_spend_cap(card["Spend Cap"])
    
    if max_cap != float('inf'):
        if '/ month' in card["Spend Cap"].lower():
            annual_spending = spending * 12
        elif '/ year' in card["Spend Cap"].lower():
            annual_spending = spending * 1
        elif '/ quarter' in card["Spend Cap"].lower():
            annual_spending = spending * 4 
        
        max_cap = (float(max_cap) * 12 if '/ month' in card["Spend Cap"].lower() else float(max_cap) * 4)
        
        if annual_spending > max_cap * num_years:
            cashback_within_cap = max_cap * card[f"{string_name}"] / 100
            cashback_beyond_cap = (annual_spending - (max_cap * num_years)) * 0.01  # 1% cashback on the rest
                        
            return cashback_within_cap + cashback_beyond_cap + card["SUB"]
    
    return ((float(spending)*12) * card[f"{string_name}"] / 100) * num_years + card["SUB"]


def find_best_card(spending, tf_sub, data, string_name):
    best_cards = []
    max_cashbacks = [0, 0, 0, 0, 0,0, 0, 0, 0, 0]  # List to store the top 3 cashback values

    if tf_sub:
        for card in data:
            card["SUB"] = card["SUB"]
            cashback = calculate_cashback(spending, card, string_name)

            for i in range(10):
                if cashback > max_cashbacks[i]:
                    max_cashbacks.insert(i, cashback)
                    best_cards.insert(i, card['Card Name'])
                    break
    else:
        for card in data:
            card["SUB"] = 0
            cashback = calculate_cashback(spending, card, string_name)

            for i in range(10):
                if cashback > max_cashbacks[i]:
                    max_cashbacks.insert(i, cashback)
                    best_cards.insert(i, card['Card Name'])
                    break

    return best_cards[:10], max_cashbacks[:10]


#Options
# "Dining CB"
# "Travel CB" 
# dining_data
# travel_data
string_name = "Dining CB"
data = dining_data


user_responses = {
    "Gas": 200,
    "Supermarket": 300,
    "Dining": 1600,
    "Travel": 600,
    "Other": 100
}


spending = user_responses["Dining"]
tf_sub =  True
best_card_with_sub, max_cashback_sub= find_best_card(spending, tf_sub , data, string_name)
tf_sub =  False 
best_card_without_sub,max_cashback_no_sub = find_best_card(spending, tf_sub, data, string_name)

print(spending, max_cashback_sub)
print(spending,max_cashback_no_sub)


    
print("Best card with SUB:", best_card_with_sub)
print("Best card without SUB:", best_card_without_sub)



