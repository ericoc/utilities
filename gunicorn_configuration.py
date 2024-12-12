from multiprocessing import cpu_count


worker_class = "gthread"
workers = cpu_count() * 2 + 1
threads = 2
keepalive = 300
capture_output = True
accesslog = errorlog = "/var/www/utilities/logs/gunicorn.log"
