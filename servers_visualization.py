import matplotlib.pyplot as plt
import sqlite3
from database_abstractions.database import session_scope
from models.server import Server

count_query = '''
SELECT COUNT(*)
FROM  servers 
WHERE servers.server_name = ?
'''


def main():
    with session_scope() as session:
        labels_raw = session.query(Server).group_by(Server.server_name).with_entities(Server.server_name).all()
    labels = list(map(lambda x: x[0], labels_raw))
    counts = []
    connection = sqlite3.connect('sites.db')
    cursor = connection.cursor()

    for label in labels:
        cursor.execute(count_query, (label,))
        res = cursor.fetchone()
        counts.append(res)
    connection.commit()
    connection.close()

    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


if __name__ == '__main__':
    main()
