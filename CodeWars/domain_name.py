def domain_name(url: str) -> str:
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


if __name__ == '__main__':
    print(domain_name("http://www.wert.google.co.jp"))
