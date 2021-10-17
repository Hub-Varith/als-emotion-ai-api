from model import Model

def main():
    model = Model()
    test_text = "I hate you"
    model.predict(test_text)

if __name__ == "__main__":
    print("running model test...")
    main()