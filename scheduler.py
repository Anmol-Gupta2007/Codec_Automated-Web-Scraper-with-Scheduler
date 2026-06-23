import schedule,time,scraper
schedule.every(10).minutes.do(lambda: __import__("scraper"))
while True:
    schedule.run_pending();time.sleep(1)
