def explain(plate, confidence, severity):

    print()
    print("Violation Explanation")
    print("---------------------")

    print("Plate Number :", plate)
    print("OCR Confidence :", confidence)
    print("Severity :", severity)

    if severity > 80:
        print("Action : Immediate Enforcement")

    elif severity > 50:
        print("Action : Medium Priority")

    else:
        print("Action : Low Priority")


explain(
    "MH20DV2363",
    0.80,
    92
)