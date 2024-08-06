#manualy update lists in the text files by typing in items

def chooseLang():
    '''Asks the user for a language of the item they want to add.
    
    Returns:

        toFile - name of the file to which this item will be added.
    '''
    
    askLang, askTopic = True, True
    itemTopic, itemLang = '', ''
    toFile = ''
    while askLang:
        lang = input('''Please choose the language: 
                    0 - English
                    1 - Russian
                    2 - Ukrainian
                    3 - Czech
                        
''')
        if len(lang) == 0:
            askLang = False
        elif len(lang) == 1:
            try:
                lang = int(lang)
                match lang:
                    case 0:
                        itemLang = 'eng'
                    case 1:
                        itemLang = 'ru'
                    case 2:
                        itemLang = 'ua'
                    case 3:
                        itemLang = 'cz'
                    case _:
                        print("Please enter a valid number")
                        continue
                try:
                    while askTopic:
                        topic = input('''Please choose the topic: 
                    0 - Animals
                    1 - Monthly Cards
                    2 - Painters
                    3 - Composers
                        
''')
                        if len(topic) == 0:
                            askTopic = False
                        elif len(topic) == 1:
                            try:
                                topic = int(topic)
                                match topic:
                                    case 0:
                                        itemTopic = 'animals'
                                    case 1:
                                        itemTopic = 'MonthCards'
                                    case 2:
                                        itemTopic = 'painters'
                                    case 3:
                                        itemTopic = 'composers'
                                    case _:
                                        print("Please enter a valid number")
                                        continue
                                askTopic = False
                            except Exception:
                                print("Please enter a valid number")
                                pass
                        else:
                            print('It is not valid, please try again.')
                            pass
                    toFile = itemLang + '/' + itemTopic + '_' + itemLang + '.txt'
                    askLang = False
                except Exception:
                    print("Please enter a valid number")
                pass
            except Exception:
                print("It is not a number.")
            pass    
        else:
            print('It is not valid, please try again.')
            pass
    return toFile


def addItem():
    '''Adds an item to the list if it's not there yet.
    
    Returns:
        
        toFile - the name of the file where to add item
        items - a list of items to add

    '''
    askAgain = True
    items = []
    toFile = chooseLang()
    if len(toFile) != 0:  
        while askAgain:
            item = input('What do you want to add? ')
            if len(item) == 0:
                print('Thank you!')
                askAgain = False
            else:
                try:
                    with open(toFile, 'r') as file:
                        inFile = []
                        for line in file:
                            word = line.rstrip()
                            inFile.append(word.lower())
                        if item.lower() not in inFile:
                            items.append(item.lower())
                            print('Successfully added', item)                 
                        else:
                            print('It is already in the list')
                            pass
                except FileNotFoundError:
                    print('This file was not found, sorry. Try again.')
                    toFile = chooseLang()
    else:
        print('Something went wrong')
    return (toFile, items)
    

def writeToFile():
    askAgain = True
    toFile, items = addItem()
    while askAgain:
            if len(toFile) > 7 and len(items) > 0:
                try:
                    with open(toFile, 'a') as file:
                        for item in items:
                            file.write(item + '\n')
                    askAgain = False
                except FileNotFoundError:
                    print('This file does not exist.')
            elif len(items) == 0:
                print('It seems there is nothing to add..')
                askAgain = False
            else:
                print('Something went wrong.....Try from the beginning.')
                toFile, items = addItem()
    print('Goodbye!')
        
    

writeToFile()

