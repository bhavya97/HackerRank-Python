import threading

class Bhavya(threading.Thread):
    def run(self):
        for x in range(50):
            print(threading.current_thread().getName())

x = Bhavya(name = "Sending Messages")
y = Bhavya(name = "Receiving Messages")

x.start()
y.start()