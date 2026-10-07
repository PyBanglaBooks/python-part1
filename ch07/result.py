def show_result(marks):
    if marks >= pass_mark:
        status = "Passed"
    else:
        status = "Failed"
    print(f"{marks}: {status}")

pass_mark = 33
show_result(45)
show_result(20)
