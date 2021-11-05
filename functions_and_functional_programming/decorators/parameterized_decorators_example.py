from utils_decorators import check_non_negative

@check_non_negative(1)
def create_list(value, size):
    return [value] * size


if __name__=="__main__":

    try:
        print("Creating valid list")
        print(create_list(2, 5))
        print("-------------------")
        print("Creating invalid list")
        print(create_list(2,-2))
    except ValueError as err:
        print(err)
