def get_performance_category(total_score):
    if total_score >= 90:
        return "Excellent"
    elif total_score >= 75:
        return "Good"
    elif total_score >= 60:
        return "Average"
    else:
        return "Poor"