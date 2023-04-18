import docker
from cassandra.cluster import Cluster

client = docker.from_env()


def container_setup():
        
    # Create a container if it doesn't exist
    container_name = 'my-cassandra-container'
    containers = client.containers.list(all=True, filters={'name': container_name})

    if containers:
        container = containers[0]
        print(f"A container with the name '{container_name}' already exists.")
    else:
        container = client.containers.run(
            'cassandra:latest',
            detach=True,
            ports={'9042/tcp': 9042},
            environment={'CASSANDRA_KEYSPACE': 'mykeyspace'},
            name=container_name
        )
        print(f"Container '{container_name}' created with ID {container.id}")

    if container.status != "running":
        print(f"Starting container {container_name}")
        container.start()
        # Wait for the container to start
        container.wait(timeout= 60*5)
        print(f"Container {container_name} started")

    # Connect to the Cassandra cluster
    print("Connecting")
    cluster = Cluster(['localhost'], port=9042)
    session = cluster.connect()

    table_setup(session)

    return cluster, session

def table_setup(session):
    keyspace = "movieks"
    table_name = "movietbl"
    print("Creating table")
    # Create a keyspace and a table
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {keyspace} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};
    """)
    # Use the keyspcae
    session.execute(f"""
        USE {keyspace}
    """)
    session.execute(f"""
        DROP TABLE IF EXISTs {table_name} ;
    """)
    # Create cast_details type
    session.execute(f"""
        CREATE TYPE IF NOT EXISTS cast_type (
        cast_id bigint,
        screen_name text,
        name text,
        payment int,
        related_movies list<text>);
    """)
    # Create the table 
    session.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        movie_id bigint PRIMARY KEY,
        movie_name text,
        director text,
        writer text,
        genre text,
        runtime int,
        cast list<frozen<cast_type>>);
    """)
    print("Table created")

def container_shutdown(cluster):
    cluster.shutdown()



if __name__ == "__main__":
    cluster, session = container_setup()
    container_shutdown(cluster)
