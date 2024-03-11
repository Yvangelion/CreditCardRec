import re
from src.credit_list import *
from  config import TEST_MODE

def convert_spend_cap(spend_cap):
    if "no cap" in spend_cap.lower():
        return float('inf')  # Representing no cap with infinity
    else:
        # Using regex for a concise replacement
        cleaned_spend_cap = re.sub(r'[\$,/quarter,/month,/ month,/ quarter,/ year,]', '', spend_cap)
        return float(cleaned_spend_cap)
    

def calculate_cashback(spending, card, string_name, num_years=1):
    #print(card)
    
    fee = card.get("Annual Fee", 0)
    credits_possible = card.get("Credits", 0)
        
    if "Spend Cap" in card:
        max_cap = convert_spend_cap(card["Spend Cap"])
    else:
        max_cap = float('inf')
    
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
                        
            return cashback_within_cap + cashback_beyond_cap + card["SUB"] - fee + credits_possible
    
    return ((float(spending)*12) * card[f"{string_name}"] / 100) * num_years + card["SUB"] - fee + credits_possible


def find_best_card(spending, tf_sub, data, string_name):
    #print(data)
    best_cards = []
    max_cashbacks = [0, 0, 0, 0, 0,] 
    if tf_sub:
        for card in data:
            
            if isinstance(card["SUB"], str):
                if card["SUB"].lower() == "no sub":
                    card["SUB"] = 0
                elif card["SUB"].lower() != "no sub":
                    card["SUB"] = 0
                else:
                    card["SUB"] = float(card["SUB"])
                    
            elif isinstance(card["SUB"], int) or isinstance(card["SUB"], float):
                card["SUB"] = float(card["SUB"])
            else:
                card["SUB"] = 0
                
            cashback = calculate_cashback(spending, card, string_name)

            for i in range(len(data)):
                print(i)
                if cashback > max_cashbacks[i]:
                    max_cashbacks.insert(i, cashback)
                    best_cards.insert(i, card['Card Name'])
                    break
    else:
        for card in data:
            card["SUB"] = 0
            cashback = calculate_cashback(spending, card, string_name)

            for i in range(len(data)):
                if cashback > max_cashbacks[i]:
                    max_cashbacks.insert(i, cashback)
                    best_cards.insert(i, card['Card Name'])
                    break

    cards_cashbacks_dict = dict(zip(best_cards, max_cashbacks))
    return best_cards[:5], max_cashbacks[:5], cards_cashbacks_dict

def credit_app(user_responses):
    if TEST_MODE == True:
        user_responses = {
            "Gas": 200,
            "Supermarket": 300,
            "Dining": 300,
            "Travel": 400,
            "Other": 1000
        }
    else:
        pass


    categories = ["Dining", "Travel", "Other"]

    best_dining = [] 
    best_travel = []
    best_other = []

    for category in categories:
        
        if category == "Dining":
            data = dining_data
            string_name = f"{category} CB"
            
        elif category == "Travel":
            data = travel_cards
            string_name = f"{category} CB"
            
        elif category == "Other":
            data = other_cards
            string_name = "CB"
            
        spending = user_responses[category]

        tf_sub = True
        best_card_with_sub, max_cashback_sub, cards_cashbacks_dict = find_best_card(spending, tf_sub, data, string_name)

        tf_sub = False
        best_card_without_sub, max_cashback_no_sub, cards_cashbacks_dict_no_sub = find_best_card(spending, tf_sub, data, string_name)
        
        
        if category == "Dining":
            best_dining.append(cards_cashbacks_dict)
            
        elif category == "Travel":
            best_travel.append(cards_cashbacks_dict)
                
        elif category == "Other":
            best_other.append(cards_cashbacks_dict)
            



        print(category)
        print("----------------------------------------------------------")
        print("Best card with sub:", best_card_with_sub[0])
        print("Best card with NO sub:", best_card_without_sub[0])
        print(f"Category: {category}, Spending: {spending * 12}, Max Cashback with SUB: {max_cashback_sub}")
        print(f"Category: {category}, Spending: {spending * 12}, Max Cashback without SUB: {max_cashback_no_sub}")

        print("Cards ranked with SUB:", best_card_with_sub)
        print("Cards ranked without SUB:", best_card_without_sub)
        print("Rankings")
        for g, (key, value) in enumerate(cards_cashbacks_dict.items(), 1):
            if g <= 10:
                print(f"{g}: {key} - {value}")
                    
        print(" ")

            


    merged_dict = {}
    for category in [best_dining, best_travel, best_other]:
        for d in category:
            for key, value in d.items():
                if key in merged_dict:
                    merged_dict[key] += round(value, 2)
                else:
                    merged_dict[key] = round(value, 2)

    # Sort the merged dictionary by keys and print the result
    sorted_merged_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1], reverse=True))

    for x, (key, value) in enumerate(sorted_merged_dict.items(), 1):
        if x <= 10:
            print(f"{x}: {key} - {value}")
    
    return sorted_merged_dict