import echo as ec #mengimport module Echo
import time

"""
ini adalah suatu program chat bot sederhana
ECHO BOT akan merespon inputan yang anda masukkan

#just for fun :D
"""
print("welcome to Simple ECHO_BOT")
print("Type \"help\" or \"info\" for more information.\n")
temp = ""


#ini untuk perulanganya 
#this is looping
def main(): 
  while True:
    pesan = str(input('You : '))

    #temp = pesan
    #ec.temp_msg(temp)
    #print(temp)

    ec.send_message(pesan)
    if 'bye' in pesan:
      time.sleep(0.5)
      exit()
      break

print(temp)
main()