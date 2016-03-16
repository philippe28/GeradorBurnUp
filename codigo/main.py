from BurnUp import Sprint

def main():
    sprint=Sprint()

    sprint.add_meta(100)
    sprint.add_trabalho(0)

    sprint.add_meta(100)
    sprint.add_trabalho(6)

    sprint.add_meta(100)
    sprint.add_trabalho(18)

    sprint.add_meta(100)
    sprint.add_trabalho(31)

    sprint.add_meta(100)
    sprint.add_trabalho(45)

    sprint.add_meta(100)
    sprint.add_trabalho(57)

    sprint.add_meta(120)
    sprint.add_trabalho(70)

    sprint.add_meta(120)
    sprint.add_trabalho(84)

    sprint.add_meta(120)
    sprint.add_trabalho(97)

    sprint.grafico(sprint.meta,sprint.trabalho,9) 

if __name__ == "__main__":
    main()