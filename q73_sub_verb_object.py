subject = ["I","You"]
verb = ["Play","Love"]
object = ["Hockey","Football"]

for i in range(len(subject)):
    for j in range(len(verb)):
        for k in range(len(object)):
            sentence = "%s %s %s." % (subject[i], verb[j], object[k])
            print(sentence)
            
