def severity_score(vehicle_type,
                   speed,
                   pedestrians,
                   school_zone,
                   night_time):


    score = 0


    score += speed*0.4


    score += pedestrians*8



    if school_zone:
        score += 30


    if night_time:
        score -= 10


    if vehicle_type=="bike":
        score += 10


    return max(0,min(score,100))



print(

severity_score(

vehicle_type="bike",

speed=50,

pedestrians=5,

school_zone=True,

night_time=False

)

)