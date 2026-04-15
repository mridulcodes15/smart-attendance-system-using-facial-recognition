def predict_risk(attended, total):
    if total == 0:
        return "No Data", 0

    percentage = (attended / total) * 100

    if percentage < 60:
        return "High Risk", percentage
    elif percentage < 75:
        return "Moderate Risk", percentage
    else:
        return "Safe", percentage