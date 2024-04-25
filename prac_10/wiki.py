import wikipedia


def main():
    wikipedia.set_lang("en")
    wikipedia.set_user_agent("YourAppName/1.0 (jiahao.song@my.jcu.edu.au)")

    while True:
        search_input = input("Please Enter the page title or search phrase (press Enter to exit): ")
        if not search_input:
            break

        try:
            page = wikipedia.page(search_input)
            print("title:", page.title)
            print("abstract:", page.summary)
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print("Disambiguation page found, please select a specific page:")
            options = e.options
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            choice = input("Select a page (enter a number): ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(options):
                    page = wikipedia.page(options[choice - 1])
                    print("title:", page.title)
                    print("abstract:", page.summary)
                    print("URL:", page.url)
                else:
                    print("invalid option.")
            except ValueError:
                print("invalid option.")


if __name__ == "__main__":
    main()



