from datetime import datetime

last_date_we_met= "2023-02-13"
specific_date = datetime.strptime(last_date_we_met, "%Y-%m-%d").date()
today = datetime.today().date()
days_difference = (today - specific_date).days

print(f"It has been {days_difference} days since we last met.Hope you doing well.🙃")
