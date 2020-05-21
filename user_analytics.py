from datetime import timedelta, datetime
import matplotlib.pyplot as plt

from database_abstractions.database import session_scope
from models.domain import Domain


def main():
    choose_option = input("Choose metrics to display\n"
                          "Option last (hour, week, month): ")
    options = {
        'hour': timedelta(hours=1),
        'week': timedelta(weeks=7),
        'month': timedelta(days=30)
    }
    time_chosen = datetime.now() - options[choose_option]
    with session_scope() as session:
        domain_names_raw = session.query(Domain) \
            .filter(Domain.visited_at >= time_chosen) \
            .with_entities(Domain.domain_name) \
            .all()
    domain_names = list(map(lambda x: x[0], domain_names_raw))
    unique_domain_names = list(set(domain_names))

    count_of_domains = ['Unique domains']
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = [len(unique_domain_names)]
    width = [len(unique_domain_names)]
    error = [len(unique_domain_names)]

    ax.barh(y_pos, width, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(count_of_domains)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('User statistics')
    ax.set_title(f'Domains found in the last {choose_option}')

    plt.show()


if __name__ == '__main__':
    main()
