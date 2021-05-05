import Graph
import plot


def print_menu():  ## Your menu design here

      print (30 * "-", "MENU", 30 * "-")
      print ("1. Generazione Grafi pesati")
      print ("2. Generazione Grafi Pesati e MST")
      print ("3. Generazione Grafi non pesati")
      print ("4. test plot")
      print ("5. exit")
      print (67 * "-")


loop = True

while loop:  ## While loop which will keep going until loop = False
      print_menu()  ## Displays menu
      choice = int(input("Enter your choice [1-3]: "))

      if choice == 1:
            print ("Generazione Grafi pesati")
            graph_only=True
            result_file_weighted = open('result_wei.txt', 'w')
            for i in range(10):  # test pesato
                  result = Graph.weighted_graph_generation(graph_only)
                  # print(result)
                  result_file_weighted.writelines(str(result) + "\n")
            result_file_weighted.close()

      elif choice == 2:
            graph_only=False
            print ("Generazione Grafi Pesati e MST")
            result_file_weighted= open('result_wei.txt', 'w')
            for i in range(100):                                      #test pesato
                 result = Graph.weighted_graph_generation(graph_only)
                 print(result)
                 result_file_weighted.writelines(str(result)+"\n")
            result_file_weighted.close()


      elif choice == 3:
            print("Generazione Grafi Pesati non pesati")
            result_file_simple = open('result_simple.txt', 'w')
            for i in range(20):  # test pesato
                  result = Graph.simple_graph_generation()
                  print(result)
                  result_file_simple.writelines(str(result) + "\n")
            result_file_simple.close()

      elif choice == 4:
            print("Menu 3 has been selected")
            plot.simple_graph_plot()
      elif choice == 5:
            print("Uscita")
            loop = False
      else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")














# result_file_simple= open('result_simple.txt', 'w')
#
# for i in range(1000):                                        #test non pesato
#      result = Graph.simple_graph_generation()
#      print(result)
#      result_file_simple.writelines(str(result)+"\n")
# result_file_simple.close()
#
# result=0
#
#
# result_file_weighted= open('result_wei.txt', 'w')
# for i in range(1000):                                      #test pesato
#      result = Graph.weighted_graph_generation()
#      print(result)
#      result_file_weighted.writelines(str(result)+"\n")
# result_file_weighted.close()

