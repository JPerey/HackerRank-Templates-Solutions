if __name__ == '__main__':

    def helper_insert(changing_list, index, e):
        changing_list.insert(index, e)
        return changing_list

    def helper_remove(changing_list, e):
        if e in changing_list:
            changing_list.remove(e)
        return changing_list

    def helper_append(changing_list, e):
        changing_list.append(e)
        return changing_list

    def helper_sort(changing_list):
        changing_list.sort()
        return changing_list

    def helper_pop(changing_list):
        changing_list.pop()
        return changing_list

    def helper_reverse(changing_list):
        changing_list.reverse()
        return changing_list

    def helper_print(changing_list):
        print(changing_list)

    final_list = []
    command_list = []
    N = int(input())
    for n in range(N):
        list2 = input().split()
        command_list.append(list2)

    for command in command_list:
        if command[0] == "insert":
            final_list = helper_insert(
                final_list, int(command[1]), int(command[2]))
        elif command[0] == "remove":
            final_list = helper_remove(final_list, int(command[1]))

        elif command[0] == "append":
            final_list = helper_append(final_list, int(command[1]))

        elif command[0] == "sort":
            final_list = helper_sort(final_list)

        elif command[0] == "pop":
            final_list = helper_pop(final_list)

        elif command[0] == "reverse":
            final_list = helper_reverse(final_list)

        else:
            helper_print(final_list)
