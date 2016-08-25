import time
import sys
def big_kpiLine_function():
    print("\nProcessing....\n")
    time.sleep(1)
    print("All table column names will be shown in order, please enter a value for each column when prompted\nPlease note that in this mode there are no input restrictions.\nBe mindfull that your input is correct")
    print("\nProcessing....\n")
    time.sleep(0.3)
    c_KPI_lvl = input("KPI_LEVEL")

def kpi_empty_Line():

    kpi_ID = input("Enter the KPI_ID: ")
    kpi_Level = "'', "
    kpi_Value = "'', "
    kpi_name = "'', "
    unit = "'', "
    intern = 0
    target = 0
    deleted = 0
    start_Date = "'', "
    end_Date = "'', "
    category = "'') "
    standard_KPI_line = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values("
    prompted_KPI_LINE = standard_KPI_line + str(kpi_ID) + ", " + kpi_Level + kpi_Value + kpi_name + unit +  str(intern) + ", " + str(target) + ", "  +  str(deleted) + ", " + start_Date + end_Date + category
    cluster_List = ['PON Inbound', 'PON Outbound', 'PON Security & Service', 'PON Automerken', ]

def kpi_choice_AHT():
    aht_target = 0
    try:
        print("Please enter the target for the AHT, valid options are:\nAny number\n")
        time.sleep(1)
        aht_Target = int(input("Enter value: "))

        while aht_Target < 0:
            print("Invalid value")
            time.sleep(1)
            print("Please enter the target for the AHT, valid options are:\nAny number\n")
            time.sleep(1)
            aht_Target = int(input("Enter value: "))
    except:
        time.sleep(1)
        print("Please enter a number above -1, and no strings!\n")
        time.sleep(1)
        kpi_choice_AHT()
    return  aht_Target

def kpi_choice_fcr_target():
    print("Please enter the target for the [FCR], valid options are:\n0\n1\n2\n3\n4\n")
    time.sleep(1)
    fcr_Target = str(input("Enter value: "))

    while fcr_Target != "0" and fcr_Target != "1" and fcr_Target != "2" and fcr_Target != "3" and fcr_Target != "4":
        print("\nInvalid value\n")
        time.sleep(1)
        kpi_choice_fcr_target()
        break

    return fcr_Target

def kpi_choice_fcr_direction():
    print("Please enter the direction for the [FCR] valid options are:\nRECUR\nFCR\n")
    time.sleep(1)
    fcr_Direction = ""
    fcr_Direction = input("Enter value: ")


    while fcr_Direction != "RECUR" and fcr_Direction != "FCR":
        print("\nInvalid value\n")
        time.sleep(1)
        kpi_choice_fcr_direction()
        break

    return fcr_Direction

def kpi_choice_SL_Level():
    print("Please enter the level for the SL, valid values are:\n0\n1\n2\n3\n4\n")
    time.sleep(1)
    sl_Level = input("Enter value: ")
    while sl_Level != "0" and sl_Level != "1" and sl_Level != "2" and sl_Level != "3" and sl_Level != "4":
        print("\nInvalid value\n")
        time.sleep(1)
        print("Please enter the level for the SL, valid values are:\n0\n1\n2\n3\n4\n")
        time.sleep(1)
        sl_Level = input("Enter value: ")
    return sl_Level

def kpi_choice_SL_Percentage():
    sl_Percentage = float(0)
    try:
        print("Please enter the target percentage for SL, valid values Are:\nA decimal number between 0.0 and 1.0\n")
        time.sleep(1)
        sl_Percentage = float(input("Enter value:"))
        while sl_Percentage < float(0.0) or sl_Percentage > float(1.0):
            print("\nInvalid value\n")
            time.sleep(1)
            print("Please enter the target percentage for SL, valid values Are:\nA decimal number between 0.0 and 1.0\n")
            time.sleep(1)
            sl_Percentage = float(input("Enter value:"))
    except:
        time.sleep(1)
        print("Please enter a decimal number between 0,0 and 1,0")
        time.sleep(1)
        kpi_choice_SL_Percentage()
    return sl_Percentage

def kpi_choice_answer_Percentage():
    answer_percentage = float(0)
    try:
        print("Please enter the target percentage for Answer, valid values are:\nA decimal number between 0.0 and 1.0\n")
        time.sleep(1)
        answer_percentage = float(input("Enter value:"))
        while answer_percentage < float(0.0) or answer_percentage > float(1.0):
            print("\nInvalid value\n")
            time.sleep(1)
            kpi_choice_answer_Percentage()
            break
    except:
        time.sleep(1)
        print("Please enter a decimal number between 0,0 and 1,0")
        time.sleep(1)
        kpi_choice_answer_Percentage()
    return answer_percentage

def n_clusters_loop():
    clusters_n = 0
    print("How many clusters would you like to insert?\n")
    try:
        clusters_n = int(input("Enter value: \n"))
        if clusters_n == "EXIT":
            print("Thank you, bye bye")
            time.sleep(1)
            return 0;
        else:
            return clusters_n
    except:
        time.sleep(1)
        print("\nInvalid value!\n Please enter a number: ")
        n_clusters_loop()
    return clusters_n

def choice_1():
    choice = "1"
    import time
    kpi_id_2 = 0
    try:
        print("Processing.....\n")
        time.sleep(1)
        kpi_id_2 = int(input("Please enter the most recent KPI ID: "))
        if kpi_id_2 == "EXIT":
            print("Thank you, bye bye")
            time.sleep(1)
            return 0
        else:
            print("\nProcessing.....\n")
            time.sleep(0.6)
    except:
        time.sleep(0.6)
        print("Please enter a number")
        time.sleep(0.3)
        choice_1()

    if choice == "EXIT":
        print("Thank you, bye bye")
        return 0
    else:

        return kpi_id_2
    return kpi_id_2

def n_clusterloop():
    n_clusters = n_clusters_loop()
    cL = 0
    cluster_list3 = [""] * n_clusters
    print("\nPlease enter the cluster names you would like to insert\n ")
    time.sleep(0.2)
    for c in range(0, (n_clusters)):
        cluster_list3[cL] = str(input("Cluster:"))
        time.sleep(0.2)
        cL = cL + 1
        if "EXIT" in cluster_list3:
            print("Thank you bye bye")
            sys.exit()
        elif "DONE" in cluster_list3:

            break
        else:
            continue
    return cluster_list3

def print_clusterset():

    kpi_id_2 = choice_1()
    cluster_list3 = n_clusterloop()
    fcr_Direction = kpi_choice_fcr_direction()
    fcr_Target = kpi_choice_fcr_target()
    aht_Target = kpi_choice_AHT()
    sl_Level = kpi_choice_SL_Level()
    sl_Percentage = kpi_choice_SL_Percentage()
    answer_Percentage = kpi_choice_answer_Percentage()





    for x, cluster_list3 in enumerate(cluster_list3):

        kpi_FCR_direction = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'Direction'," "'" + str(fcr_Direction) + "'" + ", 1, 0, 0, '01/01/2014', '31/12/9999', 'FCR');"
        kpi_id_2 += 1
        kpi_FCR_days = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'Period', 'Frequency', 1, " + str(fcr_Target)  + ", 0, '01/01/2014', '31/12/9999', 'FCR');"
        kpi_id_2 += 1
        kpi_AHT = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'AHT', 'Seconds', 1, " + str(aht_Target) + ", 0, '01/01/2014', '31/12/9999', 'Call')"
        kpi_id_2 += 1
        kpi_SL_level = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'Level', 'Percentage', 1, " + str(sl_Level) + ", 0, '01/01/2014', '31/12/9999', 'Serviclevel');"
        kpi_id_2 += 1
        kpi_SL_target = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'Percentage', 'Percentage', 1, " + str(sl_Percentage) + ", 0, '01/01/2014', '31/12/9999','Servicelevel');"
        kpi_id_2 += 1
        kpi_answer_perc = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_id_2) + "', 'Cluster', '" + str(cluster_list3) + "', 'Answer', 'Percentage', 1, " +  str(answer_Percentage) + ", 0, '01/01/2014', '31/12/9999', 'Call');"
        kpi_id_2 += 1
        result_File = open('TITO File', 'w')
        print(kpi_FCR_direction, file = open("Tito_Results",'a'))
        print(kpi_FCR_days,file = open("Tito_Results",'a'))
        print(kpi_AHT,file = open("Tito_Results",'a'))
        print(kpi_SL_level,file = open("Tito_Results",'a'))
        print(kpi_SL_target,file = open("Tito_Results",'a'))
        print(kpi_answer_perc,file = open("Tito_Results",'a'))

    print("Writing file.....\n")
    time.sleep(5)
    print("Writing succesful!\n")
    complete1 = input("To exit the program enter: EXIT, to go back to the beginning of the program, enter: RESTART\n")
    time.sleep(0.2)

    if complete1 == "EXIT":
            return 0
    elif complete1 == "RESTART":
        tito_KPI_Program_startup()
    else:
        while complete1 != "EXIT" and complete1 != "RESTART":
            complete1 = input("Please enter a valid value: ")
        if complete1 == "EXIT":
            return 0
        elif complete1 == "RESTART":
                tito_KPI_Program_startup()

def choice_2_FCR():

    kpi_ID = "0"
    cluster_List = ""
    print("Welcome to the FCR printing enviroment, here you can produce FCR SQL lines to insert FCR KPI lines\n")
    input("Press Enter to continue....\n")
    time.sleep(0.3)
    kpi_ID = choice_1()
    time.sleep(2)
    FCR_Cluster_List = n_clusterloop()
    time.sleep(2)
    t_Choice = input("Will you use the same kpi values for all those clusters? \n\nEnter: YES, or NO\n\nEnter value:  ")
    print("\nProcessing....\n")
    time.sleep(1.3)
    if t_Choice == "YES":
        print("\nProcessing....\n")
        time.sleep(0.5)
        print("All entered values will be used for all clusters...\n")
        time.sleep(0.5)
        fcr_Direction = kpi_choice_fcr_direction()
        fcr_Target = kpi_choice_fcr_target()
        open("Tito_File2", "w")
        for x, FCR_Cluster_List in enumerate(FCR_Cluster_List):
            standard_Line_FCR_range = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(FCR_Cluster_List) + "', 'Direction'," "'" + str(fcr_Direction) + "'" + ", 1, 0, 0, '01/01/2014', '31/12/9999', 'FCR');"
            kpi_ID += 1
            standard_Line_FCR_direction = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(FCR_Cluster_List) + "', 'Period', 'Frequency', 1, " + str(fcr_Target) + ", 0, '01/01/2014', '31/12/9999', 'FCR');"
            kpi_ID += 1

            print(standard_Line_FCR_range, file=open("Tito_File2", "a"))
            print(standard_Line_FCR_direction, file=open("Tito_File2", "a"))

    elif t_Choice == "NO":
        open("Tito_File2", "w")
        for x, FCR_Cluster_List in enumerate(FCR_Cluster_List):

            print("Enter values for: " + FCR_Cluster_List + "\n")
            fcr_Direction = kpi_choice_fcr_direction()
            fcr_Target = kpi_choice_fcr_target()

            standard_Line_FCR_range = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(FCR_Cluster_List) + "', 'Direction'," "'" + str(fcr_Direction) + "'" + ", 1, 0, 0, '01/01/2014', '31/12/9999', 'FCR');"
            kpi_ID += 1
            standard_Line_FCR_direction = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(FCR_Cluster_List) + "', 'Period', 'Frequency', 1, " + str(fcr_Target) + ", 0, '01/01/2014', '31/12/9999', 'FCR');"
            kpi_ID += 1

            print(standard_Line_FCR_range, file=open("Tito_File2", "a"))
            print(standard_Line_FCR_direction, file=open("Tito_File2", "a"))

    print("Writing file.....\n")
    time.sleep(5)
    print("Writing succesful!\n")
    complete1 = input("To exit the program enter: EXIT, to go back to the beginning of the program, enter: RESTART\n")
    time.sleep(0.2)

def choice_2_AHT():

    kpi_ID = "0"
    cluster_List = ""
    print("Welcome to the AHT printing enviroment, here you can produce AHT SQL lines to insert AHT KPI lines\n")
    input("Press Enter to continue....\n")
    time.sleep(0.3)
    kpi_ID = choice_1()
    time.sleep(2)
    AHT_Cluster_List = n_clusterloop()
    time.sleep(2)
    t_Choice = input("Will you use the same kpi values for all those clusters? \n\nEnter: YES, or NO\n\nEnter value:  ")
    print("\nProcessing....\n")
    time.sleep(1.3)
    if t_Choice == "YES":
        print("\nProcessing....\n")
        time.sleep(0.5)
        print("All entered values will be used for all clusters...\n")
        time.sleep(0.5)
        aht_Target = kpi_choice_AHT()
        open("Tito_File2", "w")
        for x, AHT_Cluster_List in enumerate(AHT_Cluster_List):

            standard_Line_AHT_Target = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(AHT_Cluster_List) + "', 'AHT', 'Seconds', 1, " + str(aht_Target) + ", 0, '01/01/2014', '31/12/9999', 'Call');"
            kpi_ID += 1
            print(standard_Line_AHT_Target, file=open("Tito_File2", "a"))


    elif t_Choice == "NO":
        open("Tito_File2", "w")
        for x, AHT_Cluster_List in enumerate(AHT_Cluster_List):
            print("Enter value for: " + AHT_Cluster_List + "\n")
            aht_Target = kpi_choice_AHT()
            standard_Line_AHT_Target = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(AHT_Cluster_List) + "', 'AHT', 'Seconds', 1, " + str(aht_Target) + ", 0, '01/01/2014', '31/12/9999', 'Call');"
            kpi_ID += 1
            print(standard_Line_AHT_Target, file=open("Tito_File2", "a"))


    print("Writing file.....\n")
    time.sleep(5)
    print("Writing succesful!\n")
    complete1 = input("To exit the program enter: EXIT, to go back to the beginning of the program, enter: RESTART\n")
    time.sleep(0.2)

def choice_2_Answer():

    kpi_ID = "0"
    cluster_List = ""
    print("Welcome to the ANSWER printing enviroment, here you can produce ANSWER SQL lines to insert ANSWER KPI lines\n")
    input("Press Enter to continue....\n")
    time.sleep(0.3)
    kpi_ID = choice_1()
    time.sleep(2)
    answer_Cluster_List = n_clusterloop()
    time.sleep(2)
    t_Choice = input("Will you use the same kpi values for all those clusters? \n\nEnter: YES, or NO\n\nEnter value:  ")
    print("\nProcessing....\n")
    time.sleep(1.3)
    if t_Choice == "YES":
        print("\nProcessing....\n")
        time.sleep(0.5)
        print("All entered values will be used for all clusters...\n")
        time.sleep(0.5)
        answer_Target = kpi_choice_answer_Percentage()
        open("Tito_File2", "w")
        for x, answer_Cluster_List in enumerate(answer_Cluster_List):
            standard_Line_Answer_Target = kpi_answer_perc = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(answer_Cluster_List) + "', 'Answer', 'Percentage', 1, " +  str(answer_Target) + ", 0, '01/01/2014', '31/12/9999', 'Call');"
            kpi_ID += 1
            print(standard_Line_Answer_Target, file=open("Tito_File2", "a"))


    elif t_Choice == "NO":
        open("Tito_File2", "w")
        for x, answer_Cluster_List in enumerate(answer_Cluster_List):
            print("Enter value for: " + answer_Cluster_List + "\n")
            time.sleep(0.7)
            answer_Target = kpi_choice_answer_Percentage()
            standard_Line_Answer_Target = kpi_answer_perc = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(answer_Cluster_List) + "', 'Answer', 'Percentage', 1, " + str(answer_Target) + ", 0, '01/01/2014', '31/12/9999', 'Call');"
            kpi_ID += 1
            print(standard_Line_Answer_Target, file=open("Tito_File2", "a"))

def choice_2_SL():

    kpi_ID = "0"
    cluster_List = ""
    print("Welcome to the SL printing enviroment, here you can produce SL SQL lines to insert SL KPI lines\n")
    input("Press Enter to continue....\n")
    time.sleep(0.3)
    kpi_ID = choice_1()
    time.sleep(2)
    sl_Cluster_List = n_clusterloop()
    time.sleep(2)
    t_Choice = input("Will you use the same kpi values for all those clusters? \n\nEnter: YES, or NO\n\nEnter value:  ")
    print("\nProcessing....\n")
    time.sleep(1.3)
    if t_Choice == "YES":
        print("\nProcessing....\n")
        time.sleep(0.5)
        print("All entered values will be used for all clusters...\n")
        time.sleep(0.5)
        sl_Level = kpi_choice_SL_Level()
        sl_Percentage = kpi_choice_SL_Percentage()
        open("Tito_File2", "w")
        for x, sl_Cluster_List in enumerate(sl_Cluster_List):
            standard_Line_sl_level = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(sl_Cluster_List) + "', 'Level', 'Percentage', 1, " + str(sl_Level) + ", 0, '01/01/2014', '31/12/9999', 'Servicelevel');"
            kpi_ID += 1
            standard_Line_sl_percentage = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(sl_Cluster_List) + "', 'Percentage', 'Percentage', 1, " + str(sl_Percentage) + ", 0, '01/01/2014', '31/12/9999','Servicelevel');"
            kpi_ID += 1
            print(standard_Line_Answer_Target, file=open("Tito_File2", "a"))


    elif t_Choice == "NO":
        open("Tito_File2", "w")
        for x, sl_Cluster_List in enumerate(sl_Cluster_List):
            print("Enter value for: " + sl_Cluster_List + "\n")
            time.sleep(0.7)
            sl_Level = kpi_choice_SL_Level()
            sl_Percentage = kpi_choice_SL_Percentage()

            standard_Line_sl_level = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(sl_Cluster_List) + "', 'Level', 'Percentage', 1, " + str(sl_Level) + ", 0, '01/01/2014', '31/12/9999', 'Servicelevel');"
            kpi_ID += 1
            standard_Line_sl_percentage = "INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('" + str(kpi_ID) + "', 'Cluster', '" + str(sl_Cluster_List) + "', 'Percentage', 'Percentage', 1, " + str(sl_Percentage) + ", 0, '01/01/2014', '31/12/9999','Servicelevel');"
            kpi_ID += 1
            print(standard_Line_Answer_Target, file=open("Tito_File2", "a"))

    print("Writing file.....\n")
    time.sleep(5)
    print("Writing succesful!\n")
    complete1 = input("To exit the program enter: EXIT, to go back to the beginning of the program, enter: RESTART\n")
    time.sleep(0.2)

def choice_2():

    import time
    time.sleep(1)
    kpi_choice = input("Please select one from following KPI's:\n\nFCR    AHT    ANSWER    SL     \n\nEnter value:")
    print("\nProcessing....\n")
    time.sleep(1)

    if kpi_choice == "FCR":
        choice_2_FCR()

    elif kpi_choice == "AHT":
        choice_2_AHT()

    elif kpi_choice == "ANSWER":
        choice_2_Answer()

    elif kpi_choice == "SL":
        choice_2_SL()
    else:
        return 0

def tito_KPI_Program_startup():
    import time
    cluster_List2 = ""
    choice = 0
    kpi_id_2 = 0
    cluster_entry_number = 1
    print("Welcome to the TITO KPI entry program\n")
    print("With every input prompt you have the chance to exit by entering: EXIT\n")
    print("Please choose one of the following options:\n 1: Use the full KPI set, only enter the cluster, and target value\n 2: Choose one KPI, enter all clusters you want to use the KPI for, enter the values manually ")
    tito_KPI_program_menu()

def tito_KPI_program_menu():
    import time
    choice = str(input())
    if choice == str(1):
        print_clusterset()

    elif choice == str(2):
        choice_2()

    elif choice == "EXIT":
        print("Thank you, bye bye\n")

    else:
        print("Please enter a valid value\n")
        time.sleep(2)
        tito_KPI_program_menu()

def kpi_Fullset():

    kpi_ID = 1252
    cluster_List = ["Pon Inbound Calls"]

    for x, cluster_List in enumerate(cluster_List):
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) + "', 'Period', 'Frequency', 1, 4, 0, '01/01/2014', '31/12/9999', 'FCR');")                   # FCR Date range
        kpi_ID += 1
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) +"', 'Direction', 'Recur', 1, 0, 0, '01/01/2014', '31/12/9999', 'FCR');")                    # FCR Direction
        kpi_ID += 1
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) + "', 'Answer', 'Percentage', 1, 0.95, 0, '01/01/2014', '31/12/9999', 'Call');")              # % Answered
        kpi_ID += 1
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) + "', 'Level', 'Percentage', 1, 2, 0, '01/01/2014', '31/12/9999', 'Servicelevel');")           # SL Level
        kpi_ID += 1
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) + "', 'Percentage', 'Percentage', 1, 0.8, 0, '01/01/2014', '31/12/9999','Servicelevel');")    # SL Percentage
        kpi_ID += 1
        print("INSERT Into KPI_LINE(KPI_ID, KPI_LEVEL, KPI_VALUE, KPI_NAME, UNIT, INTERN, TARGET, DELETED, START_DATE, END_DATE, CATEGORY) Values('", kpi_ID, "', 'Cluster', '" + str(cluster_List) + "', 'AHT', 'Seconds', 1, 550, 0, '01/01/2014', '31/12/9999', 'Call')")                      # AHT Target
        kpi_ID += 1

