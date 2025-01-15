from datetime import datetime
created_date = "2024-03-19"
issue_date = "2024-03-19"
created_date_obj = datetime.strptime(created_date,  "%Y-%m-%d")
issue_date_obj = datetime.strptime(issue_date, "%Y-%m-%d")

formatted_created_date = created_date_obj.strftime("%m-%d")
formatted_issue_date = issue_date_obj.strftime("%m-%d")


print("Created Date:", formatted_created_date)
print("Issue Date:", formatted_issue_date)