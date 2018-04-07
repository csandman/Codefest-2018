import math
import json

    
def final_comp(p_user, users):
    
    #test_users = {'_id':'12345', '_revs':'idk','users':[{'_id':'1111','name':'lindsay','gender': 'F', 'attributes':{'personal':{'cleanliness':1,'outgoing':3,"nightlife":2},'desired':{'cleanliness':3,'outgoing':2,"nightlife":2},'importance':{'cleanliness':5,'outgoing':1,"nightlife":3}}}, {'_id':'2222','name':'cam','gender': 'M', 'attributes':{'personal':{'cleanliness':3,'outgoing':2,"nightlife":1},'desired':{'cleanliness':1,'outgoing':1,"nightlife":1},'importance':{'cleanliness':2,'outgoing':3,"nightlife":4}}}, {'_id':'1131','name':'steve','gender': 'M', 'attributes':{'personal':{'cleanliness':2,'outgoing':2,"nightlife":1},'desired':{'cleanliness':3,'outgoing':1,"nightlife":3},'importance':{'cleanliness':3,'outgoing':5,"nightlife":2}}}]}
    #scores = make_comparisons(test_users)
    
    a1, a2, a3 = clean_json(p_user[0])
    primary_user_id = p_user[0]['email']
    
    scores = make_comparisons(a1, a2, a3, primary_user_id, users)
    
    return scores
    
    
def comparison(a1, a2, a3, b1, b2, b3):
    
    numerator_a_sum = 0 
    denominator_a_sum = 0

    numerator_b_sum = 0 
    denominator_b_sum = 0
    
    for i in range(len(a1)):
        a1[i] = float(a1[i])
        a2[i] = float(a2[i])
        a3[i] = float(a3[i])
        b1[i] = float(b1[i])
        b2[i] = float(b2[i])
        b3[i] = float(b3[i])
        # person b score for a 
        denominator_b = b3[i]
        if (a1[i] <=  b2[i]):
            numerator_b = (a1[i]/b2[i]) * b3[i]
        else:
            numerator_b = denominator_b

        numerator_b_sum += numerator_b
        denominator_b_sum += denominator_b
        


        # person a score for b
        denominator_a = a3[i]
        if (b1[i] <= a2[i]):
            numerator_a = (b1[i]/a2[i]) * a3[i]
        else:
            numerator_a = denominator_a
            
        numerator_a_sum += numerator_a
        denominator_a_sum += denominator_a

    if denominator_a_sum != 0: 
        score_a = numerator_a_sum/denominator_a_sum
    else:
        score_a = 0
        
    if denominator_b_sum != 0: 
        score_b = numerator_b_sum/denominator_b_sum
    else:
        score_b = 0

##    print("person b's score in the eyes of a")
##    print("num:", numerator_a_sum, "denom:", denominator_a_sum)
##    print(score_a)
##
##    print("person a's score in the eyes of b")
##    print("num:", numerator_b_sum, "denom", denominator_b_sum)
##    print(score_b)

    questions = float(len(a1))
    mutual_score = ((score_a+score_b)/2)
    
    return score_a, score_b, mutual_score

def clean_json(user) :

    user_personal = list(user['attributes']['personal'].values())
    user_desired = list(user['attributes']['desired'].values())
    user_importance = list(user['attributes']['importance'].values())

    for i in range(len(user_personal)):
        if user_personal[i] == 1:
            user_personal[i] = 1
        elif user_personal[i] == 2:
            user_personal[i] = 10
        elif user_personal[i] == 3:
            user_personal[i] = 25
            
    for j in range(len(user_desired)):
        if user_desired[j] == 1:
            user_desired[j] = 1
        elif user_desired[j] == 2:
            user_desired[j] = 10
        elif user_desired[j] == 3:
            user_desired[j] = 25
            
    for k in range(len(user_importance)):
        if user_importance[k] == 1:
            user_importance[k] = 0
        elif user_importance[k] == 2:
            user_importance[k] = 1
        elif user_importance[k] == 3:
            user_importance[k] = 10
        elif user_importance[k] == 4:
            user_importance[k] = 50
        elif user_importance[k] == 5:
            user_importance[k] = 250
        
    return user_personal, user_desired, user_importance

        
def make_comparisons(a1, a2, a3, primary_user_id, user_list):
    
    final_list = []

    for user in user_list:
        scores = {}
        if user['email'] != primary_user_id:
            b1, b2, b3 = clean_json(user)
            score_a, score_b, mutual_score = comparison(a1, a2, a3, b1, b2, b3)
            scores["email"] = user['email']
            scores['rank'] = mutual_score
            final_list.append(scores)

    return final_list


            
            
        
        
        
        
    
