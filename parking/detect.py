vehicle_present = True


time_stationary = 150



if vehicle_present:


    if time_stationary > 120:


        print()


        print("Illegal Parking Detected")


        print("Stationary Time :", time_stationary)


    else:


        print("Normal Parking")