has_high_income=True
has_good_credit=True
criminal_record=True

if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_high_income or has_good_credit:
    print("Eligible for loan")
elif has_good_credit and not criminal_record:
    print("eligible")
