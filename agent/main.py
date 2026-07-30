from agent.host import get_host_info


def main():
    print("RealmRelay Agent starting...")
    print()

    host = get_host_info()

    for key, value in host.items():
        print(f"{key}: {value}")

    print()
    print("Status: Ready")


if __name__ == "__main__":
    main()