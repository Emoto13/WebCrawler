import matplotlib.pyplot as plt
import sqlite3
from database_abstractions.database import session_scope
from models.server import Server

COUNT_QUERY = '''
SELECT COUNT(*)
FROM  servers 
WHERE servers.server_name = ?
'''


def main():
    labels = get_labels()
    counts = get_counts(labels)
    create_pie_chart(labels, counts)


def get_labels():
    with session_scope() as session:
        labels_raw = session.query(Server).group_by(Server.server_name).with_entities(Server.server_name).all()
    labels = list(map(lambda x: x[0], labels_raw))
    return labels


def get_counts(labels):
    counts = []
    connection = sqlite3.connect('sites.db')
    cursor = connection.cursor()

    for label in labels:
        cursor.execute(COUNT_QUERY, (label,))
        res = cursor.fetchone()
        counts.append(res)
    connection.commit()
    connection.close()
    return counts


def create_pie_chart(labels, counts):
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()


if __name__ == '__main__':
    main()
