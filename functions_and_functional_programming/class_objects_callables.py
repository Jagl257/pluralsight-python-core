def sequence_class(inmutable):
    if inmutable:
        cls = tuple
    else:
        cls = list
    return cls


if __name__ == "__main__":

    flag = input("Enter T for inmutable or F for mutable \n")

    cls = sequence_class(True if flag=='T' else False)

    obj = cls("INMUTABLE")

    print(obj)

    print(f"Type = {type(obj)}")


