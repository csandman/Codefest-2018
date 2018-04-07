import math

def main():
    
    a1 = [25,1,25]
    a2 = [25,1,25]
    a3 = [250,0,10]

    b1 = [10,10,25]
    b2 = [10,10,25]
    b3 = [10,50,250]
    
    comparison(a1, a2, a3, b1, b2, b3)


def comparison(a1, a2, a3, b1, b2, b3):

    numerator_a_sum = 0 
    denominator_a_sum = 0

    numerator_b_sum = 0 
    denominator_b_sum = 0
    
    for i in range(3):
        
        # person b score for a 
        denominator_b = b3[i]
        numerator_b = (a1[i]/b2[i]) * b3[i]
        numerator_b_sum += numerator_b
        denominator_b_sum += denominator_b

        # person a score for b
        denominator_a = a3[i]
        numerator_a = (b1[i]/a2[i]) * a3[i]
        numerator_a_sum += numerator_a
        denominator_a_sum += denominator_a

    score_a = numerator_a_sum/denominator_a_sum
    score_b = numerator_b_sum/denominator_b_sum

    print("person b's score in the eyes of a")
    print("num:", numerator_a_sum, "denom:", denominator_a_sum)
    print(score_a)

    print("person a's score in the eyes of b")
    print("num:", numerator_b_sum, "denom", denominator_b_sum)
    print(score_b)

    questions = len(a1)

    mutual_score = (score_a*score_b)**(1/questions)

    print(mutual_score)
    
    

main()
            
            
        
        
        
        
    
