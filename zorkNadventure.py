#Room 1

x = 0

while x == 0:
  print("You have entered a dark and spooky maze. You have an unopened bag of peanuts in your pocket. Travel 8 metres west, and there is a door. 2 miles north is a white elephant infront of a key, and 7 metres east is a treasure chest. There is another door directly behind you.\n")
  
  #I hear some elephants like peanuts
  
  answer = input("What would you like to do?")
  if "go north" in answer:
    print("There is a White Elephant")
    answer = input("What now?")
  
    if "move elephant" in answer:
      print ("You must be joking!")
    
    elif "lure elephant" in answer:
      answer = input("What do you wanna lure it with?")
      if "peanuts" in answer:
        print("The White Elephant moves towards the bag of peanuts, revealing a small key behind it.")
        answer = input("What now?")
    
    if "take all" in answer:
      print("Key taken")
      answer = input("Where would you like to go?")
      
      if "go east" in answer:
        print("There is a treasure chest")
        answer = input("What would you like to do now?")
        
        if "unlock chest" in answer:
          answer = input("What do you wanna unlock it with?")
          
          if "key" in answer:
            print("The chest has opened, inside the chest is a man in a suit with two identical keys with a skull handle surrounded by emerald snakes around his neck.")
            answer = input("Riddle me this, if you aim to give us a shot, we'll riddle you, what are we?")
            
            #Remember an episode of CollegeHumor when Batman faces the Riddler
            
            if "bullets" in answer:
              print("Correctamundo!")
              answer = input("In 1980, Pablo was 20, but in 1985, he was 15, how is this possible?")
              
              if "bc not ad" in answer:
                print("Very good.")
                answer = input("Poor people have it, rich people need it, if you eat it you die, it is greater than God, and it is worse than the Devil. What is it?")
              
                if "nothing" in answer:
                    print("Correct, here are the keys")
                    answer = input("What now?")
                    
                    #It is reccomended that you open the South door prior to opening the West door
                    
                    if "go south" in answer:
                      print("There is a door there")
                      answer = input("What do you wanna do?")
                      
                      if "unlock door" in answer:
                        answer = input("What do you wanna unlock it with?")
                      
                        if "key" in answer:
                          print("The door has been opened")
                          answer = input("What now?")
                          
                          if "go west" in answer:
                            print("There is another door")
                            answer = input("What do you wanna do?")
                            
                            if "unlock door" in answer:
                              answer = input("What do you wanna unlock it with?")
                              
                              if "key" in answer:
                                print("The door has been opened")
                              
                                x = 1
                              
                                input("\n\nPress Enter to exit!")
