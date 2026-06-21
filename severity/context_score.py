def calculate(


speed,


pedestrians,


vehicles,


night,


school,


rain

):



    score=0



    score+=speed*0.3


    score+=pedestrians*6


    score+=vehicles*4



    if school:

        score+=25



    if rain:

        score+=15



    if night:

        score-=10



    return min(score,100)