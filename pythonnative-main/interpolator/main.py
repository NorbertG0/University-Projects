from interpolator import newton_wrapper

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    x = list(map(float, lines[1].split()))
    y = list(map(float, lines[3].split()))
    values = list(map(float, lines[5].split()))

    return x, y, values

def main():
    x, y, values = parse_input("../input/data.txt")
    results = newton_wrapper.interpolate(x, y, values)
    for val, res in zip(values, results):
        print(f"x: {', '.join(str(v) for v in x)}")
        print(f"y: {', '.join(str(v) for v in y)}")
        print(f"wartosc do interpolacji: {val}")
        print(f"Interpolacja dla {val}: {res} \n ------------------------")


if __name__ == "__main__":
    main()
