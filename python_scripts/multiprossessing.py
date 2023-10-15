import multiprocessing

import time

 

# Producer/Writer

def procFunction0(messageQueue):

    for i in range(1,10):

        messageQueue.put("Child1:Message%d"%i)

        time.sleep(1)

 

# Consumer/Reader

def procFunction1(messageQueue):

    while messageQueue.empty() is False:

        print("From reader:%s"%messageQueue.get())

        time.sleep(1)

 

# Producer/Writer

def procFunction2(messageQueue):

    for i in range(1,10):

        messageQueue.put("Child3:Message%d"%i)

        time.sleep(1)

 

if __name__ == "__main__":

 

    multiprocessing.set_start_method("fork")

   

    messageQueue  = multiprocessing.Queue()

   

    # Create child processes

    childProcess0 = multiprocessing.Process(target=procFunction0, args=(messageQueue,))

    childProcess1 = multiprocessing.Process(target=procFunction1, args=(messageQueue,))

    childProcess2 = multiprocessing.Process(target=procFunction2, args=(messageQueue,))

 

    # Start all the child processes - Writer, Reader, Writer

    childProcess0.start()

    childProcess1.start()

    childProcess2.start()

 

    # Wait for child processes to finish

    childProcess0.join()

    childProcess1.join()

    childProcess2.join()