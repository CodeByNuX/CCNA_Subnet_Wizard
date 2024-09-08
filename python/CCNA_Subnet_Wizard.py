import os
import sys
import ipaddress
import random
from enum import Enum
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#if stdout is redirected, no colors
init(strip=not sys.stdout.isatty())


def random_jokes()->str:
    JokeBank = []
    JokeBank.append("What is Tom Hanks wireless password?........... 1Forest1")
    JokeBank.append("How does a tree get on the internet?.............. It logs on")
    JokeBank.append("Five routers walk into a bar. Who gets the car keys? ...... The Designated Router")
    JokeBank.append("What do they call a group of Network Engineers?..... An Outage !")
    JokeBank.append("I can tell you a joke about TCP. I guarantee you'll get it, but it might take a few tries.")
    JokeBank.append("I would tell you a joke about UDP, but you probabl wouldn't get it.")
    JokeBank.append("I once told an NTP Joke.............  The timing was perfect")
    JokeBank.append("I'm getting the license plate 'DSCP EF'.. so I don't get policed when I'm inside my CAR!!!")
    JokeBank.append("What does the networking seal say?............ ARP, ARP, ARP")
    JokeBank.append("TCP is most religious..... WHY?.. Because it all starts with a  * SYN *")
    JokeBank.append("If you have experienced an ICMP joke,  ping me..  ")

    return random.choice(JokeBank)

def sad_panda():
    sadPanda = '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠻⣿⡽⢹⣷⠆⣸⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠟⠙⣿⡇⠀⠈⣿⡋⢾⣟⠐⢻⡃⠸⢻⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣷⣶⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⢀⣀⣠⣶⣿⠷⣶⣤⣄⣀⣤⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⡶⠚⠋⠉⠉⠁⠀⠀⠀⠀⠈⠉⠛⠿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣶⣿⣷⣦⡀⢀⣀⣾⠃⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣾⣿⣾⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⠿⠛⠋⢹⡏⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⢿⣿⠟⠁⠀⠀⠀⣼⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣛⣿⣿⣿⡇⠀⠀⠀⠀⠀⠹⣿⣿⣭⣽⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⣠⣤⣤⡄⠉⠻⠿⠿⠿⠛⠈⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠙⠻⠿⠿⠟⠛⠁⠀⠀⠀⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀
⠀⣠⣤⣤⣸⡇⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠁⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⡆⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⣀⣀⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    #
    print(sadPanda)



class difficulty():
    # class to hold the difficulty
    # as its being passed around
    class levels(Enum):
        
        easy = 1
        medium = 2
        hard = 3

    def __init__(self,level=None):
        self.level = level

def _clear_screen():
    # clear the console screen
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def _print_title():
    _clear_screen()
    cprint(figlet_format('CCNA Subnet Wizard!'),'cyan', attrs=['bold'])


def _choose_difficulty()->difficulty:
    '''
    Asked the user what difficulty they want.

    Return:
    -------
    difficulty

    '''
    while True:
        #Repeat if bad selection.
        print('\n')
        print(' 1. Easy')
        print(' 2. Medium')
        print(' 3. Hard')
        print('\n\n')

        choice = input(' select the difficulty level: ')
        _difficulty = difficulty()
        if choice == '1':
            _difficulty.level = difficulty.levels.easy
            return _difficulty
        elif choice == '2':
            _difficulty.level = difficulty.levels.medium
            return _difficulty
        elif choice == '3':
            _difficulty.level = difficulty.levels.hard
            return _difficulty
        else:
            #incorrect selection
            print('\nIncorrect selection, please try again\n\n')

def generate_IPv4(DIFFICULTY:difficulty)->ipaddress:
    '''
    Generates a random IPv4 ipAddress

    Returns:
    --------
    ipaddress : object (module)


    '''
    # Generates a random ipv4 address
    try:
        #Generate a random ip  (32 bits) 2 is the base & 32 is the exponent
        ipv4 = ipaddress.IPv4Address(random.randint(0,2**32))

        if DIFFICULTY.level == difficulty.levels.easy:
            #Lets return an easy question.
            # we are saying the cidr for an easy is 24 bits to 30 bits
            # 31 and 32 are `special`
            _cidr = '/' + str(random.randint(24,30))
            # The interface lets us access the particulars for that network
            # as we can construct the 'NETWORK' with not having to worry about
            # Host bits.
            interface = ipaddress.IPv4Interface(ipv4.compressed+_cidr)
            return interface
        
        elif DIFFICULTY.level == difficulty.levels.medium:
            # Lets return a medium question.
            # we are saying the cidr for the medium is 16 bits to 30 bits
            # 31 and 32 are `special`
            _cidr = '/' + str(random.randint(16,30))
            # The interface lets us access the particulars for that network
            # as we can construct the 'NETWORK' with not having to worry about
            # Host bits.
            interface = ipaddress.IPv4Interface(ipv4.compressed+_cidr)
            return interface
        elif DIFFICULTY.level == difficulty.levels.hard:
            # Lets return a HARD questions.
            # We are saing the cidr for the hard is from 1 to 32 bits in length
            # 31 and 32 are `special`
            _cidr = '/' + str(random.randint(1,30))
            #The interface lets us access the particulars for that network
            # as we can construct the 'NETWORK' with not having to worry about 
            # Host bits.
            interface = ipaddress.IPv4Interface(ipv4.compressed+_cidr)
            return interface


    except Exception as e:
        print('Sorry.. something bad happend. While trying to generate an IPv4 Address')
        print(e)

def play_again():
    #Sub Menu
    while True:
        print('\n')
        print('1. Play again?')
        print('2. Main Menu')
        print('3. Exit.. Another IPv4 packet Expires in the world  :(  \n')

        choice = input('Please make a selection: ')
        _clear_screen()
        if choice == '1':
            return True
        elif choice == '2':
            return False
        elif choice == '3':
            _clear_screen()
            print('Sad Panda.... ')
            sad_panda()
            sys.exit(0)



def option_1(DIFFICULTY:difficulty):
    #Lets play the how many hosts game
    
    while True:
        _clear_screen()
        #Generates an IPv4 address based on our Difficulty
        IPv4 = generate_IPv4(DIFFICULTY)
        host_addresses = IPv4.network.num_addresses -2 #Need to minus two, to remove the Network ID and Broadcast

        _answer = input(' \nFor Network {}, How many [usable] availible host addresses are there?: '.format(IPv4.network.compressed))
        if _answer == str(host_addresses):
            print('\n Nicely Done!! \n')
            input('[Enter]')

        else:
            print('\n Better luck next time! Keep at it..\n')
            print('Answer: {}'.format(host_addresses))
            print('[Enter]')

        if play_again() == False:
            main_menu(DIFFICULTY)

def option_2(DIFFICULTY:difficulty):
    #Lets play the calculate the
    # * Network ID Address
    # * BroadCast Address
    # * First usable
    # * Last usable
    while True:
        _clear_screen()
        #Generate an IPv4 address based on our Difficulty
        IPv4 = generate_IPv4(DIFFICULTY)
        broadcast_address = IPv4.network.broadcast_address.compressed
        network_id_address = IPv4.network.network_address.compressed
        #Can't get the first or last from object interface
        # creating object ip_network to get first & last
        _network = ipaddress.ip_network(IPv4.network.compressed)
        first_usable_ip = next(_network.hosts())
        last_usable_ip = _network.broadcast_address -1

        # Randomly getting a host as an example to use
        magic_host = random.choice((list(_network.hosts())))
        


        ######################  Format
        # 
        print('\nAll answers are in dotted decimal.\n x.x.x.x\n')
        print('\n For this Host: {}/{}\n'.format(magic_host.compressed,IPv4._prefixlen))

        if (input('What is the Network ID: ') ==  network_id_address):
            print('\n Way to Go!!!\n')
        else:
            print('Nice try. {}\n'.format(network_id_address))
        
        if (input('What is the first usable IP Address: ') == first_usable_ip.compressed):
            print('Right on!!\n')
        else:
            print('Nice try. {}\n'.format(first_usable_ip.compressed))
        if (input('What is the last usable IP Address: ') == last_usable_ip.compressed):
            print('Whoa.. Dude.. That was awesome!\n')
        else:
            print('Nice try. {}\n'.format(last_usable_ip.compressed))
        if (input('What is the Broadcast Address: ') == broadcast_address):
            print('You are correct!\n')
        else:
            print('Nice try. {}\n'.format(broadcast_address))


        if play_again() == False:
            main_menu(DIFFICULTY)   

def option_3(DIFFICULTY:difficulty):
    '''
    Same concept as option_2 (Network Id, First, Last, Broadcast)
    But here we just want the subnet (Network id)
    '''
    while True:
        _clear_screen()
        #Generate an IPv4
        IPv4 = generate_IPv4(DIFFICULTY)
        network_id_address = IPv4.network.network_address.compressed
        #Can't get the first or last from object interface
        # creating object ip_network to get first & last
        _network = ipaddress.ip_network(IPv4.network.compressed)
        
        # Randomly getting a host as an example to use
        magic_host = random.choice((list(_network.hosts())))

        if (input('On what subnet will you find this host {}/{}: '.format(magic_host.compressed,IPv4._prefixlen)) == network_id_address):
            print('\nNice Job!\n')
        else:
            print('\n Sorry,. that is not correct..  {}\n'.format(network_id_address))
        
        if play_again() == False:
            main_menu(DIFFICULTY)  
        



def option_4(DIFFICULTY:difficulty):
    '''
    Convert the binary string to decimal.
    DIFFICULTY, is passed back to main_menu. Otherwise not used here.
    '''
    while True:
        #
        _clear_screen()
        #Randomly pick a number, and then convert it to binary string
        #Have the user guess the correct decimal number
        num = random.randint(1,255)
        ans = format(num,'08b')

        if (input('Convert the binary string {} to decimal: '.format(ans)) == str(num)):
            print('\nYou are Correct!!\n')
        else:
            print('\nNice try.\n {}\n'.format(num))
    
        if play_again() == False:
            main_menu(DIFFICULTY)


def main_menu(DIFFICULTY:difficulty):
    '''
    The main_menu of the script.  Tied to while loop that branches.

    PARAMS:
    -------
    DIFFICULTY | difficulty
        The difficulty level that will be applied to questions.
    '''


    while True:

        _print_title()

        #check difficulty setting
        if DIFFICULTY.level == None:
            #Then ask them to choose.
            DIFFICULTY = _choose_difficulty()
            _clear_screen()
            _print_title()
        
        print('\n\n')
        print(' MENU')
        print(' -----\n')

        print(' 1. (IPv4) Calculate the [usable] Available Host addresses for a Network?')
        print(' 2. (IPv4) Determine the Network ID, First, Last and Broadcast address.')
        print(' 3. (IPv4) Name that subnet.')
        print(' 4. Convert binary to decimal.')
        
        #formatting
        print('\n')
        print('9. Change Difficulty Level')
        print('10. Exit')
        print('\n')

        choice = input('Please type a selection: ')

        if choice == '1':
            _clear_screen()
            #Go to Option1
            option_1(DIFFICULTY)
        if choice == '2':
            #Go to Option 2
            option_2(DIFFICULTY)
        elif choice == '3':
            option_3(DIFFICULTY)
        elif choice == '4':
            option_4(DIFFICULTY)
        elif choice == '9':
            DIFFICULTY = _choose_difficulty()
        elif choice == '10':
            _clear_screen()
            print(' ')
            print('GoodBye !!!')
            print('\n\n\n')
            print('before you go.. how about a joke??\n\n')
            print(random_jokes())
            print('\n')
            

            sys.exit(0)
        else:
            print('{} is an invalid choice, please choose again'.format(choice))
            #Pause
            input('\n[Enter]')





if __name__=='__main__':
    # Create DIFFICULTY. Default: x.level = None
    DIFFICULTY = difficulty()
    main_menu(DIFFICULTY)