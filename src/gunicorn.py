import multiprocessing
bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 30
capture_output = True
enable_stdio_inheritance = True
