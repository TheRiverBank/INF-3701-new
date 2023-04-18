from connector import *
from datainsert import *

if __name__ == "__main__":
    cluster, session = container_setup()
    insert_data(session, N=2)
    #container_shutdown()