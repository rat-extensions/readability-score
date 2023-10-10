import os
from scrapingNode import GoogleScraper, Scraper
from textAnalyzer import TextAnalyzer
############################################################################################
gs = GoogleScraper()
sc = Scraper()
tx = TextAnalyzer()
############################################################################################
def main_menu():
    while True:
        x: str = input("Input a FULL URL or/  somthing to google (Q to quit): ")
############################################################################################
        if x.lower() == 'q':
            clean(".")
            break
############################################################################################
        y = x.lstrip()
        if y.startswith("https://"):
            mainText: str = sc.fetchTextFromURL(y)
            print("LINK DETECTED")
            text_file = open("webdoc" + str(0) + ".txt", "w")
            # Write string to file
            text_file.write(mainText)
            # Close file
            text_file.close()
            try:
                tx.analyze(mainText)
            except Exception as e:
                print(e)
                continue
############################################################################################
        else:
            print("WEBSEARCH DETECTED")
            try:
                links = gs.scrape_google(x)
            except Exception as e: 
                print("Problem occurred during scraping")
                print(e)
                break

            for link in links[:10]: 
                print ("##"+ str(1 + links.index(link)  ) + " - " + link , end='\n')
            while(True):
                lol = input("ENTER THE NUMBER OF LINK U WANNA ANALYZE OR TYPE: 'all' to analyze all of them -- type 'Q' to quite: ")
                print(lol)
                if lol == "all":
                    for link in links[:10]: 
                        mainText = sc.fetchTextFromURL(link)
                        text_file = open("webdoc" + str(1 + links.index(link)  )  + ".txt", "w")
                # Write string to file
                        if mainText is not None: text_file.write(mainText)
                        else: print("Could not retrive text from: " + link)
                # Close file    
                        text_file.close()
                        print("DOCUMENT ##NUM " +str( 1 + links.index(link)  )+ " * " + link + "  ---->  CLOSED<<>>> FETCHING SUCCESSFUL")
                        try:
                            tx.analyze(mainText)
                        except Exception as e:
                            print(e)  
                elif lol.lower() == 'q':
                    clean(".")
                    break 
                elif lol.isdigit() and int(lol) in range(1, 10):   
                    mainText = sc.fetchTextFromURL(links[int(lol)-1])
                    text_file = open("webdoc" + str(lol)   + ".txt", "w")
                # Write string to file
                    if mainText is not None: text_file.write(mainText)
                    else: print("Could not retrive text from")
                # Close file    
                    text_file.close()
                

                    try:    
                        tx.analyze(mainText)
                    except Exception as e:
                        print(e)    
                        
                    print("DOCUMENT ##NUM " +str( lol  )+ " * " + links[int(lol)-1] + "  ---->  CLOSED<<>>> Analyzing SUCCESSFUL")
                else: print("invalid input")
       
############################################################################################
def clean(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
############################################################################################
                
if __name__ == '__main__':
    main_menu()
