from p1 import read, build_tree, add, reduce, magnitude

if __name__ == "__main__":
    sns = read("input.txt")
    print(
        max(
            magnitude(reduce(add(build_tree(sns[i]), build_tree(sns[j]))))
            for i in range(len(sns))
            for j in range(len(sns))
            if i != j
        )
    )

