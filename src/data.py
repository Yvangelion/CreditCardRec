
# removing some cards with extreame pre reqs like 1 mil invested for BOA.  
travel_cards = [
    #{"Travel CB": 5.55, "Travel Types": "Most Travel", "Spend Cap": "$500/ month", "Bank Name": "Citi", "Card Name": "Custom Cash", "Type": "MC", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open, req. Rewards+ card [A]"},
    #{"Travel CB": 5.25, "Travel Types": "Most Travel", "Spend Cap": "$2,500/ quarter", "Bank Name": "Bank of America", "Card Name": "Customized Cash", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open, req. $100k [B]"},
    {"Travel CB": 5, "Travel Types": "Airfare, Hotels", "Spend Cap": "No Cap", "Bank Name": "GreenState CU", "Card Name": "World Mastercard", "Type": "MC", "SUB": 100, "FTF": 0, "Travel Benefits": "Car Rental CDW", "Membership": "Am. Cons. Counc., $5 [C]"},
    {"Travel CB": 5, "Travel Types": "Prepaid Portal Only", "Spend Cap": "No Cap", "Bank Name": "Chase", "Card Name": "Freedom Flex", "Type": "MC", "SUB": 200, "FTF": 3, "Travel Benefits": "Car Rental CDW; Trip Cancell./ Interrup. Insurance", "Membership": "Open"},
    {"Travel CB": 5, "Travel Types": "Prepaid Portal Only", "Spend Cap": "No Cap", "Bank Name": "Chase", "Card Name": "Freedom Unlimited", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "Car Rental CDW; Trip Cancell./ Interrup. Insurance", "Membership": "Open"},
    {"Travel CB": 5, "Travel Types": "Ground Transp. plus Prepaid Portal", "Spend Cap": "$2,000/ quarter (No Cap for Portal)", "Bank Name": "U.S. Bank", "Card Name": "Cash+", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open"},
    {"Travel CB": 5, "Travel Types": "Prepaid Portal Only", "Spend Cap": "No Cap", "Bank Name": "U.S. Bank (Elan)", "Card Name": "Max Cash Preferred", "Type": "Visa/MC", "SUB": 150, "FTF": 3, "Travel Benefits": "None", "Membership": "Open"},
    {"Travel CB": 5, "Travel Types": "Most Travel", "Spend Cap": "$500/ month", "Bank Name": "Citi", "Card Name": "Custom Cash", "Type": "MC", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open"},
    #{"Travel CB": 4.5, "Travel Types": "Most Travel", "Spend Cap": "$2,500/ quarter", "Bank Name": "Bank of America", "Card Name": "Customized Cash", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open, req. $50k [B]"},
    {"Travel CB": 4, "Travel Types": "Most Travel", "Spend Cap": "$7,000/ quarter", "Bank Name": "Huntington", "Card Name": "Voice Business", "Type": "MC", "SUB": 0, "FTF": 0, "Travel Benefits": "None", "Membership": "7 States [D]"},
    #{"Travel CB": 3.75, "Travel Types": "Most Travel", "Spend Cap": "$2,500/ quarter", "Bank Name": "Bank of America", "Card Name": "Customized Cash", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open, req. $20k [B]"},
    #{"Travel CB": 3.4, "Travel Types": "Most Travel + Global Entry", "Spend Cap": "No Cap", "Bank Name": "PenFed", "Card Name": "Pathfinder Rewards", "Type": "Visa", "SUB": 425, "FTF": 0, "Travel Benefits": "Baggage Loss/Delay Insurance, Travel Accident Insurance, Trip Cancell./ Interrup. Insurance", "Membership": "$5, req. checking and $500 or direct deposit [E]"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "Wells Fargo", "Card Name": "Autograph", "Type": "Visa", "SUB": 200, "FTF": 0, "Travel Benefits": "Car Rental CDW", "Membership": "Open"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "Comenity", "Card Name": "AAA Travel Advantage", "Type": "Visa", "SUB": 100, "FTF": 0, "Travel Benefits": "None", "Membership": "Open (AAA membership not req.)"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "InFirst FCU", "Card Name": "Visa Rewards", "Type": "Visa", "SUB": 15, "FTF": "Unk.", "Travel Benefits": "Baggage Loss/Delay Insurance, Travel Accident Insurance", "Membership": "Open, $20 [F]"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "FNBO", "Card Name": "Getaway", "Type": "MC", "SUB": 0, "FTF": 0, "Travel Benefits": "None", "Membership": "Open"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "Synchrony", "Card Name": "Venmo Visa", "Type": "Visa", "SUB": 0, "FTF": 0, "Travel Benefits": "None", "Membership": "Venmo"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "No Cap", "Bank Name": "Citi", "Card Name": "Costco Anywhere", "Type": "Visa", "SUB": 0, "FTF": 0, "Travel Benefits": "Car Rental CDW, Travel Accident Insurance", "Membership": "Costco, $60+ [G]"},
    {"Travel CB": 3, "Travel Types": "Airfare, Hotels, Car Rentals", "Spend Cap": "No Cap", "Bank Name": "Barclays", "Card Name": "AARP Travel Rewards", "Type": "MC", "SUB": 100, "FTF": 0, "Travel Benefits": "Baggage Loss/Delay Insurance, Car Rental CDW, Travel Accident Insurance, Trip Cancell./ Interrup. Insurance", "Membership": "Open (AARP membership not req.)"},
    {"Travel CB": 3, "Travel Types": "Most Travel + Global Entry", "Spend Cap": "No Cap", "Bank Name": "Summit CU", "Card Name": "Ultimate CashPerks", "Type": "Visa", "SUB": 0, "FTF": 0, "Travel Benefits": "None", "Membership": "Open, $5 [H]"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "$2,500/ quarter", "Bank Name": "Bank of America", "Card Name": "Customized Cash", "Type": "Visa", "SUB": 200, "FTF": 3, "Travel Benefits": "None", "Membership": "Open"},
    {"Travel CB": 3, "Travel Types": "Most Travel", "Spend Cap": "$2,000/ quarter", "Bank Name": "Huntington", "Card Name": "Voice Rewards", "Type": "MC", "SUB": 0, "FTF": 0, "Travel Benefits": "None", "Membership": "7 States [I]"}
]



dining_data = [
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Capital One",
        "Card Name": "SavorOne",
        "SUB": 200,
        "FTF": "No FTF",
        "Other Category": "Y [M]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa/ MC",
        "Bank Name": "Navy FCU",
        "Card Name": "Go Rewards",
        "SUB": 200,
        "FTF": "No FTF",
        "Other Category": "N [N]",
        "Membership": "NFCU, $5 [N]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "UMB",
        "Card Name": "Simply Rewards",
        "SUB": 150,
        "FTF": "2%",
        "Other Category": "Y [O]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "TD Bank",
        "Card Name": "Cash",
        "SUB": 150,
        "FTF": "3%",
        "Other Category": "N [P]",
        "Membership": "15 States + D.C. [P]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Comenity",
        "Card Name": "AAA Travel Advantage",
        "SUB": 100,
        "FTF": "No FTF",
        "Other Category": "Y [Q]",
        "Membership": "Open (AAA membership not req.)"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Synchrony",
        "Card Name": "Verizon Visa",
        "SUB": 100,
        "FTF": "No FTF",
        "Other Category": "Y [R]",
        "Membership": "Verizon Wireless [R]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Cardless",
        "Card Name": "Cavs Card",
        "SUB": 50,
        "FTF": "No FTF",
        "Other Category": "Y [S]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Cardless",
        "Card Name": "Celtics Card",
        "SUB": 50,
        "FTF": "No FTF",
        "Other Category": "Y [T]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Cardless",
        "Card Name": "Marlins Card",
        "SUB": 50,
        "FTF": "No FTF",
        "Other Category": "Y [U]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Cardless",
        "Card Name": "Pelicans Card",
        "SUB": 50,
        "FTF": "No FTF",
        "Other Category": "Y [V]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Synchrony",
        "Card Name": "Sam's Club Mastercard",
        "SUB": 30,
        "FTF": "No FTF",
        "Other Category": "Y [W]",
        "Membership": "Sam's Club, $45+ [W]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "AmEx",
        "Bank Name": "USAA",
        "Card Name": "Rewards",
        "SUB": 25,
        "FTF": "No FTF",
        "Other Category": "N [X]",
        "Membership": "USAA [X]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "InFirst FCU",
        "Card Name": "Visa Rewards",
        "SUB": 15,
        "FTF": "Unk.",
        "Other Category": "Y [Y]",
        "Membership": "Open, $20 [Y]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "FNBO",
        "Card Name": "Getaway",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [Z]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Synchrony",
        "Card Name": "Venmo Visa",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [AA]",
        "Membership": "Venmo"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "MC",
        "Bank Name": "Bank of the West",
        "Card Name": "Cash Back World",
        "SUB": 0,
        "FTF": "3%",
        "Other Category": "Y [BB]",
        "Membership": "Open Except D.C."
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Synovus",
        "Card Name": "Cash Rewards",
        "SUB": 0,
        "FTF": "3%",
        "Other Category": "Y [CC]",
        "Membership": "6 States [CC]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Redstone FCU",
        "Card Name": "Rural King Card",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [DD]",
        "Membership": "Open, $5 [DD]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "AmEx",
        "Bank Name": "Navy FCU",
        "Card Name": "More Rewards",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [EE]",
        "Membership": "NFCU, $5 [EE]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "No Cap",
        "Type": "Visa",
        "Bank Name": "Citi",
        "Card Name": "Costco Anywhere",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [FF]",
        "Membership": "Costco, $60+ [FF]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "$2,500/ quarter",
        "Type": "Visa",
        "Bank Name": "Bank of America",
        "Card Name": "Customized Cash",
        "SUB": 200,
        "FTF": "3%",
        "Other Category": "Y [B]",
        "Membership": "Open"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "$8,000/ year",
        "Type": "Visa",
        "Bank Name": "PNC",
        "Card Name": "Cash Rewards",
        "SUB": 200,
        "FTF": "3%",
        "Other Category": "Y [GG]",
        "Membership": "25 States + D.C. [GG]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "$2,000/ quarter",
        "Type": "MC",
        "Bank Name": "Huntington",
        "Card Name": "Voice Rewards",
        "SUB": 0,
        "FTF": "No FTF",
        "Other Category": "Y [HH]",
        "Membership": "7 States [HH]"
    },
    {
        "Dining CB": 3,
        "Spend Cap": "$6,000/ year",
        "Type": "MC",
        "Bank Name": "U.S. Bank",
        "Card Name": "Various Kroger-branded cards",
        "SUB": 100,
        "FTF": "No FTF",
        "Other Category": "Y [C]",
        "Membership": "Open"
    }
]

