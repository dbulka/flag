def flag(N):
    print("N = ", N)
    if N%2 != 0:
        N += 1
    #flag_list variable for saving each sting of flag
    flag_list = []

    #width of flag without excluding # borders, I'd define as separate function
    width = []
    for l in range(0, 3*N+2):
        width.append("#")
    flag_list.append(width)

    #create up-part of flag without circle, I'd define as separate function
    for x in range(0,int(N/2)):
        string = []
        for l in range(0, 3*N+2):
            string.append(" ")
        string[0] = "#"
        string[-1] = "#"
        flag_list.append(string)
    flag_circle = []
    # create loop for half cirle stings
    for x in range(0, int(N/2)):

    # create up-part of flag with circle, i think better define as function
        c = 3*N/2 - N
        i = 0
        # for i in
        string = []
        for i in range(0, (N+1+x)):
            string.append(" ")

        string.append("*")
        for i in range(0, (N-2-x*2)):
            string.append("o")
        string.append("*")

        for i in range(0, (N+1+x)):
            string.append(" ")
        string[0] = "#"
        string[-1] = "#"
        flag_circle.append(string)

    # make whole flag by adding up-part to reversed up-part (get bottom part)
    flag_circle.reverse()
    flag_list.extend(flag_circle)
    flag_up_part = flag_list.copy()
    flag_list.reverse()
    flag_list = flag_up_part + flag_list

    #transform flag to sting
    flag_string = ""
    for i in flag_list:
        string = ""
        for x in i:
            string += str(x)

        flag_string += str(string) + "\n"
    print(flag_string)
try:
    number = int(input('please enter N: '))
    flag(number)
except:
    raise ArgumentError

