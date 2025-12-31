def display_text_a(msg):
    print(msg)


def call_b():
    import circular_solution_b

    circular_solution_b.display_text_b("Hello b! I just imported you")



if __name__ == '__main__':
    call_b()

