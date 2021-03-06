import Graph
import plot


def print_menu():  ## Your menu design here

      print (30 * "-", "MENU", 30 * "-")
      print ("1. Generazione Grafi pesati")
      print ("2. Generazione Grafi Pesati e MST")
      print ("3. Generazione Grafi non pesati")
      print ("4. Grafico Grafo non pesato")
      print ("5. Grafico grafo pesato")
      print ("6. Grafico Mst")
      print ("7. exit")
      print (67 * "-")


loop = True

while loop:  ## While loop which will keep going until loop = False
      print_menu()  ## Displays menu
      choice = int(input("Enter your choice [1-7]: "))

      if choice == 1:
            print ("Generazione Grafi pesati")
            graph_only=True
            result_file_weighted = open('result/result_wei.txt', 'w')
            for i in range(20):  # test pesato
                  result = Graph.weighted_graph_generation(graph_only)
                  print(result)
                  result_file_weighted.writelines(str(result) + "\n")
            result_file_weighted.close()

      elif choice == 2:
            graph_only=False
            print ("Generazione Grafi Pesati e MST")
            result_file_weighted= open('result/result_mst.txt', 'w')
            for i in range(20):                                      #test pesato
                 result = Graph.weighted_graph_generation(graph_only)
                 #print(result)
                 #result_file_weighted.writelines(str(result)+"\n")
            result_file_weighted.close()


      elif choice == 3:
            print("Generazione Grafi Pesati non pesati")
            result_file_simple = open('result/result_simple.txt', 'w')
            for i in range(20):  # test pesato
                  result = Graph.simple_graph_generation()
                  print(result)
                  result_file_simple.writelines(str(result) + "\n")
            result_file_simple.close()

      elif choice == 4:
            print("E' stato selezionato grafico non pesato")
            plot.simple_graph_plot()
      elif choice == 5:
            print("E' stato selezionato grafico pesato")
            plot.weighted_graph_plot()
      elif choice == 6:
            print("E' stato selezionato grafico MST")
            plot.mst_graph_plot()
      elif choice == 7:
            print("Uscita")
            loop = False
      else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Nessuna opzione corrispondente, prova di nuovo...")















