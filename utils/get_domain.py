def get_domain_from_url_string(url_string):
    domain = url_string.split("://")[1].split("/")[0]
    return domain
