def create_scheduled_activities():
    # Define your scheduled activities in this function
    month_ = {
        "4. Send Transactions: Accounting Office": {"day": 4, "month": None},
        "5. DEH Self Metering": {"day": 5, "month": None},
        "11. PROTERGIA Self Metering": {"day": 11, "month": None},  # None means every month
        "12. Pay Day (VODAFONE HOME)": {"day": 12, "month": None},
        "13. Pay Day (My DEH)": {"day": 13, "month": None},
        "14. Pay Day (COSMOTE HOME)": {"day": 14, "month": None},
        "15. Pay Day (PROTERGIA)": {"day": 15, "month": None},
        "17. Pay Day (COSMOTE MOBILE)": {"day": 17, "month": None},
        "21. Pay Day (VODAFONE MOBILE)": {"day": 21, "month": None},
        "25. Create Special Prices": {"day": 25, "month": None},  # None means every month
        "26. Organize Employees Working Time": {"day": 26, "month": None},
    }
    scheduled_activities = month_
    return scheduled_activities