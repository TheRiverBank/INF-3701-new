from cassandra.query import SimpleStatement
import sys
sys.path.append('../')
from datagen.datagen import generate_data_4_cass_row


def insert_data(session, N):        
    insert_query = SimpleStatement("""
    INSERT INTO movietbl (movie_id, movie_name, director, writer, genre, runtime, cast)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """)
    # Execute the insert query with the data
    print("Inserting data")
    for _ in range(N):
        data = generate_data_4_cass_row()
        #cast = list({data[-1][0].values()})
        #data = data[:-1]
        #data.append(cast)
        print(data)
        session.execute(insert_query, data)
    print("Data inserted")

